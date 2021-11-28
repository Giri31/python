def uni_char2(s):
    chars =[]
    for let in s:
        # Check if in set
        if let in chars:
            pass
        else:
            #Add it to the set
            chars.append(let)
    return chars 
print(uni_char2("ddddev"))
