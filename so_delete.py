from so_create_db import connect

tunnel, mydb = connect()

try:
  mycursor = mydb.cursor()
  mycursor.execute("USE debiandb")

  mycursor.execute("SELECT * FROM inventory;")
  rows = mycursor.fetchall()
  print("Read", mycursor.rowcount, "row(s) of data.")
  for row in rows:
    print("Fruta = (%s)" %(str(row[1])))

  # Delete a data row in the table
  mycursor.execute("DELETE FROM inventory WHERE name=%(param1)s;",
                   {'param1':str(input('Qual fruta você vai remover? '))})
  print("Deleted",mycursor.rowcount,"row(s) of data.")
  
  # Cleanup
  mydb.commit()
  mycursor.close()
  mydb.close()
  print("Done.")
finally:
  tunnel.stop