import re
def variableName(name):
    match_value = re.match(r'^[A-Za-z0-9_.]+$', name)
    if match_value:
        if unicode(name[0]).isnumeric():
            return False
        else:
            return True
    else:
        return False
