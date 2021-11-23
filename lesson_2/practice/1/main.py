"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
"""

import re
import csv

import chardet


def get_data():
    """Get data from txt-file"""

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file_obj:
            data_bytes = file_obj.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encoding'])

        # get a list of OS manufacturers
        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

        # get a list of OS names
        os_name_reg = re.compile(r'Windows\s\S*')
        os_name_list.append(os_name_reg.findall(data)[0])

        # get a list of products code
        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])

        # get a list of systems type
        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    data_for_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]  # matrix 4 x 3

    # make matrix (4 x 3) from matrix (3 x 4)
    for idx in range(len(data_for_rows[0])):
        line = [row[idx] for row in data_for_rows]
        main_data.append(line)

    # variant 2
    # for idx in range(len(data_for_rows[0])):
    #     line = list(map(lambda row: row[idx], data_for_rows))
    #     main_data.append(line)

    # variant 3
    # for idx in range(len(data_for_rows[0])):
    #     main_data.append([os_prod_list[idx], os_name_list[idx], os_code_list[idx], os_type_list[idx])

    # variant 4 zip-transformation
    # list(zip([1, 2, 3],                [(1, 4),
    #          [4, 5, 6]))      ==>       (2, 5),
    #                                     (3, 6)]

    # variant 5 T-transformation in numpy
    # import numpy as np
    # main_data = np.array(main_data, dtype=str).T.tolist()
    # создаём массив numpy, трансформируем его (.T) и тут же снова превращаем в список (tolist)

    return main_data


def write_to_csv(out_file):
    """Write the data to csv-file"""

    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_report.csv')
