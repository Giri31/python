import string 
import random
alphabet_string = string. ascii_lowercase
alphabet_string_1 = string. ascii_uppercase
alphabet_list = list(alphabet_string) 
alphabet_list_1 = list(alphabet_string_1) 
letters_list=alphabet_list_1 + alphabet_list
numbers=['0','1','2','3','4','5','6','7','8','9']
characters=['!','@','#','$','%','^','&','*','_']
letters=int(input("Enter the number of words: "))
nums=int(input("Enter the number of words: ")) 
spl=int(input("Enter the number of words: "))
psswd=[]
for i in range(1, letters+1):
    psswd += random.choice(letters_list)
for j in range(1, nums+1):
    psswd += random.choice(numbers)
for k in range(1, spl+1):
    psswd += random.choice(characters)
    
random.shuffle(psswd)
#print(psswd)

password=''
for x in psswd:
    password += x 
print(password)
