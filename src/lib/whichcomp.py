## Find which computer I am on.
import os
pjoin = os.path.join

def find_vpsc_repo():
    """
    Find path to VPSC repository
    """
    path_home = os.environ['HOME']
    whereami = guessWhereami()

    if   whereami=='palmetto':
        path_vpsc=pjoin(path_home,'repo','vpsc-fld')
    elif whereami=='mac':
        path_vpsc=pjoin(path_home,'repo','vpsc','vpsc-dev-fld')
    elif whereami=='mbp':
        path_vpsc=pjoin(path_home,'repo','vpsc-fld-yld')
    else:
        raise IOError, 'Could not find vpsc repository'
    return path_vpsc

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
    userIDs = dict(younguj='palmetto',yj='mac',youngung='mbp')

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
