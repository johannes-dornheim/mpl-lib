def gen_hash_code2(nchar=6):
    """
    Generate random hash tag (to mimick what mdtemp does)

    Arguments
    ---------
    nchar=6
    """
    import os
    return os.urandom(16).encode('hex')[:nchar]

def gen_hash_code(nchar=6):
    """
    Deprecated by gen_hash_code2
    """
    import hashlib
    ## -------------------------------------------------------
    ## Gen HASH code
    m = hashlib.md5()
    m.update(tar_date)
    m.update(time.asctime())
    m.update(time.time())
    return m.hexdigest()[:nchar]
