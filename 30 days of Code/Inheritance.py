

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self,firstName, lastName, idNum , scores):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
    
    def printPerson(self):
        print("Name: " + lastName + ", " + firstName)
        print("ID:", idNum)
    
    def calculate(self):
        x = len(scores)
        n = 0
        for i in range(x):
            n+=scores[i]
        
        y = int(n)//int(x)

        if 90<= y <= 100:
            return 'O'
        elif 80<= y < 90:
            return 'E'
        elif 70<= y < 80:
            return 'A'
        elif 55<= y < 70:
            return 'P'
        elif 40<= y < 55:
            return 'D'
        else:
            return 'T'

