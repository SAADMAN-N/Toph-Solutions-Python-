
input_count=int(input())

i=1
while i<=input_count:
    input_list=list(input())
    output_dct={}
    
    for index,ch in enumerate(input_list):
        if ch not in output_dct.keys():
            output_dct[ch]=input_list.count(ch)
    
    print('Case #{}:'.format(i))
    for key in output_dct:
        print(key,output_dct[key])
    i+=1


