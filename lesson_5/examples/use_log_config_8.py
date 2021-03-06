"""
Логирование с использованием модуля logging
Вынесение настройки логирования в отдельный модуль
"""

import logging
import log_config_7

# Обратите внимание, логер уже создан в модуле log_config,
# теперь нужно его просто получить
log = logging.getLogger('app.main')


def main():
    """Тестовая главная функция"""

    log.debug('Старт приложения')


if __name__ == '__main__':
    main()
