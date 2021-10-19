"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess import
from chardet import detect

    
# решение Николая Петрова    
def_coding = locale.getpreferredencoding()
# print(def_coding)

ping = ["yandex.ru", "youtube.com"]

command = ["ping", "-c", "4"]

for url in ping:
    subproc_command = subprocess.Popen([*command, url], stdout=subprocess.PIPE)
    print(f"Result command {' '.join([*command, url])}:\n")
    for line in subproc_command.stdout:
        print(line.decode(def_coding).encode('utf-8').decode('utf-8'))
    else:
        print()
        
        
# решение Никиты Черенкова

ping_ya = subprocess.Popen(('ping', 'ya.ru'), stdout=subprocess.PIPE, encoding='utf-8')

for i, line in enumerate(ping_ya.stdout):
    ping_ya.kill() if i == 5 else print(line)   
    


# решение Сергея Аверченкова
  
def ping_service(service):
    args = ['ping', service]
    ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    count = 0  # Для выхода из режима пингования
    for line in ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        if count == 4:
            break
        count += 1


ping_service('yandex.ru')
ping_service('youtube.com')

    
       
