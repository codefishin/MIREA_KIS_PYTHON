class MealyMachine:
    def __init__(self):
        self.state = 'v5'
        self.vars = 2
        self.visited_states = {'v0': 0, 'v1': 0,
                               'v2': 0, 'v3': 0,
                               'v4': 0, 'v5': 1,
                               'v6': 0, 'v7': 0}
        self.step_count = 0
        self.transitions = {
            'v0': {
                'sway': ('v1', 'a0'),
            },
            'v1': {
                'spin': ('v0', 'a0') if self.vars == 2
                else ('v5', 'a3') if self.vars == 1
                else ('v4', 'a3')
            },
            'v2': {
                'spin': ('v0', 'a0')
            },
            'v3': {
                'spin': ('v6', 'a2'),
                'sway': ('v2', 'a2')
            },
            'v4': {
                'punch': ('v7', 'a2'),
                'type': ('v1', 'a0')
            },
            'v5': {
                'sway': ('v2', 'a0'),
                'punch': ('v4', 'a3')
            },
            'v6': {},
            'v7': {
                'type': ('v3', 'a1')
            }
        }

        self.out_edges = {'v0': 1, 'v1': 3,
                          'v2': 1, 'v3': 2,
                          'v4': 2, 'v5': 2,
                          'v6': 0, 'v7': 1}
        self.cycles = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v7']

    def t(self, value):
        self.vars = value
        if self.vars == 2:
            self.transitions['v1']['spin'] = ('v0', 'a0')
        if self.vars == 1:
            self.transitions['v1']['spin'] = ('v5', 'a3')
        if self.vars == 0:
            self.transitions['v1']['spin'] = ('v4', 'a3')

    def _make_transition(self, method_name):
        method_name = method_name.replace('go_', '')
        all_methods = set()
        for state in self.transitions:
            all_methods.update(self.transitions[state].keys())
        if method_name not in self.transitions[self.state]:
            return 'unsupported'
        next_state, output = self.transitions[self.state][method_name]
        self.state = next_state
        self.visited_states[self.state] += 1
        self.step_count += 1
        return output

    def has_max_out_edges(self):
        current_out = self.out_edges[self.state]
        max_out = 3
        return current_out == max_out

    def seen_state(self, state):
        return self.visited_states.get(state, 0)

    def part_of_loop(self):
        return self.state in self.cycles

    def go_sway(self):
        return self._make_transition('sway')

    def go_spin(self):
        return self._make_transition('spin')

    def go_punch(self):
        return self._make_transition('punch')

    def go_type(self):
        return self._make_transition('type')

    def __getattr__(self, name):
        return lambda: "unknown"


def test():
    obj = MealyMachine()
    assert main() is not None
    assert obj.t(0) is None
    assert obj.go_type() == 'unsupported'
    assert obj.go_sway() == 'a0'
    assert obj.go_punch() == 'unsupported'
    assert obj.go_spin() == 'a0'
    assert obj.go_crawl() == 'unknown'
    assert obj.has_max_out_edges() is False
    assert obj.part_of_loop() is True
    assert obj.seen_state('v3') == 0
    assert obj.go_sway() == 'a0'
    assert obj.go_spin() == 'a3'
    assert obj.go_punch() == 'a2'
    assert obj.part_of_loop() is True
    assert obj.go_type() == 'a1'
    assert obj.go_spin() == 'a2'
    assert obj.t(2) is None
    assert obj.t(1) is None
    assert obj.t(0) is None


def main():
    return MealyMachine()
