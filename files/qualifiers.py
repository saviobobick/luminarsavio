ft=open("teams","r")
fd=open("drop","r")
def getteam(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=getteam(ft)
st2=getteam(fd)
qual=st1-st2
print("Qualifiers are:",qual)
