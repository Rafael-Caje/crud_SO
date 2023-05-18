from so_create_db import connect

tunnel, mydb = connect()

try:
  mycursor = mydb.cursor()
  mycursor.execute("USE debiandb")

  # Read data
  mycursor.execute("SELECT * FROM inventory;")
  rows = mycursor.fetchall()
  print("Read", mycursor.rowcount, "row(s) of data.")

  # Print all rows
  for row in rows:
      print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  mydb.commit()
  mycursor.close()
  mydb.close()
  print("Done.")
    
finally:
  tunnel.stop()