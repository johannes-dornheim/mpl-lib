## Find which computer I am on.
def clues():
    from platform import platform
    if platform()[:6]=='Darwin':
        return 'Darwin'
    elif plaotform()[:5]=='Linux':
        return 'Linux'
    
