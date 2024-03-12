#Lab 7-3 The Dice Game
#add libraries needed
playerTwo = 'NO NAME'
playerOne = 'NO NAME'
inputNames = ("enter name")
import random

#the main function
def main():
    print
#initialize variable
sendProgram = "no"
playerOne = "NO NAME"
playerTwo = "NO NAME"

#call to inputNames
playerOne, playerTwo = inputNames(playerOne, playerTwo)
#while loop to run program again
while endProgram == 'no':

#initialize variables
p1number = 0
p2number = 0
winnerName = 'NO NAME'

#call to rollDice
winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

#call to displayInfo
displayinfo(winnerName)
endProgram = raw_input('Do you want to end program? (Enter yes or no): ')

#end of while loop

#this function gets the players names
def inputNames(playerOne, playertwo):
playerOne= raw_input('Enter player 1 name: ')
playerTwo= raw_input('Enter player 2 name: ')

return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
p1number = random.randint(1, 6)
p2number = random.randint(1, 6)
if p1number == p2number:
winnerName = "TIE"
elif p1number>p2number:
winnerName=playerOne
else:
winnerName=playerTwo
return winnerName

#this function displays the winner
def displayinfo(winnerName):
      print 'The winner is', winnerName
#calls main
main()
