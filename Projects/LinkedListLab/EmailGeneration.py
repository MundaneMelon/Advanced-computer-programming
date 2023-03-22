import random
first_names = ['james', 'john', 'robert', 'michael', 'william', 'david', \
               'richard', 'charles', 'joseph', 'thomas', 'christopher', \
               'mary', 'patricia', 'linda', 'barbara', 'elizabeth', 'jennifer', 'maria' \
               'susan', 'margaret', 'dorothy', 'lisa', 'daniel', 'paul', 'mark', \
               'donald', 'george', 'kenneth', 'steven', 'edward', 'brian', 'ronald', \
               'nancy', 'karen', 'betty', 'helen', 'sandra', 'donna', 'carol', 'ruth', \
               'sharon', 'michelle']

last_names = ['smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', \
              'davis', 'rodriguez', 'martinez', 'hernandez', 'lopez', 'wilson', 'anderson', \
              'thomas', 'taylor', 'moore', 'jackson', 'martin', 'lee', 'perez', 'thomspon', 'white', \
              'harris', 'sanchez', 'clark', 'ramirez', 'lewis', 'robinson', 'walker', 'young', \
              'allen', 'king', 'wright', 'scott', 'torres', 'nguyen', 'hill']

endings = ['@outlook.com', '@gmail.com', '@yahoo.com', '@inbox.com', '@icloud.com', '@mail.com', '@zohomail.com']
used_emails = {}
f = open('emails.txt', 'w')

def main():
    # this is the plaaan
    '''
    First, pick a random first name and assign it to a temp string,
    then pick a random last name and add it to the string, finally
    add a random email ending to this string.
    If that email isn't currently occupied, then add it to the list (use a while loop for this)

    Every 4 emails, add in a random first name, random last name, but crazy ass email ending,
    check if it's being used (which is statistically unlikely) and then proceed as usual.

    When emails are good to go, write them to the text document and then seperate them all my commas.
    No spaces or anything
    '''
    temp_email = ''

    print(f"{first_names[random.randint(0, len(first_names) - 1)]}.\
{last_names[random.randint(0, len(last_names) - 1)]}{random.randint(0, 100)}\
{endings[random.randint(0, len(endings) - 1)]}")

    for i in range(3):
        check = False
        while not check:
            temp_email = f"{first_names[random.randint(0, len(first_names) - 1)]}.\
{last_names[random.randint(0, len(last_names) - 1)]}{random.randint(0, 100)}\
{endings[random.randint(0, len(endings) - 1)]}"
            if temp_email in used_emails:
                check = False
            else:
                used_emails[temp_email] = 1
                check = True
    for i in used_emails:
        print(i)



if __name__ == "__main__":
    main()