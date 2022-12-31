from cgi import test
import email
import random
import csv
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
from urllib.request import urlopen



class Person:
    def __init__(props, name, age):
        props.name = name
        props.age = age

    def findtravel(abc):
        print("Voayge de " + abc.name)

class Airport:
    def __init__(props, name, code,lat,long):
        props.name = name
        props.code = code
        props.lat = lat
        props.long = long
        
    def airports():
        fields = [] 
        with open(r'/home/ds/Documents/ESTIAM/PROJETS/TP - Vols avec-sans correspondances/aeroports.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile) 
            fields = next(csvreader)
            print('-'*40)
            for row in csvreader:
                print('-'*40)
                print('| ', row[0],'   |    ', row[1],' '*2, '|', row[2],' '*2, '|', row[3],' '*2, '|')
                print('-'*40)
        
class Flight:
    def __init__(props, src_code, dst_code,duration):
        props.src_code = src_code
        props.dst_code = dst_code
        props.duration = duration
        
    def flights():
        
        fields = [] 
        with open(r'/home/ds/Documents/ESTIAM/PROJETS/TP - Vols avec-sans correspondances/flights.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile) 
            fields = next(csvreader)
            print('-'*40)
            for row in csvreader:
                print('-'*40)
                print('| ', row[0],'   |    ', row[1],' '*2, '|', row[2],' '*2, '|')
                print('-'*40)
    
    
class FlightMap:
    def __init__(props, id):
        props.id = id
    
    def import_airports(csv_file : str):
        csv_file___ = csv.reader(open(csv_file, "r"), delimiter=",")
        return csv_file___
        
    def import_flights(csv_file : str):
        print('rerere')
        
    def airport_find(airport_code):
        print("cherche l'aéroport qui correspond au code")
        list_search = list()
        for row in FlightMap.import_airports('/home/ds/Documents/ESTIAM/PROJETS/TP - Vols avec-sans correspondances/aeroports.csv'):
            list_search.append({'NAME': row[0], 'CODE AIRPORT': row[1]})
        if len(list_search) < 1:
            print(list_search) 
        else:
            print('None')
            
        
    def flight_exist(src_airport_code: str, dst_airport_code: str) : bool
    
    def flights_where(airport_code: str):
        print("Cette méthode cherche les vols directs qui concernent l'aéroport airport_code, et retourne la liste des vols concernés")
        
    def airports_from(airport_code: str):
        print("Retourne la liste des aéroports destinations des vols en partance de l'aéroport airport_code (plutôt que les vols eux-mêmes).")

class FlightPathBroken(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
        print(message)
        pass

class FlightPathDuplicate(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
        print(message)
        pass
    
class FlightPath:
    def __init__(src_airport : Airport):
        # qui représentera un chemin.   
        src_airport = Airport
    
    
if __name__ == "__main__":
    p1 = Person("John", 36)
    p1.findtravel()
    
    ans=True
    while ans:
        print("""
        1.Retourne la liste des aéroports
        2.Retourne la liste complète des vols
        3.Cherche l'aéroport qui correspond au code
        4.S'il existe un vol direct entre l'aéroport src_airport_code et l'aéroport dst_airport_code
        5.Cherche les vols directs qui concernent l'aéroport airport_code
        6.Retourne la liste des aéroports destinations des vols en partance de l'aéroport airport_code
        7.Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            print("\nla liste des aéroports")
            airports = Airport.airports()
            print(airports)
            print("\n--------------------------------------------------\n")
        elif ans=="2":
            print("\n Listes flights VOLS")
            flights = Flight.flights()
            print(flights)
            print("\n--------------------------------------------------\n")
        elif ans=="3":
            airport_code = str(input("\n Entrer le code de l'aéroport "))
            print("\n"+ airport_code +"\n")
            airport_code = FlightMap.airport_find(airport_code)
            airport_code()
            print("\n--------------------------------------------------\n")
        elif ans=="4":
            print("\n Goodbye") 
            ans = None
            print("\n--------------------------------------------------\n")
        elif ans=="5":
            print("\n Student Record Found")
            print("\n--------------------------------------------------\n")
        elif ans=="6":
            print("\n Student Record Found")
            print("\n--------------------------------------------------\n")
        elif ans=="7":
            print("\n Student Record Found")
            print("\n--------------------------------------------------\n")
        else:
            print("\n Not Valid Choice Try again")
