
import socket # for socket
import sys
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
# default port for socket
port = 9999
 
host_ip = "192.168.1.32"

# connecting to the server
s.connect((host_ip, port))
 
print ("the socket has successfully connected to host")



from pynput.mouse import Button, Controller

mouse = Controller()
def move(cmds):
    mouse.move(int(cmds[1]),int(cmds[2]))
def click(cmds):
    if(cmd[2]=="True"):
        if(cmd[1]=='left'):
            mouse.press(Button.left)
        if(cmd[1]=='right'):
            mouse.press(Button.right)
    else:
        if(cmd[1]=='left'):
            mouse.release(Button.left)
        if(cmd[1]=='right'):
            mouse.release(Button.right)
def scroll(cmds):
    mouse.scroll(int(cmds[1]),int(cmds[2]))

while True:

    cmd=s.recv(1024).decode()
    print(cmd)
    cmdl=cmd.split(' ')
    switcher ={
        'move':move,
        'click':click,
        'scroll':scroll,
    }
    switcher[cmdl[0]](cmdl)













'''
# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)
'''