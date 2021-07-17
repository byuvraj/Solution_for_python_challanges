def merge_the_tools(string, k):
    j=0
    substr=[]
    l=len(string)
    stri=''
    count=0
    if k != 1:
        for o in string:
            print(o)
    else:
        for i in string:
            add = True
            count+=1
            for char in stri:
                if char == i:
                    add = False
                    j+=1
                    break
                else:
                    add = True
            if j<k and add:
                stri = stri+i
                j+=1
            elif j == k and add:
                print("Done string")
                substr.append(stri)
                stri=i
                j=1
            elif j == k:
                print('set achieved')
                substr.append(stri)
                stri = ''
                j=0
            if count==l:
                print("append")
                print(stri)
                substr.append(stri)   
        for s in substr:
            print(s)    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)