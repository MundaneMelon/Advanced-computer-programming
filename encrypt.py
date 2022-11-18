alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_alphabet = '!HR*(&}|":>?<./UT$@#[-=]`~'


def main():
    encrypt('30 Big day.txt', 'output.txt')


def encrypt(text_url, output_url):
    with open(text_url, 'r') as file:
        text = file.read()
    text = text.lower()
    output = ""

    # The part where I actually encrypt the thing
    for i in range(len(text)):
        print(text[i])
        try:
            if alphabet.index(text[i]) >= 0:
                output += new_alphabet[alphabet.index(text[i])]
        except:
            output += text[i]

    print(output)
    with open(output_url, 'w') as f:
        f.write(output)
if __name__ == "__main__":
    main()