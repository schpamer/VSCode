from math import*

p = circleIntersection([0, 0],[7, 0],5)
print(p)

# R=2r 

# d = ((b[0]-a[0])**2+(b[1]-a[1])**2)**(.5)
#     print(d)
#     p = (int((2*r**2)*acos(d/(2*r))-d*((2*r)**2-d*d)**(.5)/2))
#     return p

# from math import*
# a,b,x,y,r=input()
# d,R=hypot(x-a,y-b),2*r
# print int(d<R and R*r*acos(d/R)-d*sqrt(R*R-d*d)/2)

# #circleIntersection = lambda a,b,r: 
# def circleIntersection(a,b,r):
#     return int((2*r**2)*acos(((b[0]-a[0])**2+(b[1]-a[1])**2)**(.5)/(2*r))-((b[0]-a[0])**2+(b[1]-a[1])**2)**(.5)*((2*r)**2-((b[0]-a[0])**2+(b[1]-a[1])**2)**(.5)**2)**(.5)/2)

#     #((b[0]-a[0])**2+(b[1]-a[1])**2)**(.5)
#     #d = ((b[0]-a[0])**2+(b[1]-a[1])**2)**(.5); print(d); p = (int((2*r**2)*acos(d/(2*r))-d*((2*r)**2-d*d)**(.5)/2)); return p  
    
    
#     #return p
