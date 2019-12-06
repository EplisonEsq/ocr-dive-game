import random
import time
import sys
import sqlite3, os

i = 0
Player1Points = 0
Player2Points = 0
Player1Tiebreaker = 0
Player2Tiebreaker = 0
Winner_Points = 0

##to log in use 1 then 2 with the password 1

logged_in1 = False
logged_in2 = False
while logged_in1 == False:
    username = input('Enter Your Username - ')
    password = input('Enter Your Password -  ')
    if username == 'Username1' or username == 'Username2' or username == 'Username3' or username == 'Username4' or username == 'Username5' or username == '1' or username == '2':
        if password == 'password' or password == '1':
            print('Welcome, ',username,'. ')
            logged_in1 = True
            user1 = username
        else:
            print('Wrong pass. Try again.')
    else:
        print('Wrong username. Try again.')

while logged_in2 == False:
    username = input('Enter Your Username - ')
    password = input('Enter Your Password - ')
    if username == 'Username1' or username == 'Username2' or username == 'Username3' or username == 'Username4' or username == 'Username5' or username == '1' or username == '2':
        if password == 'password' or password == '1':
            print('Welcome, ',username,'.')
            logged_in2 = True
            user2 = username
        else:
            print('Wrong pass. Try again.')
    else:
        print('Wrong pass. Try again.')

### Makes the dice roll for the player and works out the total for that roll
def roll():
    points = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dietotal = die1 + die2
    points = points + dietotal
    if dietotal % 2 == 0:
        points = points + 10
    else:
        points = points - 5
    if die1 == die2:
        die3 = random.randint(1,6)
        points = points +die3
    return(points)
### This rolls the dice 5 times for the players, and then adds up the total. (next section of code)
for i in range(1,5):
    Player1Points += roll()
    print('After this round,',user1, 'you now have: ',Player1Points,' Points')
    time.sleep(1)
    Player2Points += roll()
    print('After this round, ',user2, 'you now have: ',Player2Points,' Points')
    time.sleep(1)

if Player1Points == Player2Points:
    while Player1Tiebreaker == Player2Tiebreaker:
        Player1Tiebreaker = random.randint(1,6)
        Player2Tiebreaker = random.randint(1,6)
    if Player1Tiebreaker > Player2Tiebreaker:
        Player2Points = 0
    elif Player2Tiebreaker > Player1Tiebreaker:
        Player1Points = 0
# This checks which score is bigger, adds to leaderboard
if Player1Points > Player2Points:
    Winner_Points = Player1Points
    winner_User = user1
    winner = (Winner_Points, user1)
elif Player2Points > Player1Points:
    Winner_Points = Player2Points
    winner = (Winner_Points, user2)
    winner_User = user2
print('Nice one,', winner_User,' you won with ',Winner_Points,' Points')
#export code, broken currently so its commented out
#winner = (Winner_Points,winner_User)
#f = open('Winner.txt', 'a')
#f.write(''.join(winner))
#f.close()
###### CODE TO LOAD, UPDATE AND SORT LEADERBOARD ######
### This loads the leaderboard into an array, then compares the scores just gotton and replaces it ###
### Commentaadet out dont know how to fix
#f = open('Leaderboard.txt', 'w')
#f = [line.replace('\n','') for line in f.readlines()]
#f.close()
#for idx, item in enumerate(leaderboard):
#    if item.split(', ')[1] == winner[1] and int(item.split(', ')[0]) < int(winner[0]):
#            leaderboard[idx] = '{}, {}'.format(winner[0], winner[1])
#    else:
#        pass 
#### This sorts the leaderboard in reverse, and then rewrites it ###
#leaderboard.sort(reverse=True)
#with open('Leaderboard.txt', 'w') as f:
#    for item in leaderboard:
#        f.write("%s\n" % item)
### Creating the data base if there isnt one alreadry
    # makes c var the cursor
Leaderboard = sqlite3.connect("Leaderboard.db")
c = Leaderboard.cursor()
## making the db if there isn't one whic there is btw.
if not os.path.isfile("Leaderboard.db"):
    c.execute("""CREATE TABLE leadB
    (player_name text,
    player_score text,
    players_place) """)
    c.execute("""INSERT INTO leadB
    VALUES("Willam", "50", "?")""",(wills_place))
    c.execute("""INSERT INTO leadB
    VALUES('Daddy_David', '40', ?)""",(daddy_david_place))
    c.execute("""INSERT INTO leadB
    VALUES("Jack", "30", ?)""",(Jack_place))
    c.execute("""INSERT INTO leadB
    VALUES("Ewan", "20", ?)""",(Ewan_place))
    leaderboard.commit()
##Declaring the var
Player1place = 0
Player2place = 0
wills_place = 0
daddy_david_place = 0
Jack_place = 0
Ewan_place = 0
###Saving the players into the data base
if winner_User == user1:
    if Player1Points > 50:
        Player1place == 1
        wills_place == 2
        daddy_david_place == 3
        Jack_place == 4
        Ewan_place == 5
    elif Player1Points > 40 and Player1Points <= 49:
        Player1place == 2
        wills_place == 1
        daddy_david_place = 3
        Jack_place = 4
        Ewan_place = 5
    elif Player1Points > 30 and Player1Points <=  40:
        Player1place == 3
        wills_place == 1
        daddy_david_place = 2
        Jack_place = 4
        Ewan_place = 5
    elif Player1Points > 20 and Player1Points <=  30:
        Player1place == 4
        wills_place == 1
        daddy_david_place = 2
        Jack_place = 3
        Ewan_place = 5
    elif Player1Points > 10:
        Player1place == 5
        wills_place == 1
        daddy_david_place = 2
        Jack_place = 3
        Ewan_place = 4
else:
    if Player2Points > 50:
        Player2place == 1
        wills_place == 2
        daddy_david_place = 3
        Jack_place = 4
        Ewan_place = 5
    elif Player2Points > 40 and Player2Points <= 50:
        Player2place == 2
        wills_place == 1
        daddy_david_place = 3
        Jack_place = 4
        Ewan_place = 5
    elif Player2Points > 30 and Player2Points <= 40:
        Player2place == 3
        wills_place == 1
        daddy_david_place = 2
        Jack_place = 4
        Ewan_place = 5
    elif Player2Points > 20 and Player2Points <= 30:
        Player2place == 4
        wills_place == 1
        daddy_david_place = 2
        Jack_place = 3
        Ewan_place = 5
    elif Player2Points > 10:
        Player2place == 5
        wills_place == 1
        daddy_david_place = 2
        Jack_place = 3
        Ewan_place = 4
        c.execute("""UPDATE leaderboard
        SET player's_place = 1
        WHERE""")
