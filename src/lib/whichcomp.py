## Find which computer I am on.
import os
pjoin = os.path.join

def find_vpsc_repo():
    """
    Find path to VPSC repository
    """
    path_home = os.environ['HOME']
    whereami = guessWhereami()

    ## test if repo/vpsc-fld-yld is present
    if   whereami=='palmetto':
        path_vpsc=pjoin(path_home,'repo','vpsc-fld')
    elif whereami=='mac':
        path_vpsc=pjoin(path_home,'repo','vpsc','vpsc-dev-fld')
    elif whereami=='mbp':
        path_vpsc=pjoin(path_home,'repo','vpsc-fld-yld')
    elif whereami=='ubuntu@mml':
        path_vpsc=pjoin(path_home,'repo','vpsc-fld-yld')
    elif whereami=='hg@ubuntu':
        path_vpsc=pjoin(path_home,'vpsc-fld-yld-postech')
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
    userIDs = dict(younguj='palmetto',yj='mac',youngung='mbp',hwigeon='hg@ubuntu')#,yougnung='ubuntu@mml'

    p = os.popen('whoami')
    whoami=p.read().split('\n')[0]
    print '-----------------'
    print 'whoami:', whoami
    print '-----------------'
    if whoami in userIDs.keys():
        if whoami=='youngung': ## either my mbp or ubuntu@mml
            path_home = os.environ['HOME']
            if path_home==pjoin(os.sep,'Users','youngung'):
                whereami='mbp'
            elif path_home==pjoin(os.sep,'home','youngung'):
                whereami='ubuntu@mml'
            else:
                print 'whoami:', whoami
                print 'path_home:',path_home
                raise IOError, 'Did not expect this case in whichcomp'
        else:
            whereami=userIDs[whoami]
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
