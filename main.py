import pandas as pd
from statistics import mode # Импортируем удобную штуку - https://docs.python.org/3/library/statistics.html

# Загрузка датасета
titanic = pd.read_csv('titanic.csv')

# Отображение статистики по числовым признакам
print(titanic.describe())

# Отображение статистики по нечисловым признакам
print(titanic.describe(include=['O']))

# Определение количества пассажиров
print('Количество пассажиров на борту:',len(titanic)) # Как я понял , len пробегается по индексу https://docs.python.org/3/library/functions.html#len

# Определение среднего возраста пассажиров
print('Средний возраст пассажиров на борту :',titanic['Age'].mean()) 

# Определение медианного возраста пассажиров
print('Медианный возраст пассажиров на борту :',titanic['Age'].median())

# Определение моды возраста пассажиров
print('Мода возраста пассжиров на борту:',mode(titanic['Age'])) # наша библиотека statistics нам помогла

# Определение среднего количества братьев/сестер на борту
print('Вывод среднего количества братьев/сестер на борту:',titanic['SibSp'].mean())

# Определение среднего количества родственников на борту
print('Вывод среднего количества родственников на борту:',titanic['SibSp'].mean() + titanic['Parch'].mean())

survived_passengers = titanic['Survived'].sum()
print('Количество выживших пассажиров: {survived_passengers}')

died_passengers = len(titanic) - survived_passengers
print('Количество погибших пассажиров: {died_passengers}')

passengers_by_class = titanic['Pclass'].value_counts()
print('Количество пассажиров по классам:')
print(passengers_by_class)

mean_fare_by_class = titanic.groupby('Pclass')['Fare'].mean()
print('Средняя цена билета для каждого класса:')
print(mean_fare_by_class)

mean_fare_by_sex = titanic.groupby('Sex')['Fare'].mean()
print('Средняя цена билета для каждого пола:')
print(mean_fare_by_sex)

total_passengers_with_relatives = titanic[(titanic['SibSp'] > 0) | (titanic['Parch'] > 0)]['PassengerId'].count() # .count возвращает нам сколько встречается тот или иной элемент в списке
print('Количество пассажиров, путешествовавших вместе с родственниками: {total_passengers_with_relatives}')

mean_fare_for_survivors = titanic[titanic['Survived'] == 1]['Fare'].mean()
print('Средняя цена билета для выживших пассажиров: {mean_fare_for_survivors}')

null_counts = titanic.isnull().sum() # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html
print('Количество пустых значений в каждой колонке:')
print(null_counts)
# 17 пункт
mean_age = titanic['Age'].mean()
titanic['Age'].fillna(mean_age, inplace=True)
# 18 пункт
titanic['FamilySize'] = titanic['SibSp'] + titanic['Parch'] + 1  # +1 для учета самого пассажира



# 19 пункт
most_common_port = titanic['Embarked'].value_counts().idxmax()
if most_common_port == 'S' :
    print("Самый популярный порт отправления: Southampton")
if most_common_port == 'Q' :
    print('Самый популярный порт отправления: Queenstown')
if most_common_port == 'C' :
    print('Самый популярный порт отправления: Cherbourg')







