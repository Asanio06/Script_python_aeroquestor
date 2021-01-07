# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:55:00 2020

@author: Lansana Diomande

This script searches the French eAIP folder in order to insert 
in the database the list of charts for each airport.

"""
import os;
import mysql.connector

mydb = mysql.connector.connect(
  host="mysql-asanio.alwaysdata.net",
  user="asanio_php",
  password="]{jrcrmS{vRL48!<",
  database="asanio_api"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Chart_of_airport(ICAO_AIRPORT,Charts_type,Chart_name) VALUES (%s,%s,%s)"
values = []

folder = 'FRANCE\AIRAC-2020-12-31\html\eAIP\Cartes'

my_list = os.listdir(folder)


for airport in my_list :
    path  = airport
    with os.scandir(folder + path) as listOfEntries:
        for entry in listOfEntries:
            # print all entries that are files
            if entry.is_file():
                file_name = entry.name
                file_name_without_type = file_name.split('.')[0]
                values.append(tuple((airport,'IFR',file_name_without_type)))
                

print(values)

# mycursor.executemany(sql, values)

# mydb.commit()