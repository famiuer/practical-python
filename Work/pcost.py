# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    f = open(filename, 'rt')

    #headers = next(f).split(',')
    #print(headers)
    sum = 0
    for line in f:
        row = line.split(',')
        #print(row)
        sum = sum + int(row[1]) * float(row[2])
    f.close()
    print(f'Total cost {sum}')

import sys 

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
#portfolio_cost(filename)
#print('Total cost:', cost)
