pattern="ABABC"
for i in pattern:
    for j in pattern:
        if i==j:
            print("First recursive element is ",i)
            break
    break