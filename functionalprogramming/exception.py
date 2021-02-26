employees=[
    {"name":"varun","desig":"devop","sal":40000,"join":2000,"resign":2008},
    {"name":"ram","desig":"devop","sal":30000,"join":1989,"resign":1995},
    {"name":"raju","desig":"qa","sal":28000,"join":2004,"resign":2010},
    {"name":"ravi","desig":"qa","sal":32000,"join":2005,"resign":2015},
    {"name":"sravan","desig":"arkt","sal":35000,"join":2010,"resign":2020}
]
maxsal=max(list(map(lambda emp:emp["sal"],employees)))
print(maxsal)
print(list(filter(lambda emp:emp["sal"]==maxsal,employees)))
print(list(filter(lambda emp:emp["resign"]-emp["join"]>8,employees)))
