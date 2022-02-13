import os
import requests
from mysql.connector import errorcode
import mysql.connector
import calendar
from _datetime import datetime
from getpass import getpass
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Visualization():

    def __init__(self):
        pass

    def PiePlot(self):
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba, index_col='ID')
        Presenty = []
        P = 0
        A = 0
        for col in data.keys():
            P += data[col].value_counts()[0]
            A += data[col].value_counts()[1]
        Presenty.append(P)
        Presenty.append(A)
        plt.figure(figsize=(12, 8))
        plt.pie(Presenty, labels=['Present', 'Absent'], autopct='%1.1f%%', shadow=True)
        plt.title('Total present and absent student out of 2820 students')
        plt.legend()
        plt.show()
        
    def Present_Students(self):
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba, index_col='ID')
        Presenty = []
        for col in data.keys():
            Presenty.append(data[col].value_counts()[0])
        plt.figure(figsize=(12, 8))
        plt.hist(Presenty, label=['Present'], color=['g'], rwidth=0.8, histtype='bar')
        plt.title('Student Presenty using Histogram')
        plt.legend()
        plt.show()
        
    def Absent_Students(self):
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba, index_col='ID')
        Absenty = []
        for col in data.keys():
            Absenty.append(data[col].value_counts()[1])
        plt.figure(figsize=(12, 8))
        plt.hist(Absenty, label=['Absent'], color=['r'], rwidth=0.8, histtype='bar')
        plt.title('Student Absenty using Histogram')
        plt.legend()
        plt.show()

    def Presenty_Density(self):
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba, index_col='ID')
        Presenty = []
        for col in data.keys():
            Presenty.append(data[col].value_counts()[0])
        plt.figure(figsize=(12, 8))
        sns.distplot(Presenty)
        plt.title('Density of Present Student')
        plt.legend()
        plt.show()
        
    def Absenty_Density(self):
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba, index_col='ID')
        Absenty = []
        for col in data.keys():
            Absenty.append(data[col].value_counts()[1])
        plt.figure(figsize=(12, 8))
        sns.distplot(Absenty)
        plt.title('Density of Absent Student')
        plt.legend()
        plt.show()

    def ScatterPlot(self):
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba, index_col='ID')
        Presenty = []
        Absenty = []
        for col in data.keys():
            Absenty.append(data[col].value_counts()[0])
            Absenty.append(data[col].value_counts()[1])
        plt.figure(figsize=(12, 8))
        sns.scatterplot(Presenty, Absenty)
        plt.title('Scatter Plot of Students')
        plt.show()


class Utelsis():

    def _init_(self):
        pass

    def Main(self):

        os.system('cls')
        # This is the starting part of almost every programme
        print("\nWelcome to Student Attendance System...\n")
        Name = input("Enter your name: ")
        print("\nHello " + Name.capitalize())
        while True:
            print('\n\n************** Student Attendance System **************\n')
            print('\t\t\t\t\t  +-------------------+')
            print('\t\t\t\t\t  | 1. Teacher Login  |')
            print('\t\t\t\t\t  | 2. Student Login  |')
            print('\t\t\t\t\t  | 3. Exit (No Pass) |')
            print('\t\t\t\t\t  +-------------------+\n')
            Login_As = input('Login: ')
            Password = getpass('Password: ')
            if (Login_As == '1' or Login_As.capitalize() == 'Teacher') and Password == 'Teacher@123':
                return 'Teacher', Name
            elif (Login_As == '2' or Login_As.capitalize() == 'Student') and Password == 'Student@123':
                return 'Student', Name
            elif (Login_As == '3' or Login_As.capitalize() == 'Exit'):
                return 'EXIT', Name
            else:
                print('\nInvalid Login...')
                continue

    def connect(self, user, database):
        config = {
            'user': user,
            'database': database,
            'raise_on_warnings': True
            }
        mydba = mysql.connector.connect(**config)
        mycursor = mydba.cursor()
        return mydba, mycursor

    def Record(self, msg):
        global Name 
        with open("record.txt", "a") as f:
            f.write(f"{Name.capitalize()}: {msg} :{datetime.now()}\n")

    def FindDay(self, date):
        born = datetime.strptime(date, '%Y-%m-%d').weekday()
        return (calendar.day_name[born])
    
    
class Staffs():

    def _init_(self):
        pass

    def Take_Attendance(self):
        os.system('cls')
        print('Attendance is successfully taken, Thank You...!')
        input()

    def Options(self):
        os.system('cls')
        print('1. Take Attendance')
        print('2. View Attendance')
        print('3. Visualization')
        print('4. Back')
        Choice_Staff = input('\nEnter your Choice: ') 
        return Choice_Staff

    def View_Attendance(self):
        os.system('cls')
        query = "Select * from attendances limit 10"
        print('10 Days Attendance Data...\n')
        df = pd.read_sql(query, con = mydba)
        print(df)
        input()
    
    def Visualization(self):
        os.system('cls')
        query = "Select * from attendances"
        data = pd.read_sql(query, con = mydba)
        print('1. Total Present and Absent using pie chart')
        print('2. Student Presenty using Histogram')
        print('3. Student Absenty using Histogram')
        print('4. Density of Present Student')
        print('5. Density of Absent Student')
        print('6. Back')
        Visual = input('\nEnter your choice: ')
        return Visual, data

class Students():
    
    def _init_(self):
        pass

    def Options(self):
        os.system('cls')
        print('1. View Attendance')
        print('2. Visualization')
        print('3. Back')
        Choice_Student = input('\nEnter your Choice: ')
        return Choice_Student

if __name__ == '__main__':
    
    Tools = Utelsis()
    Start, Name = Tools.Main()
    Tools.Record('Login succesfully')
    Staff = Staffs()
    Student = Students()
    Visualize = Visualization()
    os.system('cls')

    while True:
        try:
            mydba, mycursor = Tools.connect('root', 'attendance_system')
            if Start == 'Teacher':
                Choice_Staff = Staff.Options()
                if Choice_Staff == '1' or Choice_Staff.lower() == 'take attendance':
                    Staff.Take_Attendance()
                elif Choice_Staff == '2' or Choice_Staff.lower() == 'view attendance':
                    Staff.View_Attendance()
                elif Choice_Staff == '3' or Choice_Staff.lower() == 'visualization':
                    Visual, data = Staff.Visualization()
                    if Visual == '1':
                        Visualize.PiePlot()
                    elif Visual == '2':
                        Visualize.Present_Students()
                    elif Visual == '3':
                        Visualize.Absent_Students()
                    elif Visual == '4':
                        Visualize.Presenty_Density()
                    elif Visual == '5':
                        Visualize.Absenty_Density()
                    elif Visual == '6' or Visual.lower() == 'back':
                        Start, Name = Tools.Main()
                elif Choice_Staff == '4' or Choice_Staff.lower() == 'back':
                    Start, Name = Tools.Main()

            elif Start == 'Student':
                Choice_Student = Student.Options()
                if Choice_Student == '1' or Choice_Student.lower() == 'view attendance':
                    Staff.View_Attendance()
                elif Choice_Student == '2' or Choice_Student.lower() == 'visualization':
                    Visual, data = Staff.Visualization()
                    if Visual == '1':
                        Visualize.PiePlot()
                    elif Visual == '2':
                        Visualize.Present_Students()
                    elif Visual == '3':
                        Visualize.Absent_Students()
                    elif Visual == '4':
                        Visualize.Presenty_Density()
                    elif Visual == '5':
                        Visualize.Absenty_Density()
                    elif Visual == '6' or Visual.lower() == 'back':
                        Start, Name = Tools.Main()
                elif Choice_Student == '3' or Choice_Student.lower() == 'back':
                    Start, Name = Tools.Main()

            elif Start == 'EXIT':
                print('\nThanks For Visiting Us...')
                exit()
                
            else:
                print('\nSomething Wents Wrong...')
                input()

        except Exception as E:
            print(f'\nError Occured: {E}')
            input()

        finally:
            mycursor.close()
            mydba.close()