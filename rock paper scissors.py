import random
random_num=random.randint(0,2)
print("Enter 0 for rock , 1 for paper ,2 for scissors")
choice=int(input())
print("Computer choice was:",random_num)
if(random_num==choice):
    print("Draw")
elif(choice>random_num and choice!=2):
    print("You lose")
elif(choice<random_num ):
    print("You Win")
elif(choice==0 and random_num==2):
    print("You Win")
elif(choice==2 and random_num==0):
    print("You lose")
else:
    print("Invalid input")
