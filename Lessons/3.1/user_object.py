'''
This tutorial shows how to define a class
and instantiate an object.
'''

class Actor:
    pass

print(Actor)
helen = Actor()
print(type(helen))

helen.first_name = "Helen"
helen.last_name = "Mirren"
print(helen.first_name, helen.last_name)

print(helen.first_name.upper(), helen.last_name.lower())
helen.total_films = 80
helen.notable_films = ['The Queen', 'The Madness of King George', 'Gosford Park']
print(helen)