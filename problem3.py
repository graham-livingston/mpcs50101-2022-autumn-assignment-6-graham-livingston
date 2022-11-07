
def clean_input(userInput):
    lowercase = userInput.lower()
    tempData = ''
    for letter in lowercase:
        if letter == ' ':
            letter = 'blank'

        template = ":scrabble-{}:"
        tempData += template.format(letter)
    
    return tempData
# :scrabble-e:

print(clean_input(input('Please input your text for scrabble emoji conversion')))