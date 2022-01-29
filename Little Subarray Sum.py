
input_string=input()
input_string2=input()

N,A,B=input_string.split()
list1=input_string2.split()

total=0
for item in list1[int(A):(int(B)+1)]:
    total+=int(item)
print(total)
    