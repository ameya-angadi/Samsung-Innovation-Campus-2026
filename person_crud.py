import pymysql

def connect_db():
    try:
        connection = pymysql.connect(user = 'root', password='root', port=3306, database='ameya', charset='utf8', host='localhost')
        print('DB Connected')
        return connection
    except:
        print('DB Connection failed')
        
def disconnect_db(connection):
    try:
        connection.close()
        print('DB Disconnected')
    except:
        print('DB Disconnection Failed')

def create_table():
    query = 'create table IF NOT EXISTS people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, age int default(0), location varchar(32));'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print('Table Created')
        else:
            print('Table Creation Failed')
        cursor.close()
        disconnect_db(connection)
    
    except:
        print('Table Creation Error')

def create_database(connection):
    query = 'create table people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, age int default(0), location varchar(32));'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print('Table Created')
        else:
            print('Table Creation Failed')
        cursor.close()
        disconnect_db(connection)
    
    except:
        print('Table Creation Error')

create_table()
