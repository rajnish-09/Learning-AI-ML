# Create Student class with private attributes _name, _roll, _marks. Provide getter and setter method for vaildation (marks cannot be empty, roll between 1 to 100, and name cant be empty)

class Student:
    # def __init__(self, _name, _roll, _marks):
    #     self._name = _name
    #     self._roll = _roll
    #     self._marks = _marks

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name