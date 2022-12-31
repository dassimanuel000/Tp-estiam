from cgi import test
import email
import random
from logging import exception
import html2text
from datetime import datetime
from os.path import exists
# pour colorer les prints
from colorama import Fore
from colorama import Style
from urllib.parse import ParseResult, urlparse
# pour colorer les prints
import colorama
import os
import os.path
import re
import time
import json
import pymongo
import json
from pymongo import MongoClient
from pprint import pprint
import urllib.request
from urllib.parse import ParseResult, urlparse
import pandas as pd
from googletrans import Translator
translator = Translator()
import html




class Person:
    def __init__(props, name, age):
        props.name = name
        props.age = age

    def findtravel(abc):
        print("Voayge de " + abc.name)


if __name__ == "__main__":
    p1 = Person("John", 36)
    p1.findtravel()