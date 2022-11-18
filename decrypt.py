alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_alphabet = '!HR*(&}|":>?<./UT$@#[-=]`~'


def main():
    encrypt('output.txt', 'second_output.txt')


def encrypt(text_url, output_url):
    with open(text_url, 'r') as file:
        text = file.read()
    output = ""

    # The part where I actually encrypt the thing
    for i in range(len(text)):
        try:
            if new_alphabet.index(text[i]) >= 0:
                output += alphabet[new_alphabet.index(text[i])]
        except:
            output += text[i]

    print(output)
    with open(output_url, 'w') as f:
        f.write(output)
if __name__ == "__main__":
    main()