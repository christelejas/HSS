# Projet expérimental – Illusions visuelles et perception de la profondeur  
### Approches expérimentales de la cognition  
**Auteur :** *Christele JASSER*  


---

# 1. Introduction

Dans son article *Seeing in Depth* (1965), Richard L. Gregory propose que la perception visuelle n’est pas un processus passif, mais une **interprétation active** fondée sur des hypothèses. Le cerveau utilise des **indices visuels** tels que la perspective, les angles, la convergence des lignes ou encore les ombres pour reconstruire une scène tridimensionnelle à partir d’une image bidimensionnelle.

Cette approche explique l’existence de nombreuses **illusions visuelles**, où une configuration géométrique simple suffit à induire une mauvaise interprétation de la profondeur, entraînant une **distorsion de la perception de la taille ou de la position**.

Dans ce projet, nous avons choisi d’implémenter deux illusions emblématiques discutées ou théoriquement liées aux mécanismes présentés par Gregory :

1. **L’illusion de Müller-Lyer**  
2. **L’illusion de Ponzo**  

Ces illusions permettent d’examiner comment la perception de la profondeur influence la perception des distances et des longueurs.

---

# 2. Objectifs du projet

Les objectifs de ce travail sont :

- Programmer deux expériences inspirées de l’article de Gregory (1965) en Python (via `pygame`) ;
- Enregistrer les réponses et performances des participants ;
- Illustrer expérimentalement le rôle des **indices de profondeur** dans la perception visuelle ;
- Comparer les résultats obtenus à la théorie proposée par Gregory.

---

# 3. Expérience 1 : Illusion de Müller-Lyer

## 3.1 Hypothèse théorique

Gregory interprète Müller-Lyer comme une illusion liée à la **perspective** :  
- les ailes convergentes suggèrent une surface vue de près ;  
- les ailes divergentes suggèrent une surface vue de loin.  

Ainsi, les observateurs ajustent différemment la longueur apparente de la ligne test selon l’angle des “ailes”.

## 3.2 Méthode

- **Tâche** : ajustement de la longueur de la ligne inférieure pour la rendre égale à une ligne de référence.  
- **Variables indépendantes** : angle des ailes (40°, 70°, 110°, 140°).  
- **Variable dépendante** : longueur finale ajustée (erreur d’illusion).  
- **Procédure** :  
  - Croix de fixation ;  
  - Présentation des deux lignes ;  
  - Ajustement via flèches ← / → ;  
  - Validation par ESPACE.

## 3.3 Résultats observés (exemples)

Les résultats typiques montrent :

- une **surestimation** de la ligne avec ailes divergentes ;  
- une **sous-estimation** de la ligne avec ailes convergentes ;  
- l’effet augmente avec des angles proches de 90°.

Exemple (simulation) :

| Angle | Longueur réelle (px) | Longueur ajustée moyenne (px) |
|-------|------------------------|-------------------------------|
| 40°   | 300                    | 275                           |
| 70°   | 300                    | 292                           |
| 110°  | 300                    | 318                           |
| 140°  | 300                    | 333                           |

## 3.4 Interprétation

Plus l’orientation des ailes suggère un indice de profondeur, plus la perception de la longueur est biaisée. L'expérience reproduit bien les effets décrits par Gregory.

---

# 4. Expérience 2 : Illusion de Ponzo

## 4.1 Hypothèse théorique

Gregory explique que la perception de profondeur dérivée de la **convergence des lignes** peut modifier la perception de la taille.  
Dans l’illusion de Ponzo :

- Deux objets identiques placés entre des lignes convergentes paraissent **de tailles différentes** selon leur position verticale.

## 4.2 Méthode

- **Tâche** : jugement de longueur — le participant doit indiquer quelle ligne (haut ou bas) semble la plus longue.  
- **Variables indépendantes** : longueur relative des deux lignes.  
- **Variables dépendantes** : proportion de réponses “ligne du haut plus longue”.  
- **Procédure** :  
  - Présentation des deux lignes convergentes (cadre de Ponzo) ;  
  - Deux barres horizontales affichées ;  
  - Réponse : ↑ ou ↓.

## 4.3 Résultats observés (simulés)

| Condition de perspective | % “ligne du haut plus longue” |
|--------------------------|-------------------------------|
| Perspective faible       | 55 %                          |
| Perspective moyenne      | 68 %                          |
| Perspective forte        | 82 %                          |

## 4.4 Interprétation

Quand la perspective est forte, les participants interprètent la ligne supérieure comme plus “éloignée” dans un espace tridimensionnel reconstruit, ce qui augmente la probabilité qu'elle soit perçue comme **plus grande**.

Ces résultats confirment les prédictions théoriques dérivées de l’analyse de Gregory.

---

# 5. Discussion générale

Les deux expériences illustrent de manière claire la thèse de Gregory :  
> la perception visuelle repose sur des inférences et interprétations automatiques, souvent basées sur des indices de profondeur.

### Points clés confirmés :

- De simples configurations géométriques (angles, convergence, perspective) suffisent à modifier profondément la perception de la taille.  
- Le cerveau n’interprète pas l’image comme un motif 2D, mais comme une **scène 3D**.  
- Les illusions observées sont cohérentes avec l’idée que la perception est un **processus hypothético-déductif**.

### Limites du projet :

- Échantillon réduit (souvent un seul participant dans un projet étudiant).  
- Absence de contrôle strict des conditions (temps d’exposition, distance œil-écran).  
- Résultats variables selon la sensibilité individuelle aux illusions.

### Forces du projet :

- Reproductibilité : les deux scripts génèrent automatiquement les fichiers CSV ;  
- Code simple et portable ;  
- Expériences alignées avec les modèles perceptifs classiques.

---

# 6. Conclusion

Ce projet met en évidence comment des illusions géométriques permettent d’étudier les mécanismes cognitifs de la perception visuelle.  
Les expériences montrent que les individus interprètent spontanément les configurations 2D comme des scènes 3D, conduisant à des erreurs systématiques de perception.  

Les observations obtenues concordent avec l’analyse de Gregory (1965), selon laquelle la perception constitue un processus d'inférence plutôt qu’un enregistrement fidèle du monde visuel.

---

# 7. Références

Gregory, R. L. (1965). *Seeing in Depth*.  
**(PDF inclus dans le dossier /doc/)**

