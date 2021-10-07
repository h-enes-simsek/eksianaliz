# Ekşi Analiz
Ekşisözlükte, belirli bir başlıktaki entrylerin yazıldığı günlere göre dağılımını bulan program.

## Algoritma
1-İlk entrynin yazıldığı günü bul.
2-İlk entrynin yazıldığı günden itibaren bir artarak her bir gün yazılan entrylerin olduğu sayfaya git.
örneğin: https://eksisozluk.com/borsa-istanbul--3559807?day=2021-10-03
Not: Bugün hariç, çünkü bugün hala entry girilebilir, veri toplamak anlamlı olmayabilir.
3-Toplam kaç sayfa olduğunu bul, tüm sayfalardaki entry sayılarını topla
4-Her bir gün için toplam entry sayısını hesapla.
5-Her günün ardından verileri bir csv dosyasına yaz (append)

## TODO
1-Başlangıçtan itibaren her seferinde bir sonraki günü kontrol etmek çok uzun.
Bunun yerine ekşideki sıra ile her bir sayfa bilgisayara kaydedilip, 
sayfadaki tarihler tek tek parse edilerek iş yükü azaltılabilir. 
2-Her sayfa başına gösterilen max entry limiti tarayıcı özelliklerine göre değişiyor.
Şu an ekşisözlük sayfa başına 10 entry gösteriyor. Ama bir laptop ile 25 entry görülebiliyor.
Muhtemelen HTTP headerlerı ile max limit artırılarak daha az istekle veriler toplanabilir. 

## Borsa İstanbul 
Ekşisözlükteki borsa istanbul başlığına yazılan entrylerin günlere göre dağılımı ile borsa istanbulun günlük değer değişimi arasındaki ilişkiyi inceledim.


