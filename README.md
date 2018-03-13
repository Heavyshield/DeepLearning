# Deep Learning
## Introduction

# Deep Learning
## Introduction
Le deep learning est un champ d’études similaires aux machines learning . Il comporte la conception, l’analyse et le développement de méthodes permettant à des machines d’évoluer par un processus systémique dans le but de remplir des tâches complexes impossibles à réaliser par des algorithmes classiques.
Spécificité 
Là ou le Deep Learning diffère de son cousin le Machine learning c’est sur la quantité de donnée et la manière de la traiter.
Un algorithme de machine learning chercher avant tout à trouver des corrélations entre des variables, après le traitement d’un certain nombre d’informations va avoir tendance à plafonner en matière de performance.
Un algorithme de deep learning va en revanche s’améliorer de façon exponentielle avec le nombre de données. Ils ont tendance à être moins dirigé. Ils adoptent une démarche de type **réseau neuronal**.
Il y a également une différence au niveau du résultat, les algorithmes de type machine learning produisent toujours un résultat numérique comme un score ou une classification.
Ceux du Deep Leerning sont plus variés, du texte, des images etc.

## Réseau de neurones:

Domaine du machine Learning visant à construire des modèles paramétriques, c'est à dire un modèle avec une fonction de décision explicite. Il s'agit ni plus ni moins d'un automate avec des données d'entrés pondérées et une fonction de transfert adaptée.


## Réseau neuronal convolutif

Un réseau de neurones convolutifs est un réseau de neurones qui s’inspire du modèle animal.
On y retrouve 2 types de neurones :
* Les neurones de traitement, ils se concentrent sur une petite parcelle de l’image ( un champ réceptif)
* Les neurones de mise en commun des sorties (neurone de pooling)

### Le traitement :

- traitement en profondeur : L’image est découpée en tuiles. Chaque tuile est traitée par un neurone. Tous les neurones appliquent le même traitement. L’ensemble de ces neurones forme un noyau de convolution.

- Généralisation : Les tuiles appelée aussi champ récepteur se chevauchent gracent a un décalage entre les champs récepteur. Chaque noyaux de convolution représente une strate visant a analyser une caractéristique de l’image. L’empilement de ces strates forme «  la couche de traitement convolutif ». Une couche de convolution traite un volume d’entré pour fournir un volume de sortie.

### Paramétrage :
1. Profondeur de la couche : Il s’agit du nombre de neurones associés a un champ récepteur.
2. Le pas : Définit le chevauchement des récepteurs plus cette valeur est petite plus les récepteur se chevauchent.
3. La marge ou zero-padding : Permet le contrôle  de la dimension afin d’avoir un surface de sortie équivalente a c’elle en entré.

### Pooling

Le pooling consiste a mettre en commun des portions de l’images (les tuiles) pour créer un sous-échantillonnage.

## TensorFlow

TensorFlow est une API de Google servant d’outil au machine learning. Dans le cadre du TP coding game l’application un classifier CNN(Convolutional neural network).

L’ application fonctionne en 4 étapes :

1. Injection des données, un tensor placeholder est crée, il s’agit d’un graphe standardisé qui servira a stocker les données.
2. Création du réseau de neurone :
.* Utilisation d’une fonction prédéfini (softmax) pour créer le réseau de neurones.
.* Réduction de l’entropie de l’image (son coté aléatoire).
3. Définition d’un programme d’entrainement
4. Exécution de l’algorithme

#