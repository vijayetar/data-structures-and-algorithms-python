def reverseArray(list):
  new_list=[]
  for i in range((len(list)),0,-1):
    new_list.append(list[i-1])
  print(new_list)

def reverseArray2(list):
    for i in range(len(list)):
        list[i], list[i+1] = list[-1-i], list[-2-i]
