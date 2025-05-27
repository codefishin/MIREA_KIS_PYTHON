import csv
import datetime
import matplotlib.pyplot as plt
from collections import Counter

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# Сообщения, присланные в ЦАП.
# 0    1     2        3      4
# id, task, variant, group, time
messages = load_csv('messages.csv')

# Результаты проверок сообщений, присланных в ЦАП.
#  0    1       2       3
# id, message, time, status
checks = load_csv('checks.csv')

# Состояния задач ЦАП.
#   0     1       2      3      4       5
# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

# Таблица соответствия номеров групп и их названий.
# 0     1
# Id, title
groups = load_csv('groups.csv')

# 1
statuses_time = []
for _ in range(0, len(statuses)):
    statuses_time.append(parse_time(statuses[_][3]).isoweekday())

c_st_time = Counter(statuses_time).most_common()
x = [item[0] for item in c_st_time]
y = [item[1] for item in c_st_time]


plt.bar(x, y)
plt.show()
print("из графика видно, что самое частое - день недели 1, то есть понедельник")
