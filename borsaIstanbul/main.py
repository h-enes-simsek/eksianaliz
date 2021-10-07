import pandas as pd
import matplotlib.pyplot as plt

df_eksi = pd.read_csv("borsa-istanbul--3559807.csv", header=None, index_col=0, names=['entry'])
df_eksi.index.name = "Date"
#print(df_eksi)

df_bist = pd.read_csv("bist100.csv", index_col=0)
#print(df_bist)

#günlük değişimi hesapla
df_bist["Change"] =  100* ( ( df_bist["Close"] - df_bist["Open"] ) / df_bist["Open"] ) 
#print(df_bist)

#sadece change column kalsın
df_bist_change = df_bist[['Change']]
#print(df_bist_change)

#verisetlerinin indexlerini datetime olarak düzenle
df_eksi.index = pd.to_datetime(df_eksi.index, format='%Y-%m-%d')
df_bist_change.index = pd.to_datetime(df_bist_change.index, format='%Y-%m-%d')

#iki verisetinin tarihlerini kullarak birleştir
#ortak tarihli veriler ile yeni bir veriseti oluşturuldu.
merged = pd.merge_asof(df_eksi, df_bist_change, left_index=True, right_index=True, direction='nearest')
print(merged)

#korelasyon
print("\ngenel korelasyon")
print(merged.corr(method ='pearson'))

#ancak pozitif ve negatif değişimi ayrı ayrı incelemek daha doğru olabilir.
df_bist_change_p = df_bist_change[df_bist_change.Change>0]
#print(df_bist_change_p)

df_bist_change_n = df_bist_change[df_bist_change.Change<0]
#print(df_bist_change_n)

merged_p = pd.merge_asof(df_eksi, df_bist_change_p, left_index=True, right_index=True, direction='nearest')
merged_n = pd.merge_asof(df_eksi, df_bist_change_n, left_index=True, right_index=True, direction='nearest')

#korelasyon
print("\npozitif değişim için korelasyon")
print(merged_p.corr(method ='pearson'))
print("\nnegatif değişim için korelasyon")
print(merged_n.corr(method ='pearson'))

#plot
merged.plot(x ='Change', y='entry', kind = 'scatter')
plt.savefig("change-entry.png")
plt.show()







