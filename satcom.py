#! /bin/python3
# -*- coding: utf-8 -*-

from colorama import Back, Fore, Style, init
import os
import sys
import asyncio
import configparser
import json
import sys
import time
from datetime import datetime
from terminaltables import AsciiTable

init(autoreset=True)
# END IMPORT
__author__ = "-- Satcom --"
version = "0.0.1"


class Misc:
    def __init__(self):
        pass

    def printwt(msg):
        """Print message with current date and time"""
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_date_time}] {msg}")

    def print_board(tableList):
        """
        https://robpol86.github.io/terminaltables/
        tableList = []
        tableList = tableList.append(['Row one column one', 'Row one column two'])
        """
        table = AsciiTable(tableList)
        table.inner_row_border = True
        print(table.table)