#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

# создаём подключение с помощью метода Connect
db = MySQLdb.connect("localhost","root","0000","diplom")

# создаём объект db с помощью метода cursor() модуля MySQLdb
cursor = db.cursor()

# выполняем SQL запрос с помощью метода execute()
cursor.execute("select version()")

# предыдущая строка возвращает объект класса Connection;
# выполним метод fetchone для получения одной строки
# или fetchall для получения всех
data = cursor.fetchone()

print "Версия MySQL : %s " % data
cursor.execute("show tables")
for data in cursor:
  print data[0]
# и отключаемся от сервера
db.close()
gc.collect()