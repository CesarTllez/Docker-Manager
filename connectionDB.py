import psycopg2 as pg2

try:
    connectionDB = pg2.connect (
        database = "containers_db",
        user = "postgres",
        password = "H@wkers358s",
        host = "localhost",
        port = "5432"
    )
except pg2.Error as e:
    print(e)

cursor = connectionDB.cursor()

sqlCommands = {
    'insertSQL': 'INSERT INTO containers (id, name) VALUES (%s, %s)',
    'selectAllSQL': 'SELECT * FROM containers',
    'updateSQL': 'UPDATE containers SET name = %s WHERE id = %s',
    'deleteSQL': 'DELETE FROM containers WHERE id = %s'
}