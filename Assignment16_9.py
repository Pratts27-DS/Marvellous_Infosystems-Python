# Write a program which display first 10 even numbers on screen.

def Even():
    for i in range(1,21):
        if i % 2 == 0:
            print(i,end=" ")
        
Even()