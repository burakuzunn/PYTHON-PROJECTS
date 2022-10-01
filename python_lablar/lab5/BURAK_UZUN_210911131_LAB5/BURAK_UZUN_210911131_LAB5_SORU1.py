from cr import critics as critics 
def sim_jaccard(prefs,person1,person2):
    birlesim=0
    kesisim=0
    
    for film in prefs[person1]:
        if film in prefs[person2]:
            kesisim+=1
            
    birlesim=len(critics[person1] | critics[person2])
    
    if kesisim==0: 
        print("ortak film yoktur")
        return 0
    elif kesisim==birlesim:
        print("Evlenebilirsiniz Tam eşleşme")
        return 0
    
    deger=1/1-(kesisim/birlesim)
    print("{} kullanıcısı ile {} kullanıcısı arasındaki jaccard benzerliği:".format(person1,person2),deger,"kadardır")
    
    
