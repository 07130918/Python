"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

logging.basicConfig(level=logging.INFO)

logging.info('info')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')
