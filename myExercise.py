import sys
data = {}
commands = sys.argv[2].split(",")
f = sys.argv[1]
o = open("outpuFile.txt","w",encoding="utf-8")
with open('student.txt','r',encoding='utf-8') as f:
    for i in f:
        l = i.split(":")
        data[l[0]] = l[1:]
for l in data.values():
    l[-1] = l[-1].rstrip()
for i in commands:
    try:
        o.write(f"Name : {i}, Univeristy : {data[i][0]}\n")
    except KeyError:
        o.write(f"No record of '{i}' was found.\n")




