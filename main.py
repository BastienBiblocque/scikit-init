import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chemin vers le fichier CSV
chemin_fichier = "./data_sets/bodyPerformance.csv"

data = pd.read_csv(chemin_fichier)
# tableau_assoc = data.to_dict(orient='records')


# ages = [personne['age'] for personne in tableau_assoc]
# age_moyen = sum(ages) / len(ages)

# print(f"L'âge moyen est : {age_moyen:.2f} ans")


# variables_physiques = ['height_cm', 'weight_kg', 'body fat_%', 'gripForce', 'sit and bend forward_cm', 'sit-ups counts', 'broad jump_cm']
#
# # Calculer la matrice de corrélation
# correlation_matrix = data[variables_physiques].corr()

# # Afficher la matrice de corrélation avec seaborn
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
# plt.title("Matrice de corrélation entre les variables physiques")
# plt.show()


# Créer un graphique de dispersion avec seaborn
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='height_cm', y='weight_kg', hue='gender', data=data, s=100)
# plt.title("Relation entre la taille, le poids et le genre")
# plt.xlabel("Taille (cm)")
# plt.ylabel("Poids (kg)")
# plt.legend(title='Genre')
# plt.show()


plt.figure(figsize=(14, 6))

# Comparaison de la taille entre les genres
plt.subplot(1, 3, 1)
sns.boxplot(x='gender', y='height_cm', data=data)
plt.title("Comparaison de la taille entre les genres")

# Comparaison du poids entre les genres
plt.subplot(1, 3, 2)
sns.boxplot(x='gender', y='weight_kg', data=data)
plt.title("Comparaison du poids entre les genres")

# Comparaison du pourcentage de graisse corporelle entre les genres
plt.subplot(1, 3, 3)
sns.boxplot(x='gender', y='body fat_%', data=data)
plt.title("Comparaison du pourcentage de graisse corporelle entre les genres")

plt.tight_layout()
plt.show()