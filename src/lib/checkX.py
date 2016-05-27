checkX_sh = """
if ! xset q &>/dev/null; then
    echo "No X server at \$DISPLAY [$DISPLAY]" >&2
    exit 1
fi
exit 0
"""
from temp import gen_tempfile
import os

def main():
    rst= os.system(checkX_sh)
    print 'rst:', rst
    return rst

if __name__=='__main__':
    import os
    os._exit(main())
