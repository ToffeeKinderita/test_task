import logging
import string
import random

from utils.constants import TestData


def generate_unique_str(k: int, pool: str = string.ascii_letters) -> str:
    """Generate a unique string.
    k: Length of each string
    pool: Iterable of characters to choose from
    """
    join = ''.join
    token = join(random.choices(pool, k=k))
    return token


class MyLogger:
    def get_logger_custom(self, name, level=logging.INFO, file=None):
        logging.basicConfig(format=TestData.LOGGER_FORMAT, level=level, filename=file)
        logger = logging.getLogger(name)
        return logger
