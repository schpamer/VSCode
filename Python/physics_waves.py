#GlowScript 2.7 VPython

# Enter wave properties below.
amplitude_1 = 1.0
frequency_1 = 1.0
wavelength_1 = 1.0 
phase_1 = 0.0

amplitude_2 = 1.0
frequency_2 = 1.0 
wavelength_2 = 1.0 
phase_2 = 0.0

# Change the values below to adjust the size of the grid.
xmax = 4
ymax = 2
make_grid()
dx = 2*xmax/150
wave_1 = curve(color=color.red)
wave_2 = curve(color=color.blue)
total_wave = curve(color=color.green)
for x in range(-xmax,xmax+dx,dx):
  wave_1.append(vector(x,wave_fun_1(x,0),0))
  wave_2.append(vector(x,wave_fun_2(x,0),0))
  total_wave.append(vector(x,wave_fun_1(x,0)+wave_fun_2(x,0),0))
def wave_fun_1(x,t):
  return amplitude_1*cos(2*pi*(x/wavelength_1-frequency_1*t)+phase_1)
def wave_fun_2(x,t):
  return amplitude_2*cos(2*pi*(x/wavelength_2-frequency_2*t)+phase_2)

dt = dx/(wavelength_1*frequency_1)
animation_rate = 10
time = 0
while (True):
  rate(animation_rate)
  for i in range(0,wave_1.npoints):
    wave_1.modify(i,y=wave_fun_1(wave_1.point(i).pos.x,time))
    wave_2.modify(i,y=wave_fun_2(wave_2.point(i).pos.x,time))
    total_wave.modify(i,y=wave_1.point(i).pos.y+wave_2.point(i).pos.y)
  time += dt

### Don't change anything below here! ###

def make_grid():
  scene.background = color.white
  thickness = 0.02
  dx = 1
  x = -xmax
  while (x <= xmax):
    y = -ymax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (y <= ymax):
      gridline.append(vector(x,y,-thickness))
      y = y + dx
    x = x + dx
  y = -ymax
  while (y <= ymax):
    x = -xmax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (x <= xmax):
      gridline.append(vector(x,y,-thickness))
      x = x + dx
    y = y + dx
  label(text="green = red + blue",pos=vector(0,ymax+0.4,0))
  return