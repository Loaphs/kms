''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number = 0, name = "", credit = 0.0, grade = 0.0):
        if not isinstance(number, int) or number < 0:
            raise ValueError("Input negative or not an integer.")
        else:
            self._number = number
        if not isinstance(name, str):
            raise ValueError("Input not a string.")
        else:
            self._name = name
        if not isinstance(credit, float) or credit < 0:
            raise ValueError("Input negative or not a float.")
        else:
            self._credit = credit
        if not isinstance(grade, float) or grade < 0.0 or grade > 4.0:
            raise ValueError("Input negative, above 4.0, or not a float.")
        else:
            self._grade = grade

    def number(self):
        return self._number

    def name(self):
        return self._name

    def credit_hr(self):
        return self._credit

    def grade(self):
        return self._grade

    def __str__(self):
        return f"cs{self._number} {self._name} Grade: {self._grade} Credit Hours: {self._credit}"

  
    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb
      
    def __lt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() < cnumb
    
    def __le__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() <= cnumb
