from time import sleep
import os
x = os.get_terminal_size().columns
def gap(): # prints line width of current window.
    x = os.get_terminal_size().columns
    print("-"* x)

def sec(time): # Delay execution of line by 'seconds'
    sleep(time)

def skip(): # prompts user to hit enter to continue program
    input("...")

def prompt(): # combines "skip" and "gap"
    skip() # prompts user to hit enter to continue program
    gap()  # prints line width of current window.

def load(type,time,lines): # creates loading sequence depending on paramters provided


        if type == 1: # prints the Loading across multiple line with a time delay between lines
            print("\n\n")
            print("#      #####  #####  ###    #####  #   #  ##### ".center(x," ")),sec(time)
            print("#      #   #  #   #  #  #     #    ##  #  #     ".center(x," ")),sec(time)
            print("#      #   #  #####  #   #    #    # # #  #  ###".center(x," ")),sec(time)
            print("#      #   #  #   #  #  #     #    #  ##  #   # ".center(x," ")),sec(time)
            print("#####  #####  #   #  ###    #####  #   #  ##### ".center(x," "))
            print("\n\n")


        elif type == 2: # prints '.', each line adds new '.'. number of lines can be defined with a delay bewteen each
            dot = "."
            sec(2)
            print("\n")
            for i in range(0,lines):
                print(dot)
                i = i + i
                dot = dot + "."
                sec(time)
            print("\n")
