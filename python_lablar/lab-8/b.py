from urllib.parse import ParseResultBytes
from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.parse import urljoin
import time
import sys


class WebScrapper():


    def get_soup(self,webpage):
        
        self.gelensayfalinki=webpage
        self.c = urllib2.urlopen(self.gelensayfalinki)
        self.metin = self.c.read()
        self.soup = BeautifulSoup(self.metin,features="html.parser")
        self.soup.prettify()

        return self.soup
    
     
    def get_categories(self):
        self.mainsite="http://books.toscrape.com/index.html"

        self.soup=self.get_soup(self.mainsite)
         
        self.navlistler = self.soup.find_all(class_='nav nav-list')
        self.a_listesi = self.navlistler[0].findChildren("a" , recursive=True)
       
        self.kategorisozlugu={}
        for i in range(1,len(self.a_listesi)):

            self.stripcategories=self.a_listesi[i].string.strip()
            self.link=self.a_listesi[i].get("href")
            self.link_birlesmis = urljoin(self.mainsite, self.link)

            self.kategorisozlugu[self.stripcategories]=self.link_birlesmis

       
         
        return self.kategorisozlugu

    def get_prices_stars(self,soup,link):
        self.link=link
        self.h3=soup.find_all("h3")
        self.deger=soup.find_all(class_="price_color")
        self.rate=soup.find_all(class_="")
        
        self.nesneler=[]
        for i in range(len(self.h3)):
            self.kitaplarSoz={}
            self.kitapAdi=self.h3[i].string.strip().strip()
            self.KitapFiyati=self.deger[i].string
            self.a_listesi = self.h3[i].findChildren("a" , recursive=True)
            self.a_linki=self.a_listesi[0].get("href")
            self.joinlink=urljoin("{}".format(self.link),self.a_linki)


             
            self.kitaplarSoz["Name"]=self.kitapAdi
            self.kitaplarSoz["Price"]=self.KitapFiyati
            self.kitaplarSoz["Url"]=self.joinlink

            self.nesneler.append(self.kitaplarSoz)

        
        return self.nesneler

    
    def parse(self):

        total = 50  # total number to reach       
        bar_length = 34  # should be less than 100
        i=0



        self.genelsozluk={}
        self.x=self.get_categories()
        for kat,lik in self.x.items():
            self.souplusayfa=self.get_soup(lik)
            self.KAT1=self.get_prices_stars(self.souplusayfa,lik)
            self.genelsozluk[kat]=self.KAT1

            i=i+1
            percent = 100.0*i/total
            sys.stdout.write('\r')
            sys.stdout.write("Completed: [{:{}}] {:>3}%"
                            .format('='*int(percent/(100.0/bar_length)),
                                    bar_length, int(percent)))
            sys.stdout.flush()
            time.sleep(0.002)
         

def main():
    a=WebScrapper()
    a.parse()
    


main()