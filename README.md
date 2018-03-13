# Deep Learning
## Introduction
Le deep learning est un champ d’étude similaires aux machines learning . Il comporte la conception, l’analyse et le développement de méthodes permettant à des machines d’évoluer par un processus systémique dans le but de remplir des tâches complexes impossibles à réaliser par des algorithmes classiques.
### Spécificités 
Là ou le Deep Learning diffère de son cousin le Machine learning c’est sur la quantité de données et la manière de la traiter.
Un algorithme de machine learning chercher avant tout à trouver des corrélations entre des variables, après le traitement d’un certain nombre d’informations va avoir tendance à plafonner en matière de performance.
Un algorithme de deep learning va en revanche s’améliorer de façon exponentielle avec le nombre de données. Ils ont tendance à être moins dirigé. Ils adoptent une démarche de type **réseau neuronal**.
Il y a également une différence au niveau du résultat, les algorithmes de type machine learning produisent toujours un résultat numérique comme un score ou une classification.
Ceux du Deep Leerning sont plus variés, du texte, des images etc.

## Réseau de neurones:

Domaine du machine Learning visant à construire des modèles paramétriques, c'est à dire un modèle avec une fonction de décision explicite. Il s'agit ni plus ni moins d'un automate avec des données d'entrés pondérées et une fonction de transfert adaptée.
Un réseau de neurones est organisé en couches:
* Une couche d'entrée qui reçoit la donnée
* Une couche Caché qui traite la donnée
* Une couche de sortie qui expose le résultat

Ces couches sont des successions de neurones connectés entre eux chaque connection dispose d'une valeur représentant un poids. Cette notion sera utile plus tard pour calculer un neurone.

L'une des caractéristiques principale d'un réseau de neurones est la capacité d'apprentissage. Il en existe 3 types.
* L'apprentissage supervisé
* L'apprentissage non-supervisé
* L'apprentissage par renforcement

### Neurones

Dans le cas présent, nous allons étudier le neurone produit scalaire aussi appelé **Perceptron**. Un perceptron est représenté graphiquement par un cercle et comporte une valeur numérique. Pour calculer un Perceptron il faut multiplier par son poids et l'ajouter aux perceptrons adjacent.
Chaque perceptron dispose d'un faux neurone qui est constitué d'une constante, il faut l'ajouter au résultat précédant. Cette constante servira pour plus tard pour l'apprentissage. Et pour terminer une **fonction d'activation** qui prend en valeur le résultat du calcul cité précédemment.

### Fonction de seuil

La fonction de seuil est une notion très importante, elle permet d'établir un seuil d'une valeur à partir duquel le neurone sera stimulé ou non. le neurone activé va pouvoir se propager et renforcer un résultat.

### Traitement 
- Traitement en profondeur : L’image est découpée en tuiles. Chaque tuile est traitée par un neurone. Tous les neurones appliquent le même traitement. L’ensemble de ces neurones forme un **noyau de convolution**.
- Généralisation : Les tuiles appelée aussi **champ récepteur** se chevauchent grâces a un décalage entre les champs récepteur. Chaque noyau de convolution représente une strate visant a analyser une caractéristique de l’image. L’empilement de ces strates forme «  la couche de traitement convolutif ». Une couche de convolution traite un volume d’entré pour fournir un volume de sortie.

## Réseau neuronal convolutif

Un réseau de neurones convolutifs est un réseau de neurones qui s’inspire du modèle animal.
* On y retrouve 2 types de neurones :
* Les neurones de traitement, ils se concentrent sur une petite parcelle de l’image ( un champ réceptif)
* Les neurones de mise en commun des sorties (neurone de pooling)

Sans rentrer dans le détail le but de ce réseau de neurone sur une image est de détecter un pattern dans une image cible. Le filtrage consistant a détecter le pattern est une **convolution**. L'idée ici est de faire des convolutions sur différent pattern et d'attribué un poid en fonction du résultat du filtrage , si la cible est proche du pattern ou non. Ensuite une moyenne des convolutions va founrir une valeur. Si cette valeur dépasse un certain seuil alors un pattern est identifié sur l'image.


### Paramétrage 
1. Profondeur de la couche : Il s’agit du nombre de neurones associés a un champ récepteur.
2. Le pas : Définit le chevauchement des récepteurs plus cette valeur est petite plus les récepteurs se chevauchent.
3. La marge ou zero-padding : Permet le contrôle  de la dimension afin d’avoir une surface de sortie équivalente à la surface d'entré.

### Pooling

Le pooling consiste a mettre en commun des portions de l’image (les tuiles) pour créer un sous-échantillonnage. L'intérêt majeur du Pooling est de réduire le temps de traitement de l'image en réduisant la taille des échantillons. Cela va par contre réduire dans une certaine mesure la précision de l'algorithne.

## TensorFlow

TensorFlow est une API de Google servant d’outil au machine learning. Dans le cadre du TP coding game l’application utilise un classifier CNN(Convolutional neural network). L'API google fournit des outils pour créer les différentes couches, mettre en place le pooling etc...

L’application fonctionne en 4 étapes :

1. Injection des données, un tensor placeholder est crée, il s’agit d’un graphe standardisé qui servira a stocker les données.
2. Création du réseau de neurones:
..* Utilisation d’une fonction prédéfini (softmax) pour créer le réseau de neurones.
..* Réduction de l’entropie de l’image (son coté aléatoire).
3. Définition d’un programme d’entraînement
4. Exécution de l’algorithme
