#!/usr/bin/env python

import MySQLdb
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in("******","******")

conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="world")
cursor = conn.cursor()

sql = 'select Name, Continent, Population, LifeExpectancy, GNP from Country'
cursor.execute(sql)
rows = cursor.fetchall()
str(rows[0:300])

df = pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns={0: 'Name', 1: 'Continent', 2: 'Population', 3: 'LifeExpectancy', 4: 'GNP'}, inplace=True)
df = df.sort_values(['LifeExpectancy'], ascending=[1])
df.head()
