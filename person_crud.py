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

def create_person_demo():
    query = 'insert into people(name, gender, location, age) values("shreya", true, "mysore", 20);'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print('Person Created')
        else:
            print('Person Creation Failed')
        cursor.close()
        disconnect_db(connection)
    
    except:
        print('Person Creation Error')
        
def read_person():
    name = input("Enter Person Name: ")
    age = int(input("Enter Person Age: "))
    gender = input("Enter Person Gender (m/f): ")
    location = input("Enter Person Location: ")
    if gender.lower() == 'f' : 
        gender = True
    else:
        gender = False
    return (name, gender, age, location)

def create_person():
    query = 'insert into people(name, gender, age, location) values(%s, %s, %s, %s);'
    try:
        person = read_person()
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)
        print(f"count = {count}")
        if count == 1:
            print('Person Created')
        else:
            print('Person Creation Failed')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    
    except:
        print('Person Creation Error')



def search_person():
    pass

def update_person():
    pass

def delete_person():
    pass

def list_people():
    pass

create_person()