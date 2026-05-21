# game.py
print("Welcome to the Hidden Waterfall Adventure!")
print("You are standing at a fork in the forest trail.")
print("To your left, you hear the faint sound of rushing water.")
print("To your right, the path leads into a dense, dark thicket.")

choice = input("Do you go 'left' or 'right'? (left/right): ")

if choice.lower() == 'left':
    print("You step carefully over the damp ferns.")
    print("The trees suddenly part to reveal a magnificent, multi-tiered waterfall cascading into a crystal-clear pool.")
    print("You sit on a smooth rock, enjoying the mist. You win!")
elif choice.lower() == 'right':
    print("You head right and quickly lose your way in the thicket. You are lost.")
else:
    print("You stand paralyzed by indecision until night falls. Game over.")
