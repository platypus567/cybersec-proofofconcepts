
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Enter the encrypted message for brute force attack: \n")

for letter in range(len(letters)):
    solved = ""
    for key in message:
        if key in letters:
            num = letters.find(key)
            num = num - letter
            if num < 0:
                num = num + len(letters)
            solved = solved + letters[num]
        else:
            solved = solved + key

    print('Key #%s: %s' % (letter, solved))


