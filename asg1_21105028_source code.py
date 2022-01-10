

## ASSIGNMENT -1

###Q1. Write a Python program to find average of three numbers entered by the user. ###

### input from user###

N1= float(input("Enter first number-"))
N2=float(input("Enter second number-"))
N3=float(input("Enter third number-"))

### formula ###
avg=(N1+N2+N3)/3

print("Average-",avg)
 
#<-***********************************************************************************->#

###Q2.Write a python program to compute persons income tax...###

 ###input from user###
gross_income=float(input("Enter the Gross Income to the nearest penny -"))
dependents=int(input("Enter the number of Dependents -"))

 ###formula###
Taxable_income =gross_income - 10000 -(3000*dependents)
Tax=(Taxable_income*20)/100

if Tax<0:
    print("Your income tax is 0$")
else:
         print(Tax)

#<-***********************************************************************************->#

###Q3.Write a python program to store different data type values into a list.###

   ###input from user###
SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your gender -(M,F,U)- ")
course=input("Enter the course name-")
cgpa=float(input("Enter the CGPA-"))

###list###
Student =[SID,name,gender,course,cgpa]

print(Student)

#<-***********************************************************************************->#


###Q4.Write a python program to enter marks of 5 students and display them in sorted manner###

###input from user###
M1=float(input("Enter the marks in Subject 1 = "))
M2=float(input("Enter the marks in Subject 2 = "))
M3=float(input("Enter the marks in Subject 3 = "))
M4=float(input("Enter the marks in Subject 4 = "))
M5=float(input("Enter the marks in Subject 5 = "))

### list ###
Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)

#<-***********************************************************************************->#


###Q5. a) List :color ['Red','Green','White','Black','Pink','Yellow']###

color=['Red','Green','White','Black','Pink','Yellow']
color.remove('Black')
print(color)


###Q5. b)  List :color ['Red','Green','White','Black','Pink','Yellow']###

color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=["Purple"]
print(color)

#<-***********************************************************************************->#

























