import time

# define the countdown func.


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") # \r puts this on one line, otherwise it prints a second each second.
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))

# copy countdown(int(t))

# see geekforgeeks.com
# see also stackoverflow.com

# https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/



import sys, time, msvcrt
start_time = time.time()
 if len(input) == 0 and (time.time() - start_time) > timeout:
     print("timing out, using default value.")







import sys, time, msvcrt
def readInput(caption, timeout = 1):
    start_time = time.time()
    sys.stdout.write('%s(%s):'%(caption, "You have 10 Seconds"))
    sys.stdout.flush()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            print("timing out, using default value.")
            break
    print('')  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        sys.exit ("You die")
# and some examples of usage
ans = readInput('Please type a name ') 
print(f"The name is {ans}" )
ans = readInput('Please enter a number') 
print( 'The number is %s' % ans)





import time 
  
# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
  
  
# input time in seconds 
t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(t))





import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))








def countdown(time):
    input(time)
    time = time -1
    return time
    
time = 20
while time > 0:
    time = countdown(time)
#how you would do the countdown via enter with a function









time = 20
while time > 0:
    input(time)
    time = time-1







time = 20
input(time)
time = time -1
input({time}) #Should show 19
time = time -1
rinse and repeat   







