from so_create_db import connect

tunnel, mydb = connect()

try:
  # Crie um objeto cursor para executar comandos SQL
  mycursor = mydb.cursor()

  # Execute o comando para verificar e criar se o banco de dados não existir
  mycursor.execute("CREATE DATABASE IF NOT EXISTS debiandb")

  # Use o Banco de Dados
  mycursor.execute("USE debiandb")

  # Drop previous table of same name if one exists
  mycursor.execute("DROP TABLE IF EXISTS inventory;")
  print("Finished dropping table (if existed).")

  # Create table
  mycursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

  # Insert some data into table
  mycursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);",
                   ("banana", 207))
  print("Inserted",mycursor.rowcount,"row(s) of data.")
  mycursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);",
                   ("laranja", 173))
  print("Inserted",mycursor.rowcount,"row(s) of data.")
  mycursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);",
                   ("maçã", 122))
  print("Inserted",mycursor.rowcount,"row(s) of data.")

  # Cleanup
  mydb.commit()
  mycursor.close()
  mydb.close()
  print("Done.")

finally:
  tunnel.stop
