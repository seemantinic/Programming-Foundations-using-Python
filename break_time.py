import webbrowser
import time

n = 1

print("This program started in "+time.ctime())
while(n < 3):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=dTMLTCJzYGM")
    print("Break number"+n)
    n +=1
    
