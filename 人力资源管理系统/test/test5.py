import re


def incr14Str(string):
    """Increase one (+1) in the last number part of string."""

    rt = re.search(r'(\d+)([^\d]*$)', string)
    if rt:
        pos_left = rt.span()[0]
        num = int(rt.groups()[0])
        numStr = ''
        for i in range(len(rt.groups()[0]) - len(str(num + 1))):
            numStr += '0'
        else:
            numStr += str(num + 1)
        return string[:pos_left] + numStr[len(numStr) - len(rt.groups()[0]):] + rt.groups()[1]
    else:
        raise ValueError('No suitable number segment found to +1.')


string = incr14Str('111')
print(string)
