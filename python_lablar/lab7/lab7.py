import feedparser
import re
from recommandations import topMatches, sim_pearson


def lab5_soru1_sorua_cozum1(input):
    s = ''
    for c in input:
        if not (c == "_"):
            s +=c.lower()

    return s


def lab5_soru1_sorua_cozum2(input):
   return "".join([c.lower() for c in input if c!="_"])


def lab5_soru1_sorub_cozum1(input):
    harita = {}
    for i in input:
        if i%2 ==0:
            harita[i]  = 'cift'
        else:
            harita[i] = 'tek'
    return harita

def lab5_soru1_sorub_cozum2(input):
    return {c: 'cift' if c%2 ==0 else 'tek' for c in input}



def getwords(html):
    txt=re.sub(r'<[^>]+>', '', html)

    # Split words by all non-alpha characters
    words=re.split(r'[^A-Z^a-z]+', txt)

    return [word.lower() for word in words if word!='']


def lab7_soru2(feedlist):
    
    sozluk1 = {}
    sozluk2 = {}
    for site in feedlist:
        d = feedparser.parse(site)
        wc = {}
        wl = {}
        for e in d.entries:
            summary = e.summary
            description = e.description
            title = e.title
            uzun_cumle = title + ' ' + description +' ' + summary
            words = getwords(e.title+' '+summary)

            for index, word in enumerate(words):
                wc.setdefault(word,0)
                wl.setdefault(word,[])
                wc[word] += 1
                wl[word].append(index)
        try:
            sozluk1[d.feed.title] = wc
            sozluk2[d.feed.title] = wl
        except AttributeError:
            print('-'*20)
            print('Bu siteyi acamadim:', d.feed)
            print('-'*20)


    return sozluk1, sozluk2

def lab7_soru3(sozluk):

    for key,values in sozluk.items():
        print("-"*20)
        print(key)
        print(topMatches(sozluk, key, 5, sim_pearson))


def main():
    test_list = ['MukemmelDegisken', 'buNasilDegisken', 'degisken2Ismi', 'degiskenIsmi2',
                    'yilan_degisken', 'yilan_2degisken', 'yilan_degisken3', 'SonucDegiskeni3', 'HTTPCevabi', 'deneme_YaziMi']
    print('|'*20)
    for i in test_list:
        print(lab5_soru1_sorua_cozum1(i))
    print('|'*20)
    for i in test_list:
        print(lab5_soru1_sorua_cozum2(i))
    print('|'*20)
    print(lab5_soru1_sorub_cozum1([2, 3, 5, 7]))
    print('|'*20)
    print(lab5_soru1_sorub_cozum2([2, 3, 5, 7]))
    print('|'*20)

    FeedListesi = ['http://feeds.feedburner.com/37signals/beMH',
        'http://feeds.feedburner.com/blogspot/bRuz', 
        'http://battellemedia.com/index.xml',
        'http://feeds.feedburner.com/hotair/main', 
        'http://blog.outer-court.com/rss.xml']

    s1, s2 = lab7_soru2(FeedListesi)
    lab7_soru3(s1)

main()