import random
from collections import defaultdict


class TextModel:
    def __init__(self, order):
        self.order = order
        self.model = defaultdict(lambda: defaultdict(int))


    def train(self, text_):
        # обработка
        text_ = text_.strip()
        for i in range(len(text_) - self.order):
            prefix = text_[i:i + self.order]
            next_char = text_[i + self.order]
            self.model[prefix][next_char] += 1

    def generate(self, length, seed):
        current_prefix = seed
        result = seed

        for _ in range(length):
            if current_prefix not in self.model:
                break

            next_chars = self.model[current_prefix]
            total = sum(next_chars.values())
            rand = random.randint(1, total)

            cumulative = 0
            for char, freq in next_chars.items():
                cumulative += freq
                if cumulative >= rand:
                    result += char
                    current_prefix = current_prefix[1:] + char
                    break

        return result


def read_data(file_name=''):
    if file_name == '':
        return None
    f = open(file_name, "r+", encoding="utf8")
    return f.read()


def main(prefix=100, length=500):
    text = read_data('pushkin.txt')
    seed_prefix = text[:prefix]

    model = TextModel(prefix)
    model.train(text)
    generated_text = model.generate(length, seed_prefix)

    f = open("result.txt", "w", encoding="utf8")
    f.write(generated_text)


if __name__ == "__main__":
    main()
