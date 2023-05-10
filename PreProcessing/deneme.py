import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

train = pd.read_csv('out.csv')


print(train.head())


main_train = train[['key', 'mode', 'danceability', 'energy','loudness','acousticness', 'speechiness','instrumentalness','liveness','tempo', 'valence', 'duration_ms', 'time_signature', 'popularity' ]]



#verilerin figür olarak gösterimi için
fig1, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

ax0.hist(main_train['key'],bins=10,rwidth=5,color='red')
ax0.set_title('Perde Sınıfı',loc = 'left', fontsize = 10)
ax0.set_xlabel('Değer',fontsize=8)
ax0.set_ylabel('Şarkı Sayısı',fontsize=8)
'''
Parçanın içinde bulunduğu anahtar.
Tamsayılar, standart Pitch Class (Perde Sınıfı)
gösterimini kullanarak perdelere eşlenir.
Örneğin. 0 = C, 1 = C♯/D♭, 2 = D, vb.
Herhangi bir anahtar algılanmadıysa, değer -1'dir.
'''

ax1.hist(main_train['danceability'],bins=100,rwidth=1,color='blue')
ax1.set_title('Dans Edilebilirlik',loc = 'left', fontsize = 10)
ax1.set_xlabel('Değer',fontsize=8)
ax1.set_ylabel('Şarkı Sayısı',fontsize=8)
'''
Tempo, ritim istikrarı,
vuruş gücü ve genel düzenlilik gibi müzik
öğelerinin bir kombinasyonuna dayalı olarak
bir parçanın dans etmek için ne kadar uygun
olduğunu tanımlar. 0.0 değeri en az 
dans edilebilir ve 1.0 en çok dans edilebilir 
değerdir.
'''

ax2.hist(main_train['energy'],bins=100,rwidth=1,color='green')
ax2.set_title('Enerji',loc = 'left', fontsize = 10)
ax2.set_xlabel('Değer',fontsize=8)
ax2.set_ylabel('Şarkı Sayısı',fontsize=8)
'''
0.0 ile 1.0 arasında bir ölçüdür
ve algısal bir yoğunluk ve aktivite ölçüsünü
temsil eder. Tipik olarak, enerjik parçalar hızlı,
yüksek sesli ve gürültülü hissettirir.
Örneğin, dead metal yüksek enerjiye sahipken,
bir Bach başlangıcı ölçekte düşük puanlar alır.
Bu özelliğe katkıda bulunan algısal özellikler,
dinamik aralık, algılanan ses yüksekliği, tını, 
başlangıç hızı ve genel entropiyi içerir.

'''


ax3.hist(main_train['acousticness'],bins=10,rwidth=5,color='yellow')
ax3.set_title('Fare',loc = 'left', fontsize = 10)
ax3.grid(True)
ax3.set_xlabel('Değer',fontsize=8)
ax3.set_ylabel('Şarkı Sayısı',fontsize=8)
#500 ödeyen 10 kişi


fig1.suptitle('Şarkı Özelliklerinin Gösterimi')
fig1.tight_layout()
plt.show()


from sklearn.model_selection import train_test_split

X = main_train.drop(['popularity'], axis=1)
y = main_train['popularity']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)


from sklearn.tree import DecisionTreeClassifier
#gini indeksi ile DecisionTreeClassifier modeli oluşturuyoruz.
#max depth karar ağacındaki derinlik sayımız
clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=10,min_samples_leaf=8)
#gini classifier fitliyoruz train ile
clf_gini.fit(X_train, y_train)
#predict ediyoruz
y_pred_gini = clf_gini.predict(X_test)

#x test verilerimizle tahmin yaptıp
#y test verilerimize tahmin ettiriyorruz
from sklearn.metrics import accuracy_score
print('Gini ile modelin doğruluğu: {0:0.8f}'. format(accuracy_score(y_test, y_pred_gini)))
y_pred_train_gini = clf_gini.predict(X_train)
print('Train set ile doğruluk oranı: {0:0.8f}'. format(accuracy_score(y_train, y_pred_train_gini)))

from sklearn import tree
fig3 = plt.figure(figsize=(12,8))
features = X_train.columns
tree.plot_tree(clf_gini.fit(X_train, y_train),feature_names=features,filled=True)
fig3.suptitle('Gini Karar Agacı', fontsize=20)
plt.show()