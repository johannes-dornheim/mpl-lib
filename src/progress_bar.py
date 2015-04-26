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
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block),'%3.3i'%(progress*100), status)
    sys.stdout.write(text)
    sys.stdout.flush()

def progress_line(head,dat,iflush=True):
    text = "\r%s: %s [%s]"%(head,dat)
    sys.stdout.write(text)
    if iflush: sys.stdout.flush()

def update_elapsed_time(second,iflush=True,head='Elapsed time'):
    time = 0
    unit='sec'
    if second<60.:
        time = '%5.2f [sec]'%second
    if second>=60. and second<3600:
        unit='min'
        m = second/60.
        s = second - int(m)*60.
        time = '%2.2i [min] %2.2i [sec]'%(m,s)
    if second>=3600:
        unit='hour'
        h = second/3600.
        m = (second - int(h)*3600.)/60.
        s = second - int(m) * 60. - int(h)*3600.
        time = '%5.5i [hour] %2.2i [min] %2.2i [sec] '%(h,m,s)

    text = "\r%s: %s"%(head,time)
    sys.stdout.write(text)
    if iflush: sys.stdout.flush()
