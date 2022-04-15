#!/bin/python3

import math
import os
import random
import re
import sys


def gridSearch(G, P):
    # Write your code here
    
    G_rsize = len(G)
    G_csize = len(G[0])
    P_rsize = len(P)
    P_csize = len(P[0])
    
    p_c1 = P[0][0]
    p_c2 = P[P_rsize-1][P_csize-1]
    p_c3 = P[0][P_csize-1]
    p_c4 = P[P_rsize-1][0]

    for r in range(0, G_rsize-P_rsize + 1):
        for c in range(0, G_csize-P_csize + 1):
            g_c1 = G[r][c]
            g_c2 = G[r+P_rsize-1][c+P_csize-1]
            g_c3 = G[r][c+P_csize-1]
            g_c4 = G[r+P_rsize-1][c]            
         
            if g_c1 == p_c1 and g_c2 == p_c2 and g_c3 == p_c3 and g_c4 == p_c4:                
                g_values = [row[c:c+P_csize] for row in G[r:r+P_rsize]]
                p_values = P
            
                if g_values == p_values:
                    return 'YES'
                else:            
                    return 'NO'
    return 'NO'

if __name__ == '__main__':
    
    with open('data.txt', 'r') as f:
        files = f.read().splitlines() 
        num = int(files[0])

        row, col = 0, 0
        readlines = 1
        for n in range(num):
            row, col = files[readlines].rstrip().split()
            row, col = int(row), int(col)
            readlines +=1 

            G = []
            for r in range(row):
                G.append(files[readlines + r])
            readlines += row

            prow, pcol = files[readlines].rstrip().split()
            prow, pcol = int(prow), int(pcol)
            readlines += 1

            P = []
            for r in range(prow):
                P.append(files[readlines + r])
            readlines += prow

            if n == 3:
                print('debug')

            print(gridSearch(G, P))
            print('1 cycle end')
    print('end')
            



