seconds = float(input("what is seconds"))
BLEEP = 0
hours = 0
if seconds >= 60:
    
    BLEEP  = seconds//60
    seconds = seconds%60
if BLEEP >= 60:
    hours = BLEEP//60
    BLEEP = BLEEP%60


print (seconds , "seconds")
print(BLEEP, "minutes")
print(hours,"hours")