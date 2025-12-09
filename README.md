# Projet – Illusions visuelles et perception de la profondeur (Gregory, 1965)

Ce dépôt contient **deux expériences comportementales** implémentées en Python (compatibles Python 3.12, via `pygame`), inspirées de l’article de R. L. Gregory (1965), *Seeing in Depth*.  
Elles illustrent comment certains **indices visuels** comme les angles, convergence des lignes et perspective, influencent la **perception de la taille** et de la **profondeur**.

Les deux illusions implémentées sont :
- **Müller-Lyer** (ajustement de longueur)
- **Ponzo** (comparaison de longueurs)

*Lorsque vous lancez une expérience, le programme vous demande en input dans la console d’entrer le nom du fichier où enregistrer les résultats.*



## Description des expériences et objectif du projet

Dans son article *Seeing in Depth* (1965), Richard L. Gregory propose que la perception visuelle n’est pas un processus passif, mais une **interprétation active** fondée sur des hypothèses. Le cerveau utilise des **indices visuels** tels que la perspective, les angles, la convergence des lignes ou encore les ombres pour reconstruire une scène tridimensionnelle à partir d’une image bidimensionnelle.

Cette approche explique l’existence de nombreuses **illusions visuelles**, où une configuration géométrique simple suffit à induire une mauvaise interprétation de la profondeur, entraînant une **distorsion de la perception de la taille ou de la position**.

Dans ce projet, nous avons choisi d’implémenter deux illusions emblématiques discutées ou théoriquement liées aux mécanismes présentés par Gregory :

1. **L’illusion de Müller-Lyer**  
2. **L’illusion de Ponzo**  

Ces illusions permettent d’examiner comment la perception de la profondeur influence la perception des distances et des longueurs.

---

## Expérience 1 : Illusion de Müller-Lyer

### Objectif
Étudier comment l’orientation des “ailes” modifie la perception de la longueur d’une ligne.  
L’illusion montre que notre cerveau interprète certaines configurations comme un indice de **profondeur**, ce qui fausse la perception de la taille.

### Déroulement
- Une ligne de référence est affichée.
- Le participant doit ajuster une seconde ligne pour qu’elle semble de même longueur.
- Les ailes **convergentes** ou **divergentes** modifient la perception :
  - Ailes divergentes → ligne perçue comme **plus longue**  
  - Ailes convergentes → ligne perçue comme **plus courte**

Le but est de mesurer **l’erreur d’illusion**, c’est-à-dire l’écart entre la vraie longueur et la longueur ajustée.

---

## Expérience 2 : Illusion de Ponzo

### Objectif
Montrer comment la **perspective** influence la perception de la taille : deux lignes identiques semblent différentes lorsqu’elles sont placées dans un cadre convergent (comme des rails qui se rapprochent).

### Déroulement
- Deux lignes horizontales identiques sont affichées.
- Elles sont placées dans un cadre dont les lignes convergent vers le haut.
- Le participant doit indiquer laquelle semble la plus longue.
- Typiquement :
  - La ligne en haut paraît **plus grande**, car elle semble “plus loin” dans la perspective.

Le but est d’étudier l’effet de profondeur apparente sur le jugement de longueur.

---

##  Pourquoi ces expériences ?

Ces deux illusions démontrent un point central de la psychologie perceptive :

###  Notre cerveau utilise automatiquement des indices de profondeur pour interpréter les images en 3D.  
Mais cette stratégie entraîne parfois des **erreurs systématiques**, révélées par les illusions.

Les expériences permettent :
- d'observer concrètement ces erreurs,
- de mesurer leur intensité,
- de relier les résultats aux modèles cognitifs de Gregory.



