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
    newList = SList()

    newList.insert(1)
    print(1)
    newList.insert(6)
    print(2)
    newList.insert(3)
    print(3)
    newList.insert(10)
    print(4)
    
    print(newList)

  
if __name__ == "__main__":
    main()
