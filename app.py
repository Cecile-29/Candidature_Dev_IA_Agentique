import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# 💡 NOTE ft px.pie
# 'values' et 'names' sont des paramètres spécifiques à la fonction px.pie de PLOTLY.
# Paramètres interprétable par la lecture du tableau par la bibliothèque PANDAS, 
# et la création de la data des colonnes nommées 'qte', 'region' ou 'produit' que Plotly peut cibler.

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')



# a. Les ventes par produit reprend la fonction de visualisation des ventes par région ci-dessus
# ==============================================================================================

# values='qte' : calcule la taille des parts selon le nombre d'unités vendues
# names='produit' : la donnée du tableau ventes.csv 'produit' est l'item de partage du graphique.

figure_ventes_produit = px.pie(données, values='qte', names='produit', title='Quantités vendues par produit')

figure_ventes_produit.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')



# b. Le chiffre d'affaires par produit 
# ====================================


# Le paramètre values='chiffre_affaires' doit quantifier les parts de chaque produit selon l'argent généré.
# Son calcul est le (prix * quantité) pour chaque ligne

données['chiffre_affaires'] = données['prix'] * données['qte']

# Dans la déclaration les crochets [''] servent à cibler ou créer une colonne précise dans le tableau.
# Pandas multiplie les colonnes 'prix' et 'qte' ligne par ligne,
# et crée une nouvelle colonne appelée 'chiffre_affaires' pour stocker les résultats.

figure_chiffre_affaires_produit = px.pie(données, values='chiffre_affaires', names='produit', title="Chiffre d'affaires par produit")
# Le pramètre names='produit' : segmente le graphique par type de produit (A, B, C) et affiche le chiffre d'affaires par produit.
figure_chiffre_affaires_produit.write_html('chiffre-affaires-par-produit.html')
print('chiffre-affaires-par-produit.html généré avec succès !')
