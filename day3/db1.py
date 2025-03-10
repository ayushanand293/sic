import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root'
        , password = 'root', database='ayush_db', charset= 'utf8')
        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def create_db():
    connection = connect_db()
    query = 'create database IF NOT EXISTS ayush_db;'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)

def create_table():
    connection = connect_db()
    query = """create table IF NOT EXISTS persons_1(id int primary key auto_increment, name varchar(32) 
    not null, gender varchar(1) check(gender in ('m','M','f','F')), location varchar(32),
    dob datetime);"""
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    print('Table created')
    disconnect_db(connection)

def read_person_details():
    name = input('Enter person name: ')
    gender = input('Enter person gender: ')[0]
    location = input('Enter person location: ')
    dob = input('Enter person date of birth(yyyy-mm-dd): ')
    return (name, gender, location, dob)

def insert_row():
    person = read_person_details()
    query = 'insert into persons_1(name, gender, location, dob) values (%s, %s, %s, %s);'
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query, person)
    connection.commit()
    cursor.close()
    print('Row created')
    disconnect_db(connection)

def disconnect_db(connection):
    try:
        connection.close()
        print('DB dis-connected')
    except:
        print('Error while disconnecting DB')    
    


create_table()
insert_row()