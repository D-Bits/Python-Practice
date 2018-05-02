#Get grade point average

class grade:
    def __init__(self,course,gpoint,credit):
        self.course=course
        self.gpoint=gpoint
        self.credit=credit
    def getCourse(self):
        return self.course
    def getGradePoint(self):
        return self.gpoint
    def getCredits(self):
        return self.credit
    def __str__(self):
        return course + " " + str(self.gpoint) + " " + str(self.credits)

class student:
    def __init__(self,sid,name,email):
        self.sid=sid
        self.name=name
        self.email=email
        self.grades=[]

    def addGrades(self, gradepoint):
        self.grades.append(gradepoint)

    def calcGPA(self):
        self.gpa=0
        weight=0
        total=0
        if len(self.grades) != 0:
            for g in self.grades:
                weight += g.credit * g.gradepoint
                total += g.credit
            self.gpa=weight / total

    def __str__(self):
        self.calcGPA()
        return self.sid + " " + self.name + " " + self.email + " " + str(self.gpa())

def main():
    s=student("1124489", "John Doe", "jd@gmail.com")
    stop = "n"
    while stop == "n":
        course = input("Enter the course name: ")
        gp = float(input("Enter the final grade: "))
        cr = int(input("Enter the number credits: "))
        g=grade(course, gp, cr)
        s.addGrades(g)
        stop = input("Do you want to stop? Press 'n' to continue: ")
    print(s)

main()


        
