import maskpass


class Candidate():
    def __init__(self):
        self.uid = 0
        self.name = input('Enter Your Name : ')
        self.age = int(input('Enter Your Age : '))
        self.area_code = input('Enter Your Area Code : ').capitalize()
        self.party = input('Enter Party Name : ').capitalize()
        self.pswd = maskpass.askpass('Set A Password : ')
        self.registered_elections = []

    def __str__(self):
        return f'\nParty : {self.party}\nName : {self.name}\nUID : {self.uid}'
