from urllib.parse import ParseResultBytes
from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.parse import urljoin
import time
import sys


class WebScrapper():

    def get_soup(self,webpage):
        """girdi olarak verilan sayfanın linkindeki html kodlarını güzelleştirip return eder

        Args:

        input_file_name: webpage
        output_file_name: soup

        Returns:

        soup
        
        """
        self.gelensayfalinki=webpage
        self.c = urllib2.urlopen(self.gelensayfalinki)
        self.metin = self.c.read()
        self.soup = BeautifulSoup(self.metin,features="html.parser")
        self.soup.prettify()

        return self.soup
    
     
    def get_categories(self):
        """main sitedeki kategorileri ve kategorilerin linklerini sözlük olarak dışa verir

        Args:

        input_file_name: none
        
        Returns:

        kategorisözlüğü
        
        """
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
        """verilen kategorilerin içindeki kitapların bilgilerini çeker ve dışarıya atar

        Args:

        input_file_name: soup,link
        
        Returns:

        nesneler
        
        """
        self.link=link
        self.h3=soup.find_all("h3")
        self.deger=soup.find_all(class_="price_color")
        
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
        """kategorileri tarar ve get_prices_stars fonksiyonuna gönderir ve bütün 
        kategorideki kitapların bilgilerini bir sözlükte depolar

        Args:

        nıne
        
        Returns:

        genelsozluk
        
        """

        total = 50  # total number to reach       
        bar_length = 34  # should be less than 100
        i=0



        self.genelsozluk={}
        self.x=self.get_categories()
        for kat,lik in self.x.items():
            self.souplusayfa=self.get_soup(lik)
            self.KAT1=self.get_prices_stars(self.souplusayfa,lik)
            self.genelsozluk[kat]=self.KAT1
            ###progress bar
            i=i+1
            percent = 100.0*i/total
            sys.stdout.write('\r')
            sys.stdout.write("Completed: [{:{}}] {:>3}%"
                            .format('='*int(percent/(100.0/bar_length)),
                                    bar_length, int(percent)))
            sys.stdout.flush()
            time.sleep(0.002)
            ###progress bar
        return self.genelsozluk
