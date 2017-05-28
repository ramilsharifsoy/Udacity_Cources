# Modify the empty list, p, so that it becomes a UNIFORM probability distribution over five grid cells, as expressed 
# in a list of five probabilities.
p = [0.2, 0.2, 0.2, 0.2, 0.2]
print p

#  Modify your code to create probability vectors, p, of arbitrary size, n. Use n=5 to verify that your new solution matches 
#  the previous one.
p=[]
n=5
p=[1/float(n)]*n
print p

#Write code that outputs p after multiplying each entry by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cellsare misses.
p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2
sense = [pMiss, pHit, pHit, pMiss, pMiss]
post = []
for i in range(len(sense)):
    post.append(p[i] * sense[i])
p = post

# or
p[0] = p[0]*pMiss
p[1] = p[1]*phit
p[2] = p[2]*phit
p[3] = p[3]*pMiss
p[4] = p[4]*pMiss
print p


#Modify the program to find and print the sum of all the entries in the list p.
p=[0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2
p[0]=p[0]*pMiss
p[1]=p[1]*pHit
p[2]=p[2]*pHit
p[3]=p[3]*pMiss
p[4]=p[4]*pMiss
# Enter your code below
sump = sum(p)
print sump

#Modify the code below so that the function sense, which takes p and Z as inputs, will output the NON-normalized probability
#distribution, q, after multiplying the entries in p by pHit or pMiss according to the color in the corresponding cell in world.
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2
print sum(p)

def sense(p, Z):
    q = []
    for i in range(len(p)):
        if (world[i]==Z):
            q.append(p[i]*pHit)
        else:
            q.append(p[i]*pMiss)
    return q
print sense(p,Z)

print sense(p,Z)

#Modify your code so that it normalizes the output for the function sense. This means that the entries in q should sum to one
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    print s
    for  i in range(len(q)):
        q[i] = q[i]/s
    return q
print sense(p,Z)

#Try using your code with a measurement of 'green' and make sure the resulting probability distribution is correct.
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(p)):
        q[i]=q[i]/s 
    return q
print sense(p, Z)
#Result: [0.2727272727272727, 0.09090909090909093, 0.09090909090909093, 0.2727272727272727, 0.2727272727272727]

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        miss = (Z == world[i])
        q.append(p[i] * (miss * pMiss + (1-miss) * pHit))
    s = sum(q)
    for i in range(len(p)):
        q[i]=q[i]/s 
    return q
print sense(p, Z)
#Result: [0.1111111111111111, 0.3333333333333332, 0.3333333333333332, 0.1111111111111111, 0.1111111111111111]

#Modify the code so that it updates the probability twice and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q
    
for k in range(len(measurements)):
    p = sense(p, measurements[k])
print p

#Program a function that returns a new distribution q, shifted to the right by U units. If U=0, q should be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    U = U % len(p)
    q = p[-U:] + p[:-U]
    return q

print move(p, 1)

#Modify the move function to accommodate the added probabilities of overshooting or undershooting the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U)%len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
    

print move(p, 1) #[0.0, 0.1, 0.8, 0.1, 0.0]

#Write code that makes the robot move twice and then prints out the resulting distribution, starting with the initial 
#distribution p = [0, 1, 0, 0, 0]

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

p = move(p, 1)
p = move(p, 1)
print p  #[0.010000000000000002, 0.010000000000000002, 0.16000000000000003, 0.6600000000000001, 0.16000000000000003]

#write code that moves 1000 times and then prints the 
#resulting probability distribution.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
    
for i in range(1000):
  p = move(p,1)
print p #[0.20000000000000365, 0.20000000000000373, 0.20000000000000365, 0.2000000000000035, 0.2000000000000035]


#Given the list motions=[1,1] which means the robot moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for m in range(len(motions)):
  p = sense(p, measurements[m])
  p = move(p, motions[m])

print p #[0.21157894736842103, 0.1515789473684211, 0.08105263157894739, 0.16842105263157897, 0.3873684210526316]

#Modify the previous code so that the robot senses red twice.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])
    
print p #[0.07882352941176471, 0.07529411764705884, 0.22470588235294123, 0.4329411764705882, 0.18823529411764706]
