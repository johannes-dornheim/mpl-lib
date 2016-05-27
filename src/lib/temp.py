def find_tmp(verbose=True):
    """
    Find the relevant temp folder
    in compliance with the CTCMS cluster policy,
    The rule is if there's /data/
    create files there and run vpsc there.

    Returns
    -------
    _tmp_
    """
    import os
    ## Find /data/
    if os.path.isdir('/local_scratch/'): ## Palmetto@Clemson
        _tmp_ = '/local_scratch/'
    elif os.path.isdir('/data/'): ## CTCMS cluster@NIST
        # _tmp_='/data/ynj/'
        _tmp_='/data/ynj/scratch/'
    else:
        _tmp_='/tmp/ynj/'
    if not(os.path.isdir(_tmp_)):
        os.mkdir(_tmp_)
    if verbose:print('_tmp_:%s'%_tmp_)
    return _tmp_


def gen_tempfile(prefix='',affix='',ext='txt',i=0):
    """
    Generate temp file in _tmp_

    Arguments
    ---------
    prefix = ''
    affix  = ''
    ext    = 'txt'  (extension, defualt: txt)
    i      : an integer to avoid duplicated name
    """
    import os
    from etc import gen_hash_code2
    _tmp_ = find_tmp(verbose=False)
    exitCondition = False
    it = 0
    while not(exitCondition):
        # hc = gen_hash_code(nchar=6,i=i+it)
        hc = gen_hash_code2(nchar=6)
        tmpLocation = find_tmp(verbose=False)
        filename = '%s-%s-%s'%(prefix,hc,affix)
        if type(ext).__name__=='str':
            filename = '%s.%s'%(filename,ext)

        ## under the temp folder
        filename = os.path.join(_tmp_,filename)

        exitCondition = not(os.path.isfile(filename))
        it = it + 1

    if it>1:
        print('Warning: Oddly you just had'+\
            ' an overlapped file name')
    return filename
