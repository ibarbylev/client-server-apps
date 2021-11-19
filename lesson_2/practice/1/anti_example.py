import csv
import re

import chardet


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    os_prod_pattern = re.compile('Изготовитель системы:')
    os_name_pattern = re.compile('Название ОС:')
    os_code_pattern = re.compile('Код продукта:')
    os_type_pattern = re.compile('Тип системы:')
    headers = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    for i in range(3):
        file = f'info_{i+1}.txt'
        with open(file, "rb") as f:
            data = f.read()
            charset = chardet.detect(data)
            data = data.decode(charset["encoding"])
            lines_array = data.split("\n")
            for line in lines_array:
                if len(os_prod_pattern.split(line)) > 1:
                    os_prod_list.append(os_prod_pattern.split(line)[1].strip())

                if len(os_name_pattern.split(line)) > 1:
                    os_name_list.append(os_name_pattern.split(line)[1].strip())

                if len(os_code_pattern.split(line)) > 1:
                    os_code_list.append(os_code_pattern.split(line)[1].strip())

                if len(os_type_pattern.split(line)) > 1:
                    os_type_list.append(os_type_pattern.split(line)[1].strip())

    return [headers, os_prod_list, os_name_list, os_code_list, os_type_list]

    # data_transformed = list(zip(os_prod_list, os_name_list, os_code_list, os_type_list))
    # return [headers] + data_transformed


def write_to_csv(data):
    with open('anti_result.csv', 'w', encoding="utf-8") as f:
        csv.writer(f).writerows(data)


write_to_csv(get_data())
