# This is a simple infinite loop
# Don't run this program until you're sure you can buy a new PC

def loop1():
    while 1:
        print("Too bad!!!!!", end=" ")

def loop2():
    while 1:
        print("You can't escape", end=" ")
        
def loop3():
    while 1:
        print("You thought I was playing", end=" ")
        
def loop4():
    while 1:
        print("You can't escape the matrix", end=" ")        

def infinite_loop():
    try:
        while 1:
            loop1()
    except KeyboardInterrupt:
        loop2()
    
    finally:
        try:
            while 1:
                loop3()
        except KeyboardInterrupt:
            loop4()
        finally:
            while 1:
                infinite_loop()

infinite_loop()

# This code won't harm your PC
# Maybe , not yet ...
# Still in development