from itertools import permutations

def parse_user_Input(userInput):
    """Returns the parsed user Input and validates that 
    the char are alphabetic"""
    userInput = userInput.replace(' ','')
    userInput = userInput.replace(',','')
    # need to validate that they are alphabetic
    return userInput


def read_valid_word_file(fileName):
    # reads in file
    """Returns the list of valid words"""
    tempData = []
    try:
        with open(fileName, 'r') as txtFile:
            lines = txtFile.readlines()
            
            for line in lines:
                newLine = line.strip().lower()
                tempData.append(newLine)
            
            return tempData
    except Exception as e:
        raise(e)

    
def iterate_permutations(letter_list):
    """Returns the posible permutations of the users 7 letters"""
    combos = []
    seven = list(permutations(letter_list,7))
    for tup in seven:
        combos.append(str(''.join(tup)))
    return combos

def check_for_valid_words(permutation_list, valid_word_list):
    """Returns all valid words that are possible from the permuations of user letters"""

    wordlist = []
    for word in valid_word_list:
        for perm in permutation_list:
            if word in perm and word not in wordlist:
                wordlist.append(word)
    return(wordlist)

def points_for_letter(letter):
    """Return the points as an integer for a given letter according to Scrabble
    letter frequency tables.
    """  
    
    # Dictionary to look up the point value for each letter. In the dictionary,
    # the key is the letter and the value is the point value
    tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
    
    return tile_score[letter]


def get_scores_dictionary(wordlist):
    """Returns a dictionary of words and their subsequent scores"""
    tempData = {}
    for word in wordlist:
        tempscore = []

        try:
            for letter in word:
                tempscore.append(points_for_letter(letter))

        except Exception as e:
            # raise(e)
            continue
    
        else:
            tempData[f'{word}'] = sum(tempscore)
        
    return tempData

def sort_dict_scores(data):
    """Returns a dictionary of words sorted by their score values"""
    # sort dictionary by scores
    sorted_dict = sorted(data.items(), key=lambda x:x[1], reverse=True)
    newDict = dict(sorted_dict[:15]) 
    return newDict



def main():
    """Main driver for your program"""
    letter_perms = iterate_permutations(parse_user_Input(input('put letters here: ')))
    valid_words = read_valid_word_file('scrabble_list.txt')
    all_playable_words = check_for_valid_words(letter_perms, valid_words)
    all_scores = get_scores_dictionary(all_playable_words)
    sorted_scores = sort_dict_scores(all_scores)
    print(sorted_scores)



if __name__ == "__main__":
    main()