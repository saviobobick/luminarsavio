from re import *
#pattern='[ab]'#either a or b
#pattern='[a-b]'#checking for lowercase alhabets
#pattern='[A-Z]'
#pattern='[a-zA-Z]'
#pattern='[0-9]'
#pattern='[^0-9]'#except digits
#pattern="\s"#checking space
#pattern="\d"#checking digits
#pattern="\D"#except digits
#pattern="\w"#all words
pattern=r'\\s'
# pattern="ab"
source="ababa\sbbbab"
matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    cnt+=1
    print(match.start(),"-->",match.group())
print(cnt,"match has been found")

