#! /usr/bin/env python3

import logging
import sys

logger = logging.getLogger('my_logger_name')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('log.out')
stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug('Hello, logger!')
