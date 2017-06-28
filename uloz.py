fname = "databaze.csv"

with open(fname) as f:
    data = f.readlines()

print(data)

count = 1
for line in data:
    l = line.split('|')
    n,a,nu = l[0],l[1],l[2]
    print(count,": ")
    print(n,a,nu)
    count += 1

seek = input("Hledej: ")

result = []
for line in data:
    l = line.split('|')
    n = l[0]
    if seek in n:
        result.append(l)
        
    else:
        pass
print(result)


#jmeno = input("Jmeno: ")
#adresa = input("Adresa: ")
#cislo = input("Cislo: ")




#f = open(fname,"a")
#out = jmeno+"|"+adresa+"|"+cislo+"\n"
#f.write(out)
#f.close()

#with open(fname,"a") as f:
#    f.write(out)

#print("Zapsal jsem hodnoty: ",jmeno,adresa,cislo)
