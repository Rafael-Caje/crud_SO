from so_create_db import connect

tunnel, mydb = connect()

try:
  mycursor = mydb.cursor()
  mycursor.execute("USE debiandb")

  # Update a data row in the table
  mycursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (int(input('Digite a quantidade: ')), str(input('Digite a FRUTA: '))))
  print("Updated",mycursor.rowcount,"row(s) of data.")

  # Cleanup
  mydb.commit()
  mycursor.close()
  mydb.close()
  print("Done.")

finally:
  tunnel.stop