import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest.log')
logger.addHandler(h)

logging.info('from logtest log')
logger.info('from logtest log')
