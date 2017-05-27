#!/usr/bin/python3


import json
import logging
import os
import sys

print("Content-type: text/html\n")

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename='mylog.log')

raw_data = sys.stdin.read()

logging.info(json.loads(raw_data))
logging.info('======')
logging.info(raw_data)
