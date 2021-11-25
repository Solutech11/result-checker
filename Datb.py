import mysql.connector

myDb = mysql.connector.connect(
    host='localhost',
    database ='resultchecker',
    user ='root',
    password =''
)


myCursor = myDb.cursor(dictionary =True)

# creating students table
myCursor.execute(
    """CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL references studentAdmin(student_name),
        PRIMARY KEY(id)
    );
        
    """    
)


                # admins
    # student admin
myCursor.execute(
    """CREATE TABLE IF NOT EXISTS studentAdmin(
        student_name VARCHAR(300) NOT NULL,
        student_Id VARCHAR(300) NOT NULL,
        email VARCHAR(255)
    );"""
)

    # lecturer admin
myCursor.execute(
    """CREATE TABLE IF NOT EXISTS lecturerAdmin(
        Lecturer_name VARCHAR(300) NOT NULL,
        lecturer_Id VARCHAR(300) NOT NULL,
        course1 VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        course2 VARCHAR(255),
        PRIMARY KEY(lecturer_Id)
    );"""
)

# creating courses table
myCursor.execute(
    """CREATE TABLE IF NOT EXISTS course(
        StudentName VARCHAR(300) references studentAdmin(student_name),
        CSE201 INT,
        CSE211 INT,
        CSE221 INT,
        CSE231 INT,
        CSE241 INT,
        CSE251 INT
    );"""
)


# creating result table
myCursor.execute(
    """CREATE TABLE IF NOT EXISTS result(
        Id VARCHAR(255) NOT NULL references studentAdmin(student_Id),
        student_name VARCHAR(255) references studentAdmin(student_name),
        courses VARCHAR(255) NOT NULL,
        Final_Score INT NOT NULL,
        PRIMARY KEY(Id)
    )"""
)
