
import emoji
import random

key1 = ['( . Y . )', '눈_눈','(◍•﹏•)','ಠ▃ಠ','ಠ_ಠ','( •_•)','¯\_(ツ)_/¯','ʘ‿ʘ','(⊙_☉)','( ˇ෴ˇ )','( ͡° ͜ʖ ͡°)','(ง •̀_•́)ง','(⌐■_■)']
key2 = ['•ᴗ•', 'ಥ_ಥ','(　＾∇＾)',' [¬º-°]¬', '|_・)','(~‾▿‾)~','(ᗒᗣᗕ)՞', '◔_◔', '(ᴗ˳ᴗ)','(◣_◢)', '(/•-•)/','( ͡° ͜ʖ ͡°)', 't(-.-t)' ]
key = []
existingletters = []
content = []
outputline = ''
outputlist = []

def encriptletter(a):
    if a in existingletters:
        return key[existingletters.index(a)]
    else:
        existingletters.append(a)
        if len(existingletters) is None:
            i = 0
        else:
            i = len(existingletters)
        return key[i]  # god knows why here exist out of bound error

key= key1 + key2
random.shuffle(key)
existingletters=[]
with open('forencription.txt') as f:
     content = f.read().splitlines()


for i in range(0,len(content)):
    text = content[i]
    text_list = list(text)
    for j in range(0, len(text_list)):
        output = encriptletter(text_list[j])
        outputline = outputline+output
    outputlist.append(outputline)


#f = open('outputfile.txt', 'w')

for i in range(0,len(outputlist)):
    print(outputlist[i])


