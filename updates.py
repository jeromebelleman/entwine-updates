import os
import datetime

DATEFMT = '%d %b %Y'

def updated(*exts):
    '''
    Get modification time for last-updated file
    '''

    upd = 0
    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    mtime = os.stat(dirpath + '/' + filename).st_mtime
                    upd = mtime if mtime > upd else upd

    return datetime.date.fromtimestamp(upd).strftime(DATEFMT)
