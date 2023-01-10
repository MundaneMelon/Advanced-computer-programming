from superhero import *

def main():
    hero = Superhero("Jessica Jones", 29, "private investigator")
    print(hero.name)
    print(hero.occupation)

    print()
    hero2 = Superhero("Wonder Woman", 27, "intelligence officer")
    hero2.say_hello()

if __name__ == "__main__":
    main()