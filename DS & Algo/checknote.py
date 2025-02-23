'''
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question disguised as a random note.

Your task is to write a function that, given a list of words and a note, finds and returns the word in the list that is scrambled inside the note, if any exists. If none exist, it returns the result "-" as a string. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
note1 = "ctay"
find(words, note1) => "cat"   (the letters do not have to be in order)

note2 = "bcanihjsrrrferet"
find(words, note2) => "cat"   (the letters do not have to be together)

note3 = "tbaykkjlga"
find(words, note3) => "-"     (the letters cannot be reused)

note4 = "bbbblkkjbaby"
find(words, note4) => "baby"

note5 = "dad"
find(words, note5) => "-"

note6 = "breadmaking"
find(words, note6) => "bird"

note7 = "dadaa"
find(words, note7) => "dada"

All Test Cases:
find(words, note1) -> "cat"
find(words, note2) -> "cat"
find(words, note3) -> "-"
find(words, note4) -> "baby"
find(words, note5) -> "-"
find(words, note6) -> "bird"
find(words, note7) -> "dada"

Complexity analysis variables:

W = number of words in `words`
S = maximal length of each word or of the note
'''
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
note1 = "ctay"
note2 = "bcanihjsrrrferet"
note3 = "tbaykkjlga"
note4 = "bbbblkkjbaby"
note5 = "dad"
note6 = "breadmaking"
note7 = "dadaa"

notes = [note1,note2, note3, note4, note5, note6, note7]


def findHiddenWord(words, n):
    words_len = len(words)
    if not words_len:
        return "-"

    for word in words:
        words_map = generateCharMap(word)
        isExist = checkHiddenWord(words_map, n)
        # print(isExist, word)
        if isExist:
            return word
    return "-"



def generateCharMap(word):
    ret = {}
    for c in word:
        ret[c] = 1 + ret.get(c, 0)
    return ret


def checkHiddenWord(targetWordMap, sourceString):
    # ctay
    for c in sourceString:
        isChar = targetWordMap.get(c)
        if isChar:
            targetWordMap[c] -= 1
            if targetWordMap[c] == 0:
                del targetWordMap[c]

    keysList = list(targetWordMap.keys())
    # print(keysList)
    return True if len(keysList) == 0 else False



findHiddenWord(words, note1)

for note in notes:
    print("Result: ",findHiddenWord(words, note))
