def OptimalAssignments(strArr):

  # code goes here
  matrix = [eval(i) for i in strArr]
  res = []
  prev_cost = 0

  for i in range(0,len(matrix)):
    cur = i
    new_cost = prev_cost + matrix[i][i]
    res.append(i)
  print(res)
    
    

    for mac, task in enumerate(res):
      cost = prev_cost - matrix[mac][task] + matrix[mac][i] + matrix[i][task]
      if cost < new_cost:
        new_cost = cost
        cur = mac
    res[i] = res[cur]
    res[cur] = i
    prev_cost = new_cost
  return ''.join(['({0}-{1})'.format(x+1, y+1) for x,y in enumerate(res)])

# # keep this function call here 
print(OptimalAssignments(input()))

OptimalAssignments(["(1,2,1)","(4,1,5)","(5,2,1)"])
