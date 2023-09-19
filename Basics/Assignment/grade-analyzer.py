# Python Coding Challenge Title: Student Grade Analyzer
# Description:
# You have been tasked with creating a grade analyzer program for your class. The program should take the score of a student and award them a specific grade. eg a score of 80 should get an A etc
# Happy Coding!
name = input('Enter your name:') 
marks = int(input('Enter your marks:'))

if (marks >= 80):
    print("Excellent"+" "+ name +" "+ "you got an A")
elif(marks >= 75):
    print("Great Job" +" "+name+" "+"you got a B+")
elif(marks >=70 ):
    print("Nice" +" "+name+ " "+"You are on the verge, you got a B")
elif(marks >= 60 ):
    print('Good work' +" "+name+ " "+'You have a clean B-')
elif(marks >=55 ):
    print('superb'+" "+name+ " "+'you have a C+')
elif(marks >=50 ):
    print(name+" "+'you have a C')
elif(marks >= 45 ):
    print("Work harder"+" " +name+ " "+"you have a C-")
elif(marks >= 40 ):
    print("I wanna see you do better" +" "+name+" "+"you have a D+")
elif(marks >= 35):
    print("Work harder"+" "+ name +" "+"you have a D")
elif(marks >= 30 ):
    print("Work harder"+" "+name+" "+"you have a D-")
else:
    print('Poor perfomance'+" "+ name +" "+ 'You have an E')



