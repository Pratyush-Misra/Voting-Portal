import maskpass


class Voter():
    def __init__(self):
        self.uid = 0
        self.name = input('Enter Your Name : ')
        self.age = int(input('Enter Your Age : '))
        self.area_code = input('Enter Your Area Code : ').capitalize()
        self.pswd = maskpass.askpass('Set A Password : ')

    def __str__(self):
        return f'{self.name} --> {self.uid}\nArea Code : {self.area_code}'
