
# Gram - Schmidt

# dot product
def dotProduct(u,v):
    dim = len(u)
    newProduct = 0
    for n in range(dim):
        uNum = u[n]
        vNum = v[n]
        newProduct = newProduct + (uNum * vNum)
    return newProduct
# extra 
def addVectors(u,v):
    dim = len(u)
    newVector = []
    for n in range(dim):
        uNum = u[n]
        vNum = v[n]
        newVector.append(uNum + vNum)
    return newVector

def subVectors(u,v):
    dim = len(u)
    newVector = []
    for n in range(dim):
        uNum = u[n]
        vNum = v[n]
        newVector.append(uNum - vNum)
    return newVector

def scaleVector(u,scale):
    dim = len(u)
    newVector = []
    for n in range(dim):
        newNum = u[n] * scale
        newVector.append(newNum)
    return newVector

# projection
def projection(u,v):
    projection = scaleVector(u,(dotProduct(u,v)/dotProduct(u,u)))
    return projection

def gramSchmidt(W):
    numVectors = len(W)
    orthogBasis = []
    # u1 is just W[0]
    orthogBasis.append(W[0])
    for n in range(1,numVectors):
        print("on v",n+1)
        Vn = W[n]
        proj = Vn
        counter = n
        #print(orthogBasis[counter])
        for i in range(n):
            print("on u",i+1)
            Un = orthogBasis[n-counter]
            print(orthogBasis[n-counter])
            proj = subVectors(proj,(projection(Un,Vn)))
            print(proj)
            print()
            counter = counter  -1
        orthogBasis.append(proj)
    print("the orthogonal basis is")
    return orthogBasis



W = [[3,1,3,0,1],[3,0,3,2,2],[1,-1,-1,2,1]]
x = [[4,2,1],[2,1,4],[1,4,2]]









