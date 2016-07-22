## Find which computer I am on.
def clues():
    from platform import platform
    if platform()[:6]=='Darwin':
        return 'Darwin'
    elif platform()[:5]=='Linux':
        return 'Linux'

def guessWhereami():
    """
    Determine where am I based on the username
    returned by <whoami>

    Returned locations are all in lowercase.
    if couldn't find, 'unknown' is returned.
    """
    ## add more IDs - locations all in lowercase
    userIDs = dict(
        younguj='palmetto',
        yj='mac')

    import os
    p = os.popen('whoami')
    whoami=p.read().split('\n')[0]

    if whoami in userIDs.keys():
        whereami = userIDs[whoami]
    else:
        whereami ='unknown'
    return whereami


## more environmental options
def determineEnvironment(whereami=guessWhereami()):
    if whereami=='palmetto':
        submitCommand = 'qsub'
    else:
        submitCommand = None
    from MP.lib import checkX
    if checkX.main()!=0:
        availX = False
    else:
        availX = True
    return submitCommand, availX
