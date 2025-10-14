from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, lyst.size()  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True


def main():
    course = Course()
    print(course.grade())

    sluts = SList()

    sluts.insert(10)
    sluts.insert(11)
    sluts.insert(9)
    sluts.insert(20)
    sluts.insert(9)

    print(sluts)


    print(sluts.size())
    
    for i in sluts:
        print(sluts[i])

  
if __name__ == "__main__":
    main()
