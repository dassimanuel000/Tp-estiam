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
        csv_file = "/home/ds/Documents/ESTIAM/PROJETS/TP - Vols avec-sans correspondances/aeroports.csv"
        return csv_file
        
    def import_flights(csv_file : str):
        csv_file = "/home/ds/Documents/ESTIAM/PROJETS/TP - Vols avec-sans correspondances/flights.csv"
        return csv_file
        
    def airport_find(airport_code):
        with open(FlightMap.import_airports('0')) as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                try:
                    if airport_code in row[1]:
                        value =  str(row[0]) + '   |    '+ str(row[1])+'  |    '+ str(row[2]) + ' |\n'
                        return value
                except FlightPathBroken:
                    continue

        
    def flight_exist(src_airport_code: str, dst_airport_code: str):
        with open(FlightMap.import_flights('0')) as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                try:
                    if src_airport_code in row[0] and dst_airport_code in row[1] and "1.0" in str(row[2]):
                        return True
                except FlightPathBroken:
                    continue
                
    def flights_where(airport_code: str):
        value = ''
        print("Cette méthode cherche les vols directs qui concernent l'aéroport airport_code, et retourne la liste des vols concernés")
        with open(FlightMap.import_flights('0')) as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                try:
                    if airport_code in row[0] and "1.0" in str(row[2]):
                        value += '\n'+('-'*40)
                        value +=  str(row[0]) + '   |    '+ str(row[1])+'  |    '+ str(row[2]) + ' |\n'
                except FlightPathBroken:
                    continue
        return value
        
    def airports_from(airport_code: str):
        value = ''
        print("Retourne la liste des aéroports destinations des vols en partance de l'aéroport airport_code (plutôt que les vols eux-mêmes).")
        with open(FlightMap.import_flights('0')) as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                try:
                    if airport_code in row[0]:
                        return FlightMap.airport_find(row[1])
                except FlightPathBroken:
                    continue
        return value

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
            result = FlightMap.airport_find(airport_code)
            print(result)
            print("\n--------------------------------------------------\n")
        elif ans=="4":
            src_airport_code = str(input("\n Entrer le code de src_airport_code l'aéroport  ex: FRA "))
            dst_airport_code = str(input("\n Entrer le code de dst_airport_code l'aéroport   ex: AMS "))
            result = FlightMap.flight_exist(src_airport_code,dst_airport_code)
            print(result)
            print("\n--------------------------------------------------\n")
        elif ans=="5":
            
            airport_code = str(input("\n Entrer le code de l'aéroport "))
            result = FlightMap.flights_where(airport_code)
            print(result)
            print("\n--------------------------------------------------\n")
        elif ans=="6":
            airport_code = str(input("\n Entrer le code de l'aéroport "))
            result = FlightMap.flights_where(airport_code)
            print(result)
            print("\n--------------------------------------------------\n")
        elif ans=="7":
            ans = None
            break
        else:
            print("\n Not Valid Choice Try again")
