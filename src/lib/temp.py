"""
Functions to generate temporary files and
find a proper location to generate such files
that are expected to be flushed - like /tmp/ folder
in Unix/Linux


<find_tmp> finds and return the path meant for temporary I/O
operations in several computating resources available to me.
e.g., Palmetto or my Mac.

<gen_tempfile> generates a filename suitable for temporary
I/O operation. If <tmp> argument to <gen_tempfile> is not given
it finds the suitable temp folder using <find_tmp>
"""

def find_tmp(verbose=True):
    """
    Find the relevant temp folder
    in compliance with the CTCMS cluster policy,
    The rule is if there's /data/
    create files there and run vpsc there.

    Argument
    --------
    verbose = True

    Returns
    -------
    _tmp_
    """
    import os
    ## Find local folder that allows fast I/O condition
    if os.path.isdir('/local_scratch/'): ## Palmetto@Clemson
        _tmp_ = '/local_scratch/'
    elif os.path.isdir('/data/'): ## CTCMS cluster@NIST
        _tmp_='/data/ynj/scratch/'
    else:
        _tmp_='/tmp/ynj/'
    if not(os.path.isdir(_tmp_)):
        os.mkdir(_tmp_)
    if verbose:print('_tmp_:%s'%_tmp_)
    return _tmp_


def gen_tempfile(prefix='',affix='',ext='txt',i=0,tmp=None):
    """
    Generate temp file in _tmp_ folder.
    Unless <tmp> argument is specified, the _tmp_ folder
    is determined by <def find_tmp> function

    Arguments
    ---------
    prefix = ''
    affix  = ''
    ext    = 'txt'  (extension, defualt: txt)
    i      : an integer to avoid duplicated name
           (may be deprecated since gen_hash_code2 is used...)
    tmp = None

    Return
    ------
    filename
    """
    import os
    from etc import gen_hash_code2
    if type(tmp).__name__=='NoneType':
        tmp = find_tmp(verbose=False)
    exitCondition = False
    it = 0
    while not(exitCondition):
        hc = gen_hash_code2(nchar=6)
        tmpLocation = find_tmp(verbose=False)
        if len(affix)>0: filename = '%s-%s-%s'%(prefix,hc,affix)
        else:            filename = '%s-%s'%(prefix,hc)
        if type(ext).__name__=='str':
            filename = '%s.%s'%(filename,ext)

        ## under the temp folder
        filename = os.path.join(tmp,filename)
        exitCondition = not(os.path.isfile(filename))
        it = it + 1
        if it>100: exitCondition=True

    if it>1:
        print('Warning: Oddly you just had'+\
            ' an overlapped file name')
    return filename
