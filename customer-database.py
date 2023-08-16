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

print("This is a list of all the customers")
for x in custresult:
  print(x)
