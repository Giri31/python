choice=input("choose left or right:")
if(choice=="left"):
  print("swim or wait for boat:")
  choice1=input()
  if(choice1=="wait"):
    print("which door red or blue or yellow:")
    choice2=input()
    if(choice2=="yellow"):
      print("Hurray ! you won")
    else:
      print("gameover")  
  else:
      print("gameover") 
else:
  print("gameover")         