import os
from election import Election
from login import Login
import maskpass


class ElectionCommission():

    default_pass = "1234"

    def __init__(self):
        self.all_voters = dict()
        self.all_candidates = dict()
        self.all_elections = dict()
        self.all_open_elections = dict()

    def login(self, user: Login):
        if user.u_id in self.all_voters.keys():
            return self.all_voters[user.u_id]
        elif user.u_id in self.all_candidates.keys():
            return self.all_candidates[user.u_id]
        else:
            print('User Not Registered\n')
            return None

    def authenticate(self):
        os.system('cls')
        pin = maskpass.askpass('Please Enter The Pin To Access EC Portal : ')
        if pin == self.default_pass:
            return True
        else:
            print('\nInvalid Pin !!\n')
            print('[1] : Try Again\n')
            print('[2] : Go Back\n')
            res = -1
            while res not in [1, 2]:
                res = int(input('Select A Valid Option : '))
            if res == 1:
                return self.authenticate()
            else:
                return False

    def show_all_voters(self):
        os.system('cls')
        for voter in self.all_voters.values():
            print(voter)

    def show_all_candidates(self):
        os.system('cls')
        for candidate in self.all_candidates.values():
            print(candidate)

    def show_all_elections(self):
        os.system('cls')
        if self.all_elections:
            for area in self.all_elections.keys():
                print(f'\n\nArea Code : {area}')
                for election in self.all_elections[area]:
                    print(
                        f'\n[{self.all_elections[area].index(election) + 1}]  {election}')
        else:
            print('No Elections Found!! \n')

    # def show_all_open_elections(self):
    #     os.system('cls')

    def filter_elections_area_code(self, area):
        if area in self.all_open_elections.keys():
            for election in self.all_open_elections[area]:
                print(
                    f'{self.all_open_elections[area].index(election) + 1} --> {election}')

        else:
            print('There Are No Elections In Your Area!!\n')

    def create_election(self):
        e = Election()
        os.system('cls')
        if e.area_code not in self.all_elections.keys():
            self.all_elections[e.area_code] = []
        if e.area_code not in self.all_open_elections.keys():
            self.all_open_elections[e.area_code] = []
        if e not in self.all_open_elections[e.area_code]:
            self.all_open_elections[e.area_code].append(e)
        if e not in self.all_elections[e.area_code]:
            self.all_elections[e.area_code].append(e)
            print('Election Created\n')
