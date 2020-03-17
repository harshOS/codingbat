#problem link - https://codingbat.com/prob/p149391

def xyz_there(str):
    if str[0:3] == 'xyz': return True
    for i in range(len(str)):
        if str[i] != '.' and str[i + 1:i + 4] == 'xyz':
            return True
    return False
print(xyz_there('xyz.abc'))
