# Modify the empty list, p, so that it becomes a UNIFORM probability
# distribution over five grid cells, as expressed in a list of 
# five probabilities.

p = [0.2, 0.2, 0.2, 0.2, 0.2]

print p



#  Modify your code to create probability vectors, p, of arbitrary 
#  size, n. Use n=5 to verify that your new solution matches 
#  the previous one.

p=[]
n=5
p=[1/float(n)]*n
print p
