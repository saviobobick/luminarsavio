text="bye hello hi hello hi hello bye bye hey hello"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
# high=0
# i=0
# for num in dict:
#     if high<dict[num]:
#         high=dict[num]
#         i=num
# print("Most occured word is:",i)
print(max(dict,key=dict.get))
dict=sorted(dict,key=dict.get,reverse=True)
print(dict)