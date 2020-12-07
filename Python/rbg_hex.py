# def rgb(r, g, b):
  
#     r, g, b = (min(255, max(0, c)) for c in (r, g, b))  
#     #return  "{:02x}{:02x}{:02x}".format(r,g,b)
#     #print(r,g,b)
#     #print(hex(b))
#     #r = int(r , 0)
#     #print(r)
#     #print(type(r))
#     r = hex(r)
#     print(type(r))
#     r = int(r, 16)
#     print(type(r))
#     print(r)
#     g = hex(g)
#     print(g)
#     print(type(g))
#     b = hex(b)
#     print (r,g,b)
#     return

# def rgb(r, g, b):
#     i = 0
#   #r, g, b = (min(255, max(0, c)) for c in (r, g, b))  
#     "%.2X%.2X%.2X" % [r,g,b].map{|i| [[i,255].min,0].max}
#     return rgb
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

rgb = rgb(-20, 255, -254)
print(rgb)
#  STDERR
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
# TypeError: 'str' object is not callable

