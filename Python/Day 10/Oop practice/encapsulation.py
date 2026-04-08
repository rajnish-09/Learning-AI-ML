# Create Student class with private attributes _name, _roll, _marks. Provide getter and setter method for vaildation (marks cannot be empty, roll between 1 to 100, and name cant be empty)

class Student:
    def __init__(self, _name = '', _roll = '', _marks = ''):
        self._name = _name
        self._roll = _roll
        self._marks = _marks

    def get_name(self):
        return self._name
    
    def set_name(self, _name):
        if _name == '':
            print("Name cannot be empty.")
        else:
            self._name = _name

    def get_roll(self):
        return self._roll
    
    def set_roll(self, _roll):
        if _roll < 1 or _roll >100:
            print("Invalid roll number. Must be between 1 to 100")
        else:
            self._roll = _roll

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, _marks):
        if _marks == '' or _marks is None:
            print("Marks cannot be empty")
        self._marks = _marks


s1 = Student()
s1.set_name("Ramesh")
print(f'Name: {s1.get_name()}')

s1.set_roll(53)
print(f'Roll: {s1.get_roll()}')

s1.marks = 78
print(f'Marks: {s1.marks}')


