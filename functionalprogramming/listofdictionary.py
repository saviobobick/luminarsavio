players=[
    {"name":"sachin","matches":500,"rank":1},
    {"name":"dravid","matches":450,"rank":12},
    {"name":"sehwag","matches":250,"rank":52},
    {"name":"msd","matches":360,"rank":7}
]
name=list(map(lambda dict:dict["name"],players))
rank=list(map(lambda dict:dict["rank"],players))
print(name,rank)
above=list(map(lambda player:player["name"],list(filter(lambda dict:dict["matches"]>320,players))))
print(above)