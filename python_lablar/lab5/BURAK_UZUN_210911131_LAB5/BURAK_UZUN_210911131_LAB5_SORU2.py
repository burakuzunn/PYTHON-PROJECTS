from cr import critics as critics


    
def sim_cosine(prefs,person1,person2):
    p=[]
    q=[]
    for film in prefs[person1]:
        if film in prefs[person2]:
            p.append(prefs[person1][film])
            q.append(prefs[person2][film])

    intersection = set(p[1]) & set(q[1])
    union = set(p[1]) | set(q[1])
    tanimoto = len(intersection) / float(len(union))
    print(tanimoto)

sim_cosine(critics,"Ali","Jack Matthews")
