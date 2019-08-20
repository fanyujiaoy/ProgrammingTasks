# -*- coding: utf-8 -*-
import numpy

class DPClass:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                    continue
                if i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                    continue
                if i != 0 and j != 0:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                    continue
        return grid[m - 1][n - 1]

    def wer2(r, h):
        d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8)
        print(d)
        d = d.reshape((len(r)+1, len(h)+1))
        print(d)
        """
        [[0 0 0 0]
         [0 0 0 0]
         [0 0 0 0]
         [0 0 0 0]]
        """
        for i in range(len(r)+1):
            for j in range(len(h)+1):
                if i == 0:
                    d[0][j] = j
                elif j == 0:
                    d[i][0] = i
        print(d)
        """
        [[0 1 2 3]
         [1 0 0 0]
         [2 0 0 0]
         [3 0 0 0]
         ]
        """
        for i in range(1, len(r)+1):
            for j in range(1, len(h)+1):
                if r[i-1] == h[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    substitution = d[i-1][j-1] + 1
                    insertion    = d[i][j-1] + 1
                    deletion     = d[i-1][j] + 1
                    print(substitution,insertion,deletion)
                    d[i][j] = min(substitution, insertion, deletion)
        print(d)
        """
        [[0 1 2 3]
         [1 1 2 3]
         [2 2 1 2]
         [3 3 2 2]]
        """
        return d[len(r)][len(h)]
    
    def getHeight(self, men, n):
        longest = {}   
        longest[0] = 1
        for i in range(1, len(men)):
            maxlen = -1
            for j in range(0, i):
                if men[i]>men[j] and maxlen<longest[j]:
                    maxlen = longest[j]
            if maxlen>=1:    
                longest[i] = maxlen +1
            else:
                longest[i] = 1
        return max(longest.values())