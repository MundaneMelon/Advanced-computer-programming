import better_actor as ba

"""
This tutorial shows a program using
a class
"""

def main():
    john = ba.BetterActor("John", "Wayne", "May 26", 177, 3, 1)
    dwayne = ba.BetterActor("Dwayne", "Johnson", "July 9", 34)
    print("{} {} is a member of the " "{}.".format(john.first_name \
                                                   , john.last_name, \
                                                   john.union))
    print("{} {} is a member of the " \
          "{}.".format(dwayne.first_name, dwayne.last_name, \
                       dwayne.union))



if __name__ == "__main__":
    main()