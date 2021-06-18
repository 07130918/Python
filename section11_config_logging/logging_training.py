"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

formatter = '%(levelname)s: %(message)s: %(asctime)s'
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format=formatter)
# logging.basicConfig(filename='test.log', level=logging.INFO)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

logging.info('info {}'.format('test'))
logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')
