from numpy import dot
from numpy.linalg import norm
from cr import critics as critics
 
    
def sim_cosine(prefs,person1,person2):
    '''
    Girdi olarak verilen sözlük ve sözlük içindeki keyleri cosine methodu kullanarak benzerlik oranını verir.

    args:
        prefs,person1,person2
    returns:
        0,cosinus,person1,person2  
    raises:
        none
    
    
    '''
    p=[]
    q=[]
    
    for film in prefs[person1]:
        if film in prefs[person2]:
            p.append(prefs[person1][film])
            q.append(prefs[person2][film])
    
    if q==[]:
        
        print("Kişilerin ortak filmleri yok.")
        return 0

    else:
        cosinus = dot(p, q)/(norm(p)*norm(q))
        cosinus=1/(1+cosinus)
        print("{} kullanıcısı ile {} kullanıcısı arasındaki cosinus benzerliği:".format(person1,person2),cosinus,"kadardır")

    

    