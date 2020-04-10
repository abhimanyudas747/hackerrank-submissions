def climbingLeaderboard(scores, alice):
    scores = list(dict.fromkeys(scores))
    k = len(scores)
    res = []
    for i in alice:
        for j in range(k):
            if(i >= scores[j]):
                print(i, "::", scores[j])
                res.append(j+1)
                break
        if(i < scores[j]):
            res.append(j+2)
    return res
res = climbingLeaderboard([100, 90, 90, 80, 75, 60],[50, 65, 77, 90, 102])
