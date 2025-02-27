import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Andy@2580335520",
    auth_plugin='mysql_native_password',
    
)



def initialize_server():
    f = open("load_data_instructions.txt","r")
    for line in f:
       print(line)
       mycursor = mydb.cursor()
       mycursor.execute("USE Group_Project1 " + line)


def main():
    initialize_server()

if __name__ == "__main__":
    main()