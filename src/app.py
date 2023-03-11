import os
import random
from election_commission import ElectionCommission
from election import Election
from voter import Voter
from candidate import Candidate
from login import Login
from signup import SignUp


class VotingPortal():

    admin = ElectionCommission()

    def go_back_exit_menu(self):
        print('[1] : Go Back\n')
        print('[2] : Exit\n')

        res = -1
        while res not in [1, 2]:
            res = int(input('Select A Valid Option : '))

        return res

    def show_signup_menu(self):
        os.system('cls')
        print('Select Your Role\n')
        print('[1] : Voter\n')
        print('[2] : Candidate\n')
        print('[3] : Go Back\n')

        res = -1
        while res not in range(1, 4):
            res = int(input('Select A Valid Option : \n'))

        os.system('cls')
        if res == 1:
            v = Voter()
            if v.age > 18:
                v.uid = random.randint(10000, 100000)
                # print(len(self.admin.all_voters))
                self.admin.all_voters[v.uid] = v
                print(f'\nVoter Registered!! Your UID : {v.uid}')
                # print(len(self.admin.all_voters))
            else:
                del v
                print('\nNot Eligible To Vote!!\n')

            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_main_menu()
            else:
                quit()

        elif res == 2:
            c = Candidate()
            if c.age > 18:
                c.uid = random.randint(1000, 10000)
                # print(self.admin.all_candidates)
                self.admin.all_candidates[c.uid] = c
                print(f'\nCandidate Registered!! Your UID : {c.uid}\n')
                # print(self.admin.all_candidates)
            else:
                del c
                print('\nNot Eligible To Become A Candidate!!\n')

            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_main_menu()
            else:
                quit()

        else:
            self.show_main_menu()

    def show_ec_main_menu(self):
        os.system('cls')
        print('[1] : Create Election\n')
        print('[2] : Show All Elections\n')
        print('[3] : Announce Winners\n')
        print('[4] : Show All Voters\n')
        print('[5] : Show All Candidates\n')
        print('[6] : Exit\n')
        res = -1
        while res not in range(1, 7):
            res = int(input('Select A Valid Option : '))

        if res == 1:
            self.admin.create_election()
            print('[1] : Create Another Election\n')
            print('[2] : Go Back\n')
            print('[3] : Logout\n')

            res = -1
            while res not in [1, 2, 3]:
                res = int(input('Please Select A Valid Option : '))
            if res == 1:
                self.admin.create_election()
            elif res == 2:
                self.show_ec_main_menu()
            else:
                self.show_main_menu()
        elif res == 2:
            self.admin.show_all_elections()
            print('\n')
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_ec_main_menu()
            else:
                self.show_main_menu()
        elif res == 3:
            self.admin.show_all_elections()
            area = input('\nInput Area Code : ').capitalize()
            self.admin.filter_elections_area_code(area)
            idx = int(input('\nChoose Election : '))
            election = self.admin.all_elections[area][idx - 1]
            election.announceWinner()
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_ec_main_menu()
            else:
                quit()

        elif res == 4:
            self.admin.show_all_voters()
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_ec_main_menu()
            else:
                quit()
        elif res == 5:
            self.admin.show_all_candidates()
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_ec_main_menu()
            else:
                quit()
        else:
            self.show_main_menu()

    def voter_election_options(self, voter: Voter, election: Election):
        os.system('cls')
        print('[1] : Caste Vote\n')
        print('[2] : Go Back\n')
        print('[3] : Exit\n')

        res = -1
        while res not in [1, 2, 3]:
            res = int(input('Select A Valid Option : '))

        if res == 1:
            os.system('cls')
            loc = election.show_candidates()
            print('List Of Candidates :-\n')
            for (party, candidate) in loc:
                print(f'Party : {party} - Candidate : {candidate.name}\n')

            idx = int(input('Choose Candidate : '))
            election.addVote(loc[idx-1][1], voter)
            print(election.candidates_with_votes)
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_voter_menu(voter)
            else:
                quit()

        elif res == 2:
            self.show_voter_menu()
        else:
            self.show_main_menu()

    def show_voter_menu(self, voter: Voter):
        os.system('cls')
        print(f'\nWelcome {voter.name}\n')
        print('[1] : Show All Elections\n')
        print('[2] : Logout\n')

        res = -1
        while res not in [1, 2]:
            res = int(input('Select A Valid Choice : '))

        if res == 1:
            self.admin.filter_elections_area_code(voter.area_code)
            idx = int(input('\nChoose Election By Number : '))
            election = self.admin.all_elections[voter.area_code][idx - 1]
            self.voter_election_options(voter, election)

            # opt = self.go_back_exit_menu()
            # if opt == 1:
            #     self.show_voter_menu()
            # else:
            #     self.show_main_menu()
        else:
            self.show_main_menu()

    def candidate_election_options_menu(self, candidate: Candidate, election: Election):
        os.system('cls')
        print('[1] : Submit Nomination\n')
        print('[2] : Caste Vote\n')
        print('[3] : Exit\n')

        res = -1
        while res not in [1, 2, 3]:
            res = int(input('Select A Valid Option : '))

        if res == 1:
            election.addCandidate(candidate)
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_main_menu()
            else:
                quit()
        elif res == 2:
            os.system('cls')
            loc = election.show_candidates()
            print('List Of Candidates :-\n')
            for (party, candidate) in loc:
                print(f'Party : {party} - Candidate : {candidate.name}\n')

            idx = int(input('Choose Candidate : '))
            election.addVote(loc[idx-1][1], candidate)
            print(election.candidates_with_votes)
            opt = self.go_back_exit_menu()
            if opt == 1:
                self.show_candidate_menu(candidate)
            else:
                quit()

        else:
            self.show_candidate_menu()

    def candidate_election_menu(self, candidate: Candidate):
        area = input('\n\nInput Area Code : ').capitalize()
        self.admin.filter_elections_area_code(area)
        idx = int(input('\n Choose Election By Number : '))
        election = self.admin.all_elections[area][idx - 1]
        self.candidate_election_options_menu(candidate, election)

    def show_candidate_menu(self, candidate: Candidate):
        os.system('cls')
        print(f'Welcome {candidate.name}\n\n')
        print('[1] : Show Open Elections\n')

        res = -1
        while res not in [1, 2, 3]:
            res = int(input('Select A Valid Option : '))

        if res == 1:
            self.admin.show_all_elections()
            print('\n\n[1] : Select An Election\n')
            print('[2] : Go Back\n')
            print('[3] : Logout\n')

            res = -1
            while res not in range(1, 4):
                res = int(input('Select A Valid Option : '))
            if res == 1:
                self.candidate_election_menu(candidate)
            elif res == 2:
                self.show_candidate_menu()
            else:
                self.show_main_menu()

    def show_main_menu(self):
        os.system('cls')
        print('[1] : Login\n')
        print('[2] : SignUp\n')
        print('[3] : Election Commission Portal\n')
        print('[4] : Exit\n')

        res = -1
        while res not in range(1, 5):
            res = int(input('Select A Valid Option : '))
        if res == 1:
            user = Login()
            res_user = self.admin.login(user)
            if type(res_user) == Voter:
                self.show_voter_menu(res_user)
            elif type(res_user) == Candidate:
                self.show_candidate_menu(res_user)
            else:
                opt = self.go_back_exit_menu()
                if opt == 1:
                    self.show_main_menu()
                else:
                    quit()
        elif res == 2:
            self.show_signup_menu()
        elif res == 3:
            if self.admin.authenticate():
                self.show_ec_main_menu()
            else:
                self.show_main_menu()
        else:
            quit()

    def show_welcome_screen(self):
        os.system('cls')
        print('\n\t\t\t\t\tWelcome To The E-Voting System\n')
        res = input(
            'Do You Want To Continue To The Portal (Y/N) : ').capitalize()
        if res == 'Y':
            self.show_main_menu()
        else:
            quit()


if __name__ == "__main__":
    vp = VotingPortal()
    vp.show_welcome_screen()
