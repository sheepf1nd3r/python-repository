import mysql.connector

custdb = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  password="dbpassword",
  database="customerdb"
)

custcursor = custdb.cursor()

custcursor.execute("SELECT * FROM customers")

custresult = custcursor.fetchall()

for x in custresult:
  print(x)
