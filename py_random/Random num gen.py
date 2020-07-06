import random

play_game = input("Enter y to start the generator")
count = 0
while(play_game == 'y' or 'Y'):
    rand_num = random.randint(1,10)
    count = count + 1
    print("The random number generated is:", rand_num, ", number of times the random number generated is:", count)
    play_game = input("Enter either y to continue or n to end the program.")
    if(play_game == 'n'):
        print("The program has ended")
        break
