import random
caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
smalls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
special_char = ["!","@","#","$","%","^","&","*"]
nums = [1,2,3,4,5,6,7,8,9,0]

n = int(input("Enter the length of the password, you require?"))
rand_sel = [caps, smalls, special_char, nums]
passW = ""


for char in range(n):
    i = random.choice(rand_sel)
    j = random.choice(i)
    passW = passW + str(j)
print(passW)