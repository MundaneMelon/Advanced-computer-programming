import random
first_names = ['james', 'john', 'robert', 'michael', 'william', 'david', \
               'richard', 'charles', 'joseph', 'thomas', 'christopher', \
               'mary', 'patricia', 'linda', 'barbara', 'elizabeth', 'jennifer', 'maria', \
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

global total_emails_written
global total_duplicate_emails
global total_invalid_emails
total_emails_written = 0
total_duplicate_emails = 0
total_invalid_emails = 0

def main():

    global total_emails_written
    global total_duplicate_emails
    global total_invalid_emails

    for i in range(1000):
        for i in range(4):
            check = False
            while not check:
                temp_email = f"{first_names[random.randint(0, len(first_names) - 1)]}.\
{last_names[random.randint(0, len(last_names) - 1)]}{random.randint(0, 100)}\
{endings[random.randint(0, len(endings) - 1)]}"
                if temp_email in used_emails:
                    total_duplicate_emails += 1
                    check = False
                else:
                    used_emails[temp_email] = 1
                    f.write(f"{temp_email},")
                    total_emails_written += 1
                    check = True

        check = False
        while not check:
            temp_email = f"{first_names[random.randint(0, len(first_names) - 1)]}.\
{last_names[random.randint(0, len(last_names) - 1)]}{random.randint(0, 100)}@@@cooooudfs.csiou"
            if temp_email in used_emails:
                total_duplicate_emails += 1
                check = False
            else:
                used_emails[temp_email] = 1
                f.write(f"{temp_email},")
                total_invalid_emails += 1
                check = True

    print(f"Total emails written: {total_emails_written}")
    print(f"Total duplicate emails: {total_duplicate_emails}")
    print(f"Total invalid emails: {total_invalid_emails}")


if __name__ == "__main__":
    main()