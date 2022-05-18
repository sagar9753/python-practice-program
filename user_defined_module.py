import fact as f

x = 5 
y = f.fact(x)
print(x,y)
n=4
r=2
per=f.fact(n) / f.fact(n-r)
comb=f.fact(n) / f.fact(r)*(f.fact(n-r))
print(per)
print(comb)