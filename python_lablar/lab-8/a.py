import feedparser
import re
import urllib
def getwordcounts(url):

    """filtrelenen  verileri sayar dışarıya iki değişken çıkarır, başlık ve başlığın karşısına gelen kelimeler ve sayıları."""

    def getwords(html):
        """verilerin içindeki kelimerleri istediğimiz şekilde filtreler."""
        # Remove all the HTML tags
        
        txt=re.compile(r'<[^>]+>').sub('',html)

        # Split words by all non-alpha characters
        words=re.compile(r'[^A-Z^a-z]+').split(txt)
        
        # Convert to lowercase
        return [word.lower() for word in words if word!='']

    try:
        d = feedparser.parse(url)
    except urllib.error.URLError as e:
        print("bu url adresinde bir problem var {}".format(url))
        return None, None
    except Exception as e:
        print(' {} hatası nedeni ile bu url işleme sokulmadı {}'.format(url, e))
        return None, None
    
    kelime_saymasi = {}

    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description
        search_text = e.title+' '+summary
         
        # Extract a list of words
        words = getwords(search_text)
        for word in words:
            kelime_saymasi.setdefault(word,0)
            kelime_saymasi[word] += 1
    try:
        return d.feed.title, kelime_saymasi
    except AttributeError:
        return None, None


apcount = {}
wordcounts = {}
feedlist = []

for feedurl in open("feed.txt").readlines():
    print (feedurl)
    title, wc = getwordcounts(feedurl)
    if title != None:
        feedlist.append(feedurl)
        wordcounts[title] = wc #başlık bazında kelimerin sayısının olduğu sözlük.
        for word,count in wc.items(): #genel her şeyin kelimelerin sayısının olduğu sözlük.
            apcount.setdefault(word,0)
            apcount[word]+=1
            
wordlist=[]#son derlenmiş hali çok fazla makaleler içi tekrar eden kelimeleri azaltıyoruz
for w,bc in apcount.items():
    frac=float(bc)/len(feedlist)
    if frac>0.1 and frac<0.7:
        wordlist.append(w)


# Yeni dosyaya yazailm

output_file = 'blogdata_kucuk.txt'
out=open(output_file,'w')
out.write('Blog')
for word in wordlist:
    out.write('\t{}'.format(word))
out.write('\n')

for blog,wc in wordcounts.items():
    # incase there are non ascii blog texts
    blog = blog.encode('ascii','ignore').decode("ascii")
    out.write(blog)
    print(blog)
    for word in wordlist:
        if word in wc:
            out.write('\t{}'.format(wc[word]))
        else:
            out.write('\t0')
    out.write('\n')
    
out.close()


