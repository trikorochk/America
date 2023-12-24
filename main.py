import random 
letters_for_password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True: 
    lenn_password= int(input("lenn password: "))
    if lenn_password > 5:
        print('you made a password')
        done_password = ''
        for i in range(lenn_password):
            done_password+=random.choice(letters_for_password)
        break
    else:
        print('you must make passwor with more than 6 simbols')    
print(done_password)
        