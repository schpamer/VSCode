September 2019:

Easy local server spinup python -m http.server 8000

Extenal IP address 174.109.41.105 :80 21

port forward done page works see above

laptop now on static IP 192.168.1.3
DNS servers are now 1.1.1.1 and 1.0.0.1
DNS over HTTPS [long flag needed] check working 1.1.1.1/help

Python list comprehension (best way do now for loop)
squares = [x**2 for x in range(10)]

'''  comment document sphynx need to learn this and see how it works

best way to open file. Better error handling and closed automatically no need to close.
with open(“testfile.txt”) as file:  
data = file.read() 
do something with data 

with open(“hello.txt”, “w”) as f: 
f.write(“Hello World”) 

with open(“hello.txt”) as f: 
data = f.readlines() 

running edge chrome beta, nice works: DL from googled site

12 Sept:
-Done in my VM both packages are installed so check
The drag-and-drop (copy/paste) feature requires both open-vm-tools and gtkmm3 packages to be installed.
- Now both cut and paste and drag and drop work on the VM but had to run (need to at to Xinit so works all the time)
Make the command vmware-user run after X11 by either:

https://wiki.archlinux.org/index.php/VMware/Installing_Arch_as_a_guest#Drag_and_drop,_copy/paste