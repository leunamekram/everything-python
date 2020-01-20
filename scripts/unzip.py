import os
import sys
import zipfile

if __name__ == '__main__':

    if len(sys.argv) != 3:
        raise Exception('Please provide zip file as first input argument and  \
                         destination folder as second input argumnet.')
    else:
        f = sys.argv[1]
        d = sys.argv[2]

    assert os.path.exists(f), 'Error: Bad zip file argument.'
    assert os.path.exists(d), 'Error: Bad destination argument.'

    ziph = zipfile.ZipFile(f, 'r')
    ziph.extractall(d)
    ziph.close()
