#Noelle Adkin
#CPT 051
#noelle_grades.py
#12/1/2020

grades = [88, 90, 61, 55, 67, 100, 0, 71]
letter_grades = []

#leter_grades('B' , 'A', 'D' , 'F', 'D', 'A', 'F', 'C')
#90 > A
#80 > B
#70 > C
#60 > D
#60 < F

my_grade = 80
#my_lettergrade = 'Q'


print(my_grade)

     
print(my_lettergrade)
#letter_grades.append('Z')

for i in range(len(grades)):
    #loop
    my_grade = grades.pop()
    #my_grade =
    print(my_grade)

    if(my_grade >= 90):
        print("A!")
        letter_grades.append('A')
    elif(my_grade >= 80):
        print("B!")
        letter_grades.append('B')
    elif(my_grade >= 70):
        print("C")
        letter_grades.append('C')
    elif(my_grade < 70):
         print("lower than C")
         letter_grades.append('F')
   # letter_grades.append(my_lettergrade)
         
#letter_grades.append('Z')
print(letter_grades)


