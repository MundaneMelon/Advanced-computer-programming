alphabet = 'abcdefghijklmnopqrstuvwxyz '
new_alphabet = '!çì*(&}|":>?<./ùû$@#[-=]`~°'

def main():
    encrypt('output.txt', 'second_output.txt')


def encrypt(text_url, output_url):
    with open(text_url, 'r') as file:
        text = file.read()
    output = ""

    # The part where I actually encrypt the thing
    for i in range(len(text)):
        state1 = False
        state1 = False
        try:
            if text[i] == 'œ':
                output += text[i+1]
                i += 1
                state1 = True
        except:
            state1 = False
        if not state1:
            try:
                if new_alphabet.index(text[i]) >= 0:
                    output += alphabet[new_alphabet.index(text[i])]
                    state2 = True
            except:
                state2 = False
        if text[i] == 'æ':
            output += '\n'
        elif not state1 and not state2:
            output += text[i]




    print(output)
    with open(output_url, 'w') as f:
        f.write(output)
if __name__ == "__main__":
    main()