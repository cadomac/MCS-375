# author: Cameron MacDonald

def tsp(dist):
    global minDist

    minDist = float('inf')
    perm(1, 0)
    print("minimum tour length = %g" % minDist)

def perm(i, newDist):
    global minDist

    n = len(dist)
    if i == n-1:
        newDist += dist[pi[i]][pi[0]] + dist[pi[i-1]][pi[i]]
        d = newDist
        if d < minDist:
            minDist = d
    else:
        for j in range(i, n):
            pi[i], pi[j] = pi[j], pi[i]
            perm(i+1, newDist + dist[pi[i-1]][pi[i]])
            pi[i], pi[j] = pi[j], pi[i]

###################### Testing ######################
dist = [
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
        [ 9,  0,  8,  7,  6,  5,  4,  3, 10,  1,  2],
        [ 8,  7,  0,  6,  5,  4,  3,  2,  9, 10,  1],
        [ 7,  6,  5,  0,  4,  3,  2,  1,  8,  9, 10],
        [ 4,  3,  2,  1,  0, 10,  9,  8,  7,  6,  5],
        [10,  9,  8,  7,  6,  0,  5,  4,  3,  2,  1],
        [ 7,  8,  9, 10,  1,  2,  0,  3,  4,  5,  6],
        [ 5,  4,  3,  2,  1,  6,  7,  0,  8,  9, 10],
        [10,  9,  8,  7,  6,  5,  4,  3,  0,  2,  1],
        [ 1,  2,  4,  3,  6,  5,  8,  7, 10,  0,  9],
        [ 3,  2,  1,  6,  5,  4,  9,  8,  7, 10,  0]
        ]

pi = list(range(len(dist)))
if __name__ == '__main__':
    tsp(dist)
