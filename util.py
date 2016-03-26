import errno
import os

def makedirs(path):
    """
    Creates the directory at the given path, does nothing if it already
    exists.
    """
    try:
        os.makedirs(path)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise error 

def blocks(lines):
    """
    Partitions a sequence of lines (such as a file-like object) into lists of
    empty-line-separated lines.
    """
    block = []
    for line in lines:
        if not line.strip():
            yield block
            block = []
        else:
            block.append(line)
    if block:
        yield block
