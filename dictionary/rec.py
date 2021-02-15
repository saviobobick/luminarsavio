text="A B A C B"
letter=text.split(" ")
dict={}
for word in letter:
    if word in dict:
        print("First recursive letter is ",word)
        break
    else:
        dict[word]=1
