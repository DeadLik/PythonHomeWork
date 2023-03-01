import logging
import controller

try:
    controller.start()
except KeyboardInterrupt:
    logging.exception('Некорректное завершение программы')
