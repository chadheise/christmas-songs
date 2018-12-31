import string

songs = ["Rudolph the Red Nosed Reindeer", "Frosty the Snowman", "I'll Be Home for Christmas", "Jingle Bell Rock", \
"Joy to the World", "Jolly Old St Nicholas", "Up on the Housetop", "White Christmas", "Silver Bells" \
"Winter Wonderland", "Let It Snow", "O Holy Night", "The First Noel", "Oh Christmas Tree", "Jingle Bells", "The Twelve Days of Christmas"]
songs = [s.replace(' ','').upper() for s in songs]

allLetterCounts = {letter:0 for letter in (string.ascii_uppercase + "'") }

for s in songs:
    wordLetterCounts = {letter:0 for letter in (string.ascii_uppercase + "'") }
    for letter in s:
        wordLetterCounts[letter] += 1
    allLetterCounts = {letter:(wordLetterCounts[letter],allLetterCounts[letter]) [ wordLetterCounts[letter] < allLetterCounts[letter] ] for letter in wordLetterCounts}
            
for letter in allLetterCounts:
    print(letter + " = " + str(allLetterCounts[letter]))