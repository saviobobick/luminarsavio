f=open("text","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
for k in dict: #for k,v in dict.items():
    print(k,"===>",dict[k])
print("Max occured word is:",max(dict,key=dict.get))