
import emoji
import random

key=[':(', ':)','xD','x8','ಠ_ಠ','( •_•)','¯\_(ツ)_/¯','ʘ‿ʘ','(⊙_☉)','( ˇ෴ˇ )','( ͡° ͜ʖ ͡°)','(ง •̀_•́)ง']
existingletters=[]



def initilisation():
     random.shuffle(key);






def encriptletter(a):
    if a in existingletters:
        return key[existingletters.index(a)]
    else:
        existingletters.append(a)
        return key[len(existingletters)]



with open('forencription.txt') as f:
     content = f.read().splitlines()


for i in range(0,len(content)):
     print(content[i])
     text=content[i]
     text_list=list(text)
     for j in range(0,len(text_list)):
         encriptletter(text_list[j])


print(emoji.emojize('Python is :thumbs_up_sign:'))