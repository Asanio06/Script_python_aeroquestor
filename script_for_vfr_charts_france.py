# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:26:33 2021

@author: Lansana Diomande
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

folder = 'Atlas-VAC\PDF_AIPparSSection\VAC\AD'


with os.scandir(folder) as listOfEntries:
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            file_name = entry.name
            file_name_clean = file_name.split('.')[1]
            values.append(tuple((file_name_clean,'VFR',file_name)))
                

print(values)

mycursor.executemany(sql, values)

mydb.commit()