from PyQt5.QtSql import *
# contoh cara membuat database menggunakan python
def connectdb():
    # menerapkan library QtSql dari PyQt5
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()

        # membuat tabel
        sql = '''Create table phonebook(
        id integer not null primary key,
        nama varchar(25),
        nohp varchar(25)
        )'''
        query.exec_(sql)

        # jika berhasil maka akan menampilkan output berhasil
        if (query.exec_):
            print('Berhasil membuat tabel')
    else:
        print('ERROR: ' + db.lastError().text())
connectdb()
