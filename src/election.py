import os
from candidate import Candidate
from voter import Voter


class Election:
    has_ended = False

    def __init__(self):
        os.system('cls')
        self.name = input('Enter The Name For Election : ')
        self.position_of_interest = input(
            'Enter Position Of Contestation : ')
        self.area_code = input('Enter Area Code : ').capitalize()
        self.candidates_with_votes = dict()
        self.voters = set()

    def addCandidate(self, c: Candidate):
        if self.has_ended == False:
            if c in self.candidates_with_votes.keys():
                print('Candidate Already Registered\n')
            else:
                self.candidates_with_votes[c] = 0
                print('Nomination Submitted\n')
        else:
            print(
                f'Election Has Ended\n{self.winner} Won The Election with {self.candidates_with_votes[self.winner]} Votes!!\n')

    # def removeCandidate(self, c: Candidate):
    #     if self.has_ended == False and self.is_open == False:
    #         if c in self.candidates_with_votes.keys():
    #             del self.candidates_with_votes[c]
    #             print('Candidate Removed!\n')
    #         else:
    #             print('Candidate Is Not Registered For The Election.\n')

    #     elif self.has_ended == False and self.is_open == True:
    #         print('Voting Has Already Started!!')

    #     else:
    #         print(
    #             f'Election Has Ended\n{self.winner} Won The Election with {self.candidates_with_votes[self.winner]} Votes!!')

    def addVote(self, c: Candidate, v):

        if v in self.voters:
            print('You Have Already Voted')
        else:
            self.candidates_with_votes[c] += 1
            self.voters.add(v.uid)
            print('Vote Casted!')

    def announceWinner(self):
        # if self.has_ended == True:
        max_votes = 0
        for candidate in self.candidates_with_votes.keys():
            if self.candidates_with_votes[candidate] > max_votes:
                self.winner = candidate
                max_votes = self.candidates_with_votes[candidate]

        os.system('cls')
        print(f'{self.winner.name} HAS WON THE ELECTION\n')
        # else:
        #     print('Voting Is Still In Process!! Cannot Announce Winner')

    def get_state(self):
        if self.has_ended:
            return 'Ended'
        else:
            return 'Open'

    def show_candidates(self):
        candidate_list = []
        for candidate in self.candidates_with_votes.keys():
            candidate_list.append((candidate.party, candidate))

        return candidate_list

    def __str__(self):
        return f'\nElection Name : {self.name}\nArea Code : {self.area_code}\nStatus : {self.get_state()}\nPosition : {self.position_of_interest}\nCandidates : {self.show_candidates()}'


if __name__ == "__main__":
    e = Election()
    c = Candidate()
    e.candidates_with_votes[c] = 0
    print(e)
