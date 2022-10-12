class Student:
    
    def __init__(self, first, last, id, gpa):
        self.first = first
        self.last = last
        self.id = id
        self.gpa = gpa

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Student('{}', '{}', {})".format(self.first, self.last, self.id, self.gpa)