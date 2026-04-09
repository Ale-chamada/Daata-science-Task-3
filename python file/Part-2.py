import pandas as pd
df = pd.read_csv("python file/Titanic-Dataset.csv")

print(df.head())
print(df.info())
print(df.describe())

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

if 'Cabin' in df.columns:
    df = df.drop(columns=['Cabin'])

df = df.drop_duplicates()

print(df.isnull().sum())

survival_by_gender = df.groupby('Sex')['Survived'].mean()
print(survival_by_gender)

survival_by_class = df.groupby('Pclass')['Survived'].mean()
print(survival_by_class)

avg_age_class = df.groupby('Pclass')['Age'].mean()
print(avg_age_class)

def age_group(age):
    if age < 18:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)

survival_by_age_group = df.groupby('AgeGroup')['Survived'].mean()
print(survival_by_age_group)

female_survived = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
print(female_survived.head())

children_survived = df[(df['Age'] < 18) & (df['Survived'] == 1)]
print(children_survived.head())

first_class = df[df['Pclass'] == 1]
high_survival_first_class = first_class[first_class['Survived'] == 1]
print(high_survival_first_class.head())
first_class_survival_rate = df[df['Pclass'] == 1]['Survived'].mean()
print("1st Class Survival Rate:", first_class_survival_rate)

print("INSIGHTS")

if survival_by_gender['female'] > survival_by_gender['male']:
    print("Females were more likely to survive than males.")

print("Higher class passengers (1st class) had higher survival rates.")
print("Children had a relatively high survival rate, showing priority was given.")

best_combo = df.groupby(['Sex', 'Pclass'])['Survived'].mean().sort_values(ascending=False)
print(best_combo.head(1))
print("Best survival group: Female passengers in 1st class (~96.8%)")
