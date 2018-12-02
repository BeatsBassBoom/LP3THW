import ex45GameFile
import sys
sys.path.append('D:\Dropbox\Code\LP3THW')


'''
1. Make a different game from the one I made.
2. Use more than one file, and use import to use them. Make sure you know what that is.
3. Use one class per room and give the classes names that fit their purpose (like GoldRoom, KoiPondRoom).
4. Your runner will need to know about these rooms, so make a class that runs them and knows
about them. There’s plenty of ways to do this, but consider having each room return what room
is next or setting a variable of what room is next.
'''


print(ex45GameFile.roll_two_dice())

play_again = input("Would you like to roll again? (Y)es or (N)o? ")
