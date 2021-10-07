from urllib.request import Request, urlopen
import urllib.error
from bs4 import BeautifulSoup
import datetime

#sonunda numarası da olmalı
#ENTRY_TITLE = "borsa-istanbul--3559807"
#ENTRY_TITLE = "5-ekim-2021-insansi-robot-satislarina-baslanmasi--7049562"
#ENTRY_TITLE = "covid-19--6362411"
ENTRY_TITLE = "m-a-erbil-ve-ece-ronayin-nisanlisinin-anlasmasi--7050924"

#başlıktaki ilk entrynin ne zaman yazıldığını bul
def first_entry_date(title):

    #başlıktaki ilk sayfanın kaynak kodlarını çek
    req = Request("https://eksisozluk.com/" + title, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    webpage = urlopen(req).read().decode('utf-8')
    
    #html parser
    soup = BeautifulSoup(webpage, 'html.parser')
    
    #class'ı "entry-date permalink" olan tüm <a> taglerini çek
    for element in soup.find_all("a", {"class": "entry-date permalink"}):
    
        #her bir <a> tag'inin innerHTML'i, entry'nin yazıldığı tarihi ve saati veriyor.
        date_parsed = element.encode_contents()
        
        #binary string to string
        date_parsed = date_parsed.decode('UTF-8')
        
        #format şu şekilde 28.09.2012 10:34
        #bazen şöyle sonuçlar da oluyor 28.09.2012 10:37 ~ 10:37
        #ilk 10 karakter tarihi veriyor
        date_parsed = date_parsed[0:10]
        print("ilk entry tarihi: ",date_parsed)
        
        return date_parsed
        
#her gün kaç entry yazıldığını bul
def find_number_of_entry_every_day(title, first_date):

    #first_date = "13.03.2020" #SİL

    #tüm verileri tutmak için iki array
    #all_data = []
    #all_dates = []
    
    #bugün için datetime oluştur
    now = datetime.datetime.now()
    #dakika saniye milisaniye verilerini sil
    now = datetime.datetime(now.year,now.month,now.day)

    #ilk entry tarihi için datetime oluştur format: yıl,ay,gün
    date = datetime.datetime(int(first_date[6:10]), int(first_date[3:5]), int(first_date[0:2]))
    
    file = open(title+".csv", "a") 
    
    
    
    #ilk tarihten bugüne kadar entrleri çekmeye devam et (bugün hariç)
    while date < now:
    
        #date'i şu stringe çevir: yyyy-mm-dd
        date_for_ulr = date.strftime("%Y-%m-%d")
        
        current_page = 1
        total_page = 10000
        
        total_entry_for_day = 0
    
        #aynı gün her sayfa için tekrar et
        while current_page <= total_page:
        
            #print("current_page", current_page, "total_page", total_page)
    
            #belirli bir gündeki ekşi sayfasına git
            link = "https://eksisozluk.com/" + title + "?day=" + date_for_ulr + "&p=" + str(current_page)
            req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            
            try:
                conn = urlopen(req)
            except urllib.error.HTTPError as e:

                #eğer 200 değilse ya bağlanamadı ya da 404 entry yok.
                if 200 != e.code:
                    if 404 == e.code:
                        print("tarih: ", date_for_ulr, " sayfa: ", current_page, " sayı: 0")
                    else:
                        print("HTTP status: ", e.code, " tarih ", date_for_ulr)
                    
                    #bugünün döngüsünden çık
                    break
            
            webpage = conn.read().decode('utf-8')
            
            #html parser
            soup = BeautifulSoup(webpage, 'html.parser')
            
            #class'ı "entry-date permalink" olan tüm <a> taglerini çek
            elements = soup.find_all("a", {"class": "entry-date permalink"}, limit=None)
            #elements = soup.find_all(attrs={"class": "entry-date permalink"})
            
            #print(webpage.count("entry-date permalink"))

            print("tarih: ", date_for_ulr, " sayfa: ", current_page, " sayı: ", len(elements))
            
            #toplam sayfa sayısı
            try:
                total_page = int( soup.find("div", {"class": "pager"})["data-pagecount"] ) 
            except:
                #1 sayfa varsa, sayfa sayısı görünmüyor
                pass
                
            current_page = current_page + 1
            
            
            #verileri tutan değişkene sonucu ekle
            total_entry_for_day = total_entry_for_day + len(elements)
        
        #tüm günlerin verilerini tutan arraylere toplam sonucu ekle
        #all_dates.append(date_for_ulr)
        #all_data.append(total_entry_for_day)
        
        print("tarih: ", date_for_ulr, "toplam entry: ", total_entry_for_day)
            
        #bir sonraki gün
        date = date + datetime.timedelta(days=1)
        
        #dosyaya yaz
        file.write(date_for_ulr +", "+ str(total_entry_for_day))
        file.write('\n')
        file.flush()
        
    file.close()

        
       
first_date = first_entry_date(ENTRY_TITLE)
find_number_of_entry_every_day(ENTRY_TITLE, first_date)
    
    