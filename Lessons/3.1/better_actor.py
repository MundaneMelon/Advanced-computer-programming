"""
This tutorial shows the use of
a class.
"""

class BetterActor:
    ''' Define the Actor class '''
    def __init__(self, first_name, last_name, birthday, total_films \
                 , oscar_nominations=0, oscar_wins=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.total_films = total_films
        self.oscar_nominations = oscar_nominations
        self.oscar_wins = oscar_wins