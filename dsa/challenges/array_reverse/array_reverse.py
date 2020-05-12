def reverseArray(list):
  new_list=[]
  for i in range((len(list)),0,-1):
    new_list.append(list[i-1])
  print(new_list)