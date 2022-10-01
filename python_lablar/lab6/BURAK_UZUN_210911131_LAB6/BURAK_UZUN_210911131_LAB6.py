def eylem(file):
    """
    Girdi olarak verilen dosyayı elekleyerek bir sözlüğe gerekli şartları sağlayarak kaydeder.

    Args:
        file:bize verilen dosyayı alır.

    returns:
        sözlük:gerekli sözlüğü dışa verir.   
    
    
    """


    genres = ["Unknown", "Action", "Adventure", "Animation", "Children's",
    "Comedy", "Crime", "Documentary", "Drama",
    "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
    "Romance", "Sci-Fi", "Thriller", "War", "Western"]

    sozluk={}

    file=open(file,"r",encoding="utf-8")
    for satir in file:
        metin=satir.split("|") 
        sozluk[metin[1]]={}
        for i in range(5,24):
            if metin[i]=="1\n" or metin[i]=="1":
                sozluk[metin[1]][genres[i-5]]=1
    file.close()

    # for key,values in sozluk.items():
    #      print(key,"",values)
    print("Veriler Sözlüğe eklendi...")
    return sozluk 
     
def sim_jaccard(sozluk_adi,film_1,film_2):
    p1_intersect_p2 = {}

    for item in sozluk_adi[film_1].keys():        
        if item in sozluk_adi[film_2].keys():             
            p1_intersect_p2[item] = 1

    if p1_intersect_p2=={}:        
        return -1

    # Sozluklerin birlesimlerini alalim
    p1_union_p2 = dict(sozluk_adi[film_1])   
    for item in sozluk_adi[film_2].keys():
        if item not in p1_union_p2: 
            p1_union_p2[item] = 1
    

    p1_intersect_p2, p1_union_p2 = len(p1_intersect_p2), len(p1_union_p2)
    sonuc=float(p1_intersect_p2) / float(p1_union_p2)
    
    return sonuc
    
def topMatches(sozluk_adi,film,n=5,similarity=sim_jaccard):
    """ 
    args:
        sözlük_adi:hangi sözlük üzerinde çalışacaksak onu gönderiyoruz.
        film:bütün sözlükle karşılaştıracağımız film adı.
        n:ilk kaç elemanın listeleneceği
        similarity:hangi sim fonksiyonunu kullancağımız.


    """

    liste=[]
    for film_2 in sozluk_adi:
        if film_2 !=film:
            tu=(sim_jaccard(sozluk_adi,film,film_2),film_2)
            liste.append(tu)
    liste.sort(reverse=True)

    #ekrana güzel gözükmesi için ek olarak böyle bir script yazdım tercihen silinebilir
    #  ve fonksiyonun returnu ile hayata devam edilebilir.
    print("-- {} filmine benzer {} film:".format(film,n))
    for i,k in enumerate(liste,start=1):
        if i==n+1:
            break
        print("{})".format(i),k)
    

    return liste[0:n]

 
 
  