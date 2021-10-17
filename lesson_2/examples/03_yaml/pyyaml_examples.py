"""Модуль pyyaml_examples"""

import yaml  # pip3 install pyyaml

# считываем данные
with open('data_read.yaml', encoding='utf-8') as f_n:
    F_N_CONTENT = yaml.load(f_n, Loader=yaml.FullLoader)
print(F_N_CONTENT)

# изменяем формат записи (+ для символов юникода)
ACTION_LIST = ['msg_1', 'msg_2', 'msg_3']
TO_LIST = ['account_1', 'account_2', 'account_3']
# TO_LIST = ['account_1', 'account_2', 'вася']
DATA_TO_YAML = {'action': ACTION_LIST, 'to': TO_LIST}

with open('data_write.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(DATA_TO_YAML, f_n)
    # yaml.dump(DATA_TO_YAML, f_n, allow_unicode=True)

with open('data_write.yaml', encoding='utf-8') as f_n:
    print(f_n.read())


