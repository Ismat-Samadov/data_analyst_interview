# myscript.py

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="hr", password="hr",
                               dsn="localhost/xepdb1")

cursor = connection.cursor()
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = input("input department id : "),
        eid = input("input employee id : "))
for fname, lname in cursor:
    print("Values:", fname, lname)
input()