
input_time=int(input())

for i in range(input_time):
    s=input()
    a,b=s.split()
    avg=(int(a)+int(b))//2
    if avg%2==0:
        print("Sadia will be happy.")
    else:
        print("Oops!")
    