print('''
                                    _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to treasure hunt game!!!")
turn = input(print("Choose where you want to turn? type right or left?")).lower()
if turn == "right":
    print("Game over")
elif turn == "left":
    door = input(print("Choose which you want to open? type A or B or C?")).lower()
    if door == "B":
        treasure_Box = input(print("Choose which treasure box you want to open? type Red or Yellow or Green?")).lower()
        if treasure_Box == "Red":
            print("You got the treasure :)")
        elif treasure_Box == "Yellow" or "Green":
            print("Game Over")
        else:
            print("Invalid entry!!!")
    elif door == "A" or "C":
        print("Game Over")
    else:
        print("Invalid entry!!!")
else:
    print("Invalid entry!!!")