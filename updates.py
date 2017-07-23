import os
import datetime
import entwinelib

DATEFMT = '%d %b %Y'

def updated(*exts):
    '''
    Get modification time for last-updated file given a set of extensions
    '''

    upd = 0
    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            for ext in exts:
                if filename.lower().endswith(ext.lower()):
                    mtime = entwinelib.getmtime(dirpath + '/' + filename)
                    upd = mtime if mtime > upd else upd

    return datetime.date.fromtimestamp(upd).strftime(DATEFMT)

