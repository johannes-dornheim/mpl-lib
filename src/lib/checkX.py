checkX_sh = """
if ! xset q &>/dev/null; then
    echo "No X server at \$DISPLAY [$DISPLAY]" >&2
    exit 1
fi
exit 0
"""
# from temp import gen_tempfile
import os, subprocess

def main(verbose=False):
    import temp#.gen_tempfile
    fn_script = temp.gen_tempfile()
    fn_stdo   = temp.gen_tempfile()
    fn_stde   = temp.gen_tempfile()

    with open(fn_script,'w') as fo:
        fo.write(checkX_sh)

    stdo = open(fn_stdo,'w')
    stde = open(fn_stde,'w')
    rst = subprocess.check_call(['bash',fn_script],stdout=stdo,stderr=stde)

    if verbose:
        print 'rst:',rst
        with open(fn_stdo,'r') as fo:
            print fo.read()
        with open(fn_stde,'r') as fo:
            print fo.read()

    stdo.close(); stde.close()
    return rst

if __name__=='__main__':
    import os
    os._exit(main())
