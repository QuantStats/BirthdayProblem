from scipy.stats import binom
from math import factorial

def nCr(n,r):
    #the combination formula, n choose r
    return factorial(n) // factorial(r) // factorial(n-r)


k = 2 #number of matched
n = 30 #number of people
T = 365 #number of days

noc = nCr(n, k) #number of possible combinations

pm0 = binom.pmf(0, noc, 1/(T**(k-1)))    #the probability mass at 0

print(1-pm0)

#analytics for ***k=2 only***

pnm = (factorial(T)//factorial(T-n))/(T**n) #probability of no match

print(1-pnm)    #probability of a match


