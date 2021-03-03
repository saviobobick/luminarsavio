from re import *
#pattern="a+"#one or more a
#pattern="a*"#also checking zero number of a
#pattern="a{2}"#max 2 a
pattern="a{2,3}"#min 2 max 3
matcher=finditer(pattern,"aaacaaabafaaa")
for match in  matcher:
    print(match.start(),"--->",match.group())

