
from BURAK_UZUN_211911131_LAB8 import WebScrapper


def main():
     a=WebScrapper()

     #yorumu kaldırırsak sadece kategori ve link sözlüğü verir.
     #print(a.get_categories())
    
    #yorummu kaldırırsak bütün kitap bilgileri ve kategorileri verir.
     print(a.parse())
      


main()