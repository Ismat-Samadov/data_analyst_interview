import xlsxwriter
from xlsxwriter import Workbook
import cx_Oracle
import datetime
from datetime import date

#dsn_tns = cx_Oracle.makedsn('HOST', 'PORTNO', sid='localhost/xepdb1') 
    
#db = cx_Oracle.connect(user='hr', password='hr', dsn=dsn_tns)
connection = cx_Oracle.connect(user=input("please input your login : "), password=input("please input your password : "),
                               dsn="localhost/xepdb1")
cursor = connection.cursor()

workbook = xlsxwriter.Workbook('C:\\Users\\Ismat\\Downloads\\outfile.xlsx')
sheet = workbook.add_worksheet()


cursor.execute(input("please input your sql : "))
#("select * from employees")
for r, row in enumerate(cursor.fetchall()):
         for c, col in enumerate(row):
                sheet.write(r, c, col)

workbook.close()
cursor.close()
input()
