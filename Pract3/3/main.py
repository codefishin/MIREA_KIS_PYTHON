import csv
import datetime
import matplotlib.pyplot as plt
from collections import Counter


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

class CSVParser:
    def __init__(self):
        # Сообщения, присланные в ЦАП.
        # 0    1     2        3      4
        # id, task, variant, group, time
        self.messages = load_csv('messages.csv')

        # Результаты проверок сообщений, присланных в ЦАП.
        #  0    1       2       3
        # id, message, time, status
        self.checks = load_csv('checks.csv')

        # Состояния задач ЦАП.
        #   0     1       2      3      4       5
        # task, variant, group, time, status, achievements
        self.statuses = load_csv('statuses.csv')

        # Таблица соответствия номеров групп и их названий.
        # 0     1
        # Id, title
        self.groups = load_csv('groups.csv')

    def __show_as_bar(self, data):
        _x = [item[0] for item in data]
        _y = [item[1] for item in data]
        plt.bar(_x, _y)
        plt.show()

    def table_1(self):
        statuses_time = []
        for _ in range(0, len(self.statuses)):
            statuses_time.append(parse_time(self.statuses[_][3]).isoweekday())

        c_st_time = Counter(statuses_time).most_common()
        self.__show_as_bar(c_st_time)

    def table_2(self):
        student_work_time = []
        for _ in range(0, len(self.messages)):
            student_work_time.append(parse_time(self.messages[_][4]).hour)

        student_work_time = Counter(student_work_time).most_common()
        self.__show_as_bar(student_work_time)

    def table_3(self):
        student_try = []
        for _ in range(0, len(self.messages)):
            student_try.append(self.messages[_][1])
        student_try = Counter(student_try).most_common()
        self.__show_as_bar(student_try)

    def table_5(self):
        groups = []
        for _ in range(0, len(self.messages)):
            groups.append(self.messages[_][3])
        self.__show_as_bar(Counter(groups).most_common())

    def table_8(self):
        groups = {'': 0}
        for _ in range(0, len(self.statuses)):
            groups.update({self.statuses[_][2]: 0})
            if self.statuses[_][2] in groups:
                groups.update({self.statuses[_][2]: groups.get(self.statuses[_][2]) + len(self.statuses[_][5])})
        self.__show_as_bar(Counter(groups).most_common())


def main():
    csv_p = CSVParser()
    csv_p.table_1()
    csv_p.table_2()
    csv_p.table_3()
    csv_p.table_5()
    csv_p.table_8()


if __name__ == '__main__':
    main()
