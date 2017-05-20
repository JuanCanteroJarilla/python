#/usr/bin/python
#-*-encoding:utf-8-*-

import csv
import MySQLdb

mydb = MySQLdb.connect('localhost','root','root','pruebaPython')
cursor = mydb.cursor()


with open('/home/juan/Escritorio/salario.csv') as csvfile:
    next(csvfile)
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        cursor.execute('INSERT INTO pruebaPython.EMPLEADO(SALARIO)VALUES(%f)'%(float(row[0])))
        print(row[0])

mydb.commit()
cursor.close()
print "Done"