f=open("covidreport.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    confirmedcases=int(data[-1])
    dict[state]=confirmedcases
#dict=sorted(dict,key=dict.get,reverse=True)
# print(dict)
for k in dict:
    print(k,"====>",dict[k])
print("\nHighest covid reported state is:",max(dict,key=dict.get))