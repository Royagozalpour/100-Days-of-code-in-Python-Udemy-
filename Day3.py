print('''
Alice's Adventures in Wonderlan: 'Through the Looking Glass'


    ,--._                      _
    "'.  '.                  ,';
       )   '.              ,' /
     _/      '.          ,'   '.
   -"__        '.;  /  ,`'    ,-`
       \        /  ( ,===.  _`. )
       /__      `.__//.' \\/_.-`
          '-,._.-    \ \_/\\ ,-.
              \.-     /  \_\\/||
             _/\\    :o o :-'/;.`.
          _,";-,;|   :/"\ : // ||))
     _..."((|_//||-.._\"//  `` ;;''
    /,-----"||" ''    \`._
   //      ,'|         `-.`-..._
  ::     ,','             '.__.=
  ::     |||  _
   \\_   ""   ))     'Beware the jabberwock, my son!'
    \_"--....';
      '""---"' SSt
       ''')



print("Welcome to Treasure Island.Your mission is to find the treasure\n")
ch1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" \n').lower()
if ch1 == "left" :
    ch2 = input('You\'ve come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type"swim" to swim across.\n ').lower()
    if ch2 == "wait" :
        ch3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.Which colour do you choose?\n").lower ()
        if ch3 == "red":
           print("It's a room full of fire. Game Over.")
        elif ch3 ==  "yellow":
           print("You found the treasure! You Win!")
        elif ch3 ==  "blue":
           print("You enter a room of beasts. Game Over.")
        else:
           print("You chose a door that doesn't exist. Game Over.")
    else :
        print ("You got attacked by an angry trout. Game Over.")    

else :
    print("Fall into a hole.Game Over")