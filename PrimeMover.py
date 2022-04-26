def PrimeMover(num):

  # code goes here
  l = [i for i in range(2,10001) if 0 not in [i%n for n in range(2,i)]]
  return(l[num-1])

# keep this function call here 
print(PrimeMover(input()))
