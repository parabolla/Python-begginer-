import logging


def my_logger(func):
    logger = logging.getLogger('Логируем все подряд')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('logger.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(module)s - %(lineno)d')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info('Логгер был запущен и выведен')
    func()
    return func


@my_logger
def asd():
    pass
