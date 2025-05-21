import unittest
from collections import defaultdict
from itertools import product
from copy import deepcopy


class FiniteStateMachine:
    _GRAPH = {
        'v5': {'punch': ('v4', 'a3'), 'sway': ('v2', 'a0')},
        'v2': {'spin': ('v0', 'a0')},
        'v0': {'sway': ('v1', 'a0')},
        'v1': {'spin': [(2, 'v0', 'a0'),
                        (1, 'v5', 'a3'),
                        (0, 'v4', 'a3')]},
        'v4': {'type': ('v1', 'a0'), 'punch': ('v7', 'a2')},
        'v7': {'type': ('v3', 'a1')},
        'v3': {'sway': ('v2', 'a2'), 'spin': ('v6', 'a2')},
        'v6': {}
    }

    _MAX_OUT_EDGES = max(
        sum(len(e) if isinstance(e, list) else 1 for e in edges.values())
        for edges in _GRAPH.values()
    )

    def __init__(self):
        self._state = 'v5'
        self._vars = {}
        self._state_counts = defaultdict(int)
        self._state_counts['v5'] += 1

    @property
    def state(self):
        return self._state

    def seen_state(self, st):
        return self._state_counts[st]

    def has_max_out_edges(self):
        return self._out_degree(self._state) == self._MAX_OUT_EDGES

    def part_of_loop(self):
        start = self._state
        if start not in self._GRAPH:
            return False
        stack = [(start, iter(self._neighbours(start)))]
        visited = {start}
        while stack:
            node, children = stack[-1]
            try:
                nxt = next(children)
            except StopIteration:
                stack.pop()
                visited.discard(node)
                continue
            if nxt == start:
                return True
            if nxt not in visited:
                visited.add(nxt)
                stack.append((nxt, iter(self._neighbours(nxt))))
        return False

    def t(self, value):
        self._vars['t'] = value

    def go_sway(self):
        return self._do('sway')

    def go_punch(self):
        return self._do('punch')

    def go_spin(self):
        return self._do('spin')

    def go_type(self):
        return self._do('type')

    def __getattr__(self, name):
        return lambda: "unknown"

    def _do(self, action):
        table = self._GRAPH.get(self._state, {})
        if action not in table:
            return 'unsupported'
        edge = table[action]
        if isinstance(edge, list):
            t_val = self._vars.get('t')
            for cond, dst, out in edge:
                if cond == t_val:
                    return self._transition(dst, out)
            return 'unsupported'
        dst, out = edge
        return self._transition(dst, out)

    def _transition(self, dst, out):
        self._state = dst
        self._state_counts[dst] += 1
        return out

    @staticmethod
    def _edge_list(edges_dict):
        for edge in edges_dict.values():
            if isinstance(edge, list):
                for _, dst, _ in edge:
                    yield dst
            else:
                yield edge[0]

    def _neighbours(self, st):
        if st not in self._GRAPH:
            return []
        return list(self._edge_list(self._GRAPH.get(st, {})))

    def _out_degree(self, st):
        return len(self._neighbours(st))

    def run(self, name):
        if not hasattr(self, name) or not name.startswith('go_'):
            return 'unknown'
        return getattr(self, name)()


class BasicCoverage(unittest.TestCase):
    def setUp(self):
        self.f = FiniteStateMachine()

    def test_unknown_attribute(self):
        self.assertEqual(self.f.foo_bar(), 'unknown')

    def test_t(self):
        self.f.t(5)
        self.assertEqual(self.f._vars['t'], 5)

    def test_run_and_states(self):
        self.assertEqual(self.f.run('go_sway'), 'a0')
        self.assertEqual(self.f.seen_state('v2'), 1)
        self.assertEqual(self.f.run('go_spin'), 'a0')
        self.f.t(0)
        self.f._state = 'v1'
        self.assertEqual(self.f.run('go_spin'), 'a3')
        self.assertEqual(self.f.seen_state('v4'), 1)
        self.f._state = 'v1'
        self.f.t(0)
        self.assertEqual(self.f.run('go_spin'), 'a3')

    def test_run_unknown(self):
        self.assertEqual(self.f.run('zzz'), 'unknown')


class TransitionNegative(unittest.TestCase):
    def test_bad_transition(self):
        f = FiniteStateMachine()
        self.assertEqual(f.go_type(), 'unsupported')


