import socket            

s = socket.socket()
print ("Socket successfully created")
clients=[]
port = 9999

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")


c, addr = s.accept()
clients.append(c)

from pynput import mouse
ctr=mouse.Controller()
btn=mouse.Button
prx,pry=ctr.position
def on_move(x, y):
    global prx
    global pry
    dx,dy,prx,pry=x-prx,y-pry,x,y
    for i in clients:
        i.send(" ".join(("move",str(dx),str(dy))).encode())

def on_click(x, y, button, pressed):
    for i in clients:
        i.send(" ".join(("click","left" if button==btn.left else "right",str(pressed))).encode())

def on_scroll(x, y, dx, dy):
    for i in clients:
        i.send(" ".join(('scroll',str(dx),str(dy))).encode())

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

listener.start()

input()

