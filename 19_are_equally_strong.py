def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if set([yourLeft, yourRight]) == set([friendsLeft, friendsRight]):
        return True
    else:
        return False