## Find which computer I am on.
def clues():
    from platform import platform
    if platform()[:6]=='Darwin':
        return 'Darwin'
    elif platform()[:5]=='Linux':
        return 'Linux'
    
