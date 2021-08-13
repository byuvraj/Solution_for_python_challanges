import re
for i in range(int(input())):
    s=input()
    l = re.split('-',s)
    s=''.join(l)
    acu = 0
    
    if len(s)!=16:
        print('Invalid')
        break
    elif s[0]=='4' or s[0]=='5'or s[0]=='6':
        if len(l[0])!=16:
            for j in l:
                if len(j) != 4:
                    print('Invalid')
                    check=False
                    break
                else:
                    check= True
        else:
            check = True
        if check:
            x = re.findall("[0-9]", s)
            if len(x)==16:
                for i in range(0,len(s)-1):
                    if int(s[i])+1==int(s[i+1]):
                        acu+=1
                    if acu>=4:    
                        print("Invalid")
                        break
                print('valid')
            