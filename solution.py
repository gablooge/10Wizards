#
# @param Integer src
# @param Integer dest
# @param Array[][] wizards
# @return Array[Integer, Array[]] [Min Cost, Array Min Path]
#

def buildPath(wizard, i, path):
    path = str(i)+" "+path
    # print(path)
    if i == 0:
        return path
    else:
        return buildPath(wizard, wizard[i], path)


def getMinMagic(src, dst, wizards):
        minCost = 0
        minPath = []
        # Put your code here to calculate minCost and minPath
        visited = set()
        costs = [99999999]*10 # assume 99999999 greater the highest cost
        costs[0] = 0
        wizard = [None]*10

        visited.add(src)
        while len(visited) > 0:
            src = visited.pop()
            if src == dst:
                minCost = costs[src]
                break
            for n in wizards[src]:
                d = costs[src] + (n - src) * (n - src)
                if d < costs[n]:
                    costs[n] = d
                    visited.add(n)
                    wizard[n] = src

        # print(costs)
        # print(wizard)
        minPath = buildPath(wizard, dst, "")
        
        # Return the result, do not change the structure
        return minCost, minPath
    
def get_matrix():
    row = 10
    grid = [[] for y in range(row)]

    for i in range(row):
        line = input()
        grid[i] = [int(x) for x in list(line)]
    return grid

if __name__ == "__main__":
    
    src = int(input())
    dest = int(input())
    matrix = get_matrix()
    minCost, minPath = getMinMagic(src, dest, matrix)
    result = str(minCost) + " " + "".join([str(elem) for elem in minPath]) 
    print(result)