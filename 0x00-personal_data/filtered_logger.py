#!/usr/bin/env python3
"""obfuscates a log message"""

from typing import List
import re
import logging
# import mysql.connector
from os import getenv


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str) -> str:
    """returns a log message obfucated"""

    for i in fields:
        message = re.sub(i + "*?" + seperator,
                         i + "=" + redaction + seperator, message)

    return message
