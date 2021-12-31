import mysql.connector
from getpass import getpass

class Visualization():
    def __init__(self):
        pass

    



class Utelsis():
    def __init__(self):
        pass
    
    def connect(self, user, password, host, database):
        config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database,
            'raise_on_warnings': True
            }
        mydba = mysql.connector.connect(**config)
        mycursor = mydba.cursor()
        return mydba, mycursor

    def Record(self):
        pass
    

class Staff():
    def __init__(self):
        pass

    def Take_Attendance(self):
        pass

    def View_Attendance(self):
        pass


class Student():
    def __init__(self):
        pass

    def View_Attendance(self):
        pass

if __name__ == '__main__':
    
    print('\n\n*************************************** Student Attendance System ***************************************\n')
    print('\t\t\t\t\t  +-------------------+')
    print('\t\t\t\t\t  | 1. Teacher Login  |')
    print('\t\t\t\t\t  | 2. Student Login  |')
    print('\t\t\t\t\t  +-------------------+\n')
    Login_As = input('Login: ')
    Password = getpass()
    try:
        if Login_As in ['1', 'Teacher Login']:
            print('Login as Teacher')
        elif Login_As in ['2', 'Student Login']:
            print('Login as Student')
        else:
            print('Invalid Input, Please Try Again...')
    except Exception as Error:
        print('Something wents wrong...')
        exit()

