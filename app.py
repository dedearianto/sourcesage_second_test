try:
    n_total = int(input("please input total number (N) :"))
except ValueError:
    n_total = 0

while n_total < 1:
    try:
        n_total = int(input("please input total number (N) :"))
    except ValueError:
        n_total = 0

x_list =[n+1 for n in range(int(n_total))]
total = 0
temp =[]
x_list_set = set(nn for nn in x_list)
print("#################trace#################################")
for x in range(len(x_list)):
    for y in range(len(x_list)):
        xx = {x_list[y],x_list[x]}
        if xx in temp:
            continue
        else:
            temp.append(xx)
        print("x " +str(x) +" y " +str(y) +" temp :" +str(temp))

if x_list_set in temp:
    pass
else:
    temp.append(x_list_set)
print("#################trace#################################")

for data in temp:
    total = total + sum(data)

print("\n\n#################INFO#################################")
print ("\nGiven N = " +str(n_total) +", " +"X :" +str(x_list_set))
print("P(X)  = " +str(temp))
print("Answer = " +str(total))
print("temp type " +str(type(temp)))
print("\n\n#################FINISH#################################")