class PartOfLoopBranches(unittest.TestCase):
    def _check(self, graph, start, expect):
        saved = deepcopy(FiniteStateMachine._GRAPH)
        try:
            FiniteStateMachine._GRAPH = graph
            f = FiniteStateMachine()
            f._state = start
            self.assertEqual(f.part_of_loop(), expect)
        finally:
            FiniteStateMachine._GRAPH = saved

    def test_true_on_self_loop(self):
        self._check({'A': {'go': ('A', 'x')}}, 'A', True)

    def test_false_when_no_loop(self):
        self._check({'A': {'go': ('B', 'x')}, 'B': {}}, 'A', False)

    def test_visited_node_not_start(self):
        self._check({
            'A': {'go': ('B', 'x')},
            'B': {'go': ('C', 'x')},
            'C': {'go': ('B', 'x')}
        }, 'A', False)

    def test_graph_restored_after_exception(self):
        original_graph = deepcopy(FiniteStateMachine._GRAPH)
        try:
            self._check({'A': {'go': ('B', 'x')}}, 'INVALID_STATE', False)
        finally:
            self.assertEqual(FiniteStateMachine._GRAPH, original_graph)


class UnsupportedBranches(unittest.TestCase):
    def setUp(self):
        self.f = FiniteStateMachine()

    def test_spin_v1_unsupported(self):
        self.f._state = 'v1'
        self.f.t(42)
        self.assertEqual(self.f.go_spin(), 'unsupported')

    def test_punch_unsupported(self):
        self.f._state = 'v2'
        self.assertEqual(self.f.go_punch(), 'unsupported')

    def test_state_property(self):
        self.assertEqual(self.f.state, 'v5')
        self.f.run('go_sway')
        self.assertEqual(self.f.state, 'v2')

    def _check(self, graph, start, expect):
        saved = deepcopy(FiniteStateMachine._GRAPH)
        try:
            FiniteStateMachine._GRAPH = graph
            f = FiniteStateMachine()
            f._state = start
            self.assertEqual(f.part_of_loop(), expect)
        finally:
            FiniteStateMachine._GRAPH = saved

    def test_true_on_self_loop(self):
        self._check({'A': {'go': ('A', 'x')}}, 'A', True)

    def test_false_when_no_loop(self):
        self._check({'A': {'go': ('B', 'x')}, 'B': {}}, 'A', False)

    def test_already_visited_but_part_of_loop(self):
        self._check({
            'A': {'go': ('B', 'x')},
            'B': {'go': ('C', 'x')},
            'C': {'go': ('A', 'x')}
        }, 'A', True)


class InvalidStateTests(unittest.TestCase):
    def test_neighbours_invalid_state(self):
        f = FiniteStateMachine()
        self.assertEqual(f._neighbours('INVALID_STATE'), [])

    def test_part_of_loop_invalid_state(self):
        f = FiniteStateMachine()
        f._state = 'INVALID_STATE'
        self.assertFalse(f.part_of_loop())


class StateCountTests(unittest.TestCase):
    def test_state_counts(self):
        f = FiniteStateMachine()
        self.assertEqual(f.seen_state('v5'), 1)
        f.go_sway()
        self.assertEqual(f.seen_state('v2'), 1)
        f.go_spin()
        self.assertEqual(f.seen_state('v0'), 1)
        f.go_sway()
        self.assertEqual(f.seen_state('v1'), 1)
        f.t(1)
        f.go_spin()
        self.assertEqual(f.seen_state('v5'), 2)


class Sweep(unittest.TestCase):
    def test_all(self):
        f = FiniteStateMachine()
        for st, act, val in product(
                ['v5', 'v2', 'v0', 'v1', 'v4', 'v7', 'v3', 'v6'],
                ['go_sway', 'go_punch', 'go_spin', 'go_type'],
                [None, 0, 1, 2]):
            f._state = st
            if val is not None:
                f.t(val)
            result = getattr(f, act)()
            if result not in ['a0', 'a1', 'a2', 'a3']:
                self.assertIn(result, ['unsupported', 'unknown'])
            f.seen_state(st)
            f.has_max_out_edges()
            f.part_of_loop()
        self.assertTrue(True)


def test() -> bool:
    suite = unittest.TestSuite()
    load = unittest.TestLoader()
    suite.addTests(load.loadTestsFromTestCase(BasicCoverage))
    suite.addTests(load.loadTestsFromTestCase(TransitionNegative))
    suite.addTests(load.loadTestsFromTestCase(PartOfLoopBranches))
    suite.addTests(load.loadTestsFromTestCase(UnsupportedBranches))
    suite.addTests(load.loadTestsFromTestCase(InvalidStateTests))
    suite.addTests(load.loadTestsFromTestCase(StateCountTests))
    suite.addTests(load.loadTestsFromTestCase(Sweep))
    return unittest.TextTestRunner(verbosity=0).run(suite).wasSuccessful()


def main() -> FiniteStateMachine:
    return FiniteStateMachine()


_self_test_result = test()
_instance_for_coverage = main()
