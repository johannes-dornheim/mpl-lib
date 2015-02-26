import time, sys
barLength = 30 # Modify this to change the length of the progress bar

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def update_elapsed_time(second):
    time = 0 
    unit='sec'
    if second<60.:
        unit='sec'
        time = second
    if second>=60. and second<3600:
        unit='min'
        time =second/60.
    if second>=3600:
        unit='hour'
        time =second/3600.
    
    text = "\rElapsed time: %3.2f [%s]"%(time,unit)
    sys.stdout.write(text)
    sys.stdout.flush()
