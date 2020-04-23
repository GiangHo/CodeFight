def alternatingSums(a):
    team_1 = 0
    team_2 = 0
    for i in range(len(a)):
        if i%2 ==0:
            team_1 = team_1 + a[i]
        else:
            team_2 = team_2 +a[i]
    return [team_1, team_2]
