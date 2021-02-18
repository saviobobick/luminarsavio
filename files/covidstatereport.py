f=open("covidreport.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    confirmedcases=int(data[-1])
    curedcases=int(data[-3])
    deathcases=int(data[-2])
    dict[state]={state:{"State":state,"Confirmed":confirmedcases,"Cured":curedcases,"Death":deathcases}}
for k in dict:
    print(dict[k])
