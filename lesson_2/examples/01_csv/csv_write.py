""" Модуль csv_write """

import csv

DATA = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', 2960, 'Moscow, str'],
        ['kp2', 'Cisco', 2960, 'Novosibirsk, str'],
        ['kp3', 'Cisco', 2960, 'Kazan, str'],
        ['kp4', 'Cisco', 2960, 'Tomsk, str']]

print()
print('----- простая запись данных в файл .csv и вывод результата -----')
with open('kp_data_write_1.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n)
    for row in DATA:
        F_N_WRITER.writerow(row)

print('----- читаем как txt файл -----')
with open('kp_data_write_1.csv') as f_n:
    LINES = f_n.read()
    print(LINES)

print('----- читаем как csv файл -----')
with open('kp_data_write_1.csv') as f_n:
    LINES = csv.reader(f_n)
    for row in LINES:
        print(row)

print()
print('----- quoting=csv.QUOTE_NONNUMERIC только при записи -----')
with open('kp_data_write_2.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n, quoting=csv.QUOTE_ALL)
    for row in DATA:
        F_N_WRITER.writerow(row)

with open('kp_data_write_2.csv') as f_n:
    LINES = csv.reader(f_n)
    for row in LINES:
        print(row, type(row[2]))

print()
print('----- quoting=csv.QUOTE_NONNUMERIC и при записи, и при чтении -----')
with open('kp_data_write_3.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    F_N_WRITER.writerows(DATA)

with open('kp_data_write_3.csv') as f_n:
    LINES = csv.reader(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in LINES:
        print(row, type(row[2]))

print()
print('----- изменение формата разделителя delimiter="|" -----')
with open('kp_data_delimiter.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n, delimiter="|")
    F_N_WRITER.writerows(DATA)

with open('kp_data_delimiter.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    for row in F_N_READER:
        print(row)

print()
print('----- список словарей в качестве исходных данных -----')
DATA = [{'hostname': 'kp1',
         'location': 'Moscow',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp2',
         'location': 'Novosibirsk',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp3',
         'location': 'Kazan',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp4',
         'location': 'Tomsk',
         'model': '2960',
         'vendor': 'Cisco'}]

with open('kp_data_dictwriter.csv', 'w') as f_n:
    F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(DATA[0].keys()))
    F_N_WRITER.writeheader()
    for d in DATA:
        F_N_WRITER.writerow(d)

with open('kp_data_dictwriter.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    for row in F_N_READER:
        print(row)
