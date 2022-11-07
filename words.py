"""

Module for Scrabble scoring

"""


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
    

def read_word_file(fileName):
    # reads in file
    """Return the parsed file"""
    try:
        with open(fileName, 'r') as txtFile:
            lines = txtFile.readlines()
    except Exception as e:
        raise(e)
    
    
    else:
        # parse the lines 
        tempData = {}
        for line in lines:
            tempscore = []

            try:
                newLine = line.strip().lower()
                newWord = f'{newLine[0]}{newLine[1]}{newLine[2]}'

                tempscore.append(points_for_letter(newLine[0]))
                tempscore.append(points_for_letter(newLine[1]))
                tempscore.append(points_for_letter(newLine[2]))
                
                # print(f'{newLine[0]}{newLine[1]}{newLine[2]}')
                # print(tempscore)

            except Exception as e:
                # raise(e)
                continue
            else:
                tempData[f'{newWord}'] = sum(tempscore)
                # tempData.append(newWord)
                # tempData.append(sum(tempscore))
        return tempData

def sort_dict_scores(data):
    # sort dictionary by scores
    sorted_dict = sorted(data.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_dict)
    
def output_to_file(data):
    with open('3_letter_words_sorted.txt', 'w') as txtFile:
        for word in data:
            value = data[word]
            txtFile.write(f'{word} -> {value}\n')