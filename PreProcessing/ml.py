import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

train = pd.read_csv('out.csv')

main_train = train[['key', 'mode', 'danceability', 'energy','loudness','acousticness', 'speechiness','instrumentalness','liveness','tempo', 'valence', 'duration_ms', 'time_signature', 'popularity' ]]


from sklearn.model_selection import train_test_split

X = main_train.drop(['popularity'], axis=1)
y = main_train['popularity']

print(X.shape)
print(y.shape)

model = LinearRegression()

if X.shape[0] != y.shape[0]:
  print("X and y rows are mismatched, check dataset again")


model.fit(X, y)

r_sq = model.score(X, y)
print(f"coefficient of determination: {r_sq}")
#belirleme katsayısı: 0.10639885762892876


#.score()'u uyguladığınızda, bağımsız değişkenler
#  aynı zamanda x yordayıcısı ve y yanıtıdır ve
#  dönüş değeri 𝑅²'dir.

print(f"intercept: {model.intercept_}")



print(f"coefficients: {model.coef_}")

'''
𝑅² değerini .score() kullanarak
ve regresyon katsayılarının tahmin edicilerinin değerlerini
.intercept_ ve .coef_ ile elde edersiniz.
Yine, .intercept_ önyargıyı 𝑏₀ tutarken artık
.coef_ 𝑏₁ ve 𝑏₂ içeren bir dizidir.
Bu örnekte, kesme yaklaşık olarak 5,52'dir
ve bu, 𝑥₁ = 𝑥₂ = 0 olduğunda tahmin edilen yanıtın
değeridir. 𝑥₁'nın 1 artması, tahmin edilen yanıtın
 0,45 yükselmesini sağlar. Benzer şekilde, 𝑥₂ 1 büyüdüğünde yanıt 0,26 artar.
'''



