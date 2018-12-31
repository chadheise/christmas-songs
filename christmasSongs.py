allLetterCounts = {letter:0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ'" }
for s in [ s.replace(' ','').upper() for s in ["Rudolph the Red Nosed Reindeer", "Frosty the Snowman", "I'll Be Home for Christmas", "Jingle Bell Rock", "Joy to the World", "Jolly Old St Nicholas", "Up on the Housetop", "White Christmas", "Silver Bells", "Winter Wonderland", "Let It Snow", "O Holy Night", "The First Noel", "Oh Christmas Tree", "Jingle Bells", "The Twelve Days of Christmas"] ]:
    wordLetterCounts = {letter:s.count(letter) for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ'" }
    allLetterCounts = {letter:(wordLetterCounts[letter],allLetterCounts[letter]) [ wordLetterCounts[letter] < allLetterCounts[letter] ] for letter in wordLetterCounts}                        
for letter in allLetterCounts:
    print(letter + " = " + str(allLetterCounts[letter]))