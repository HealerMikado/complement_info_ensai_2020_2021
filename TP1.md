# TP 1 : Retour sur le POO, objets métier et patron de conception *strategy*

## 1 Introduction

Dans ce TP nous allons mettre en place la partie *Personnage* de notre jeu en console. Les *personnages* sont des **objets métier** de notre application. Ils représentent informatiquement quelque chose de concret.

> :book:**Objet métier (business objet)** : représentation informatique d'un objet "réel" que notre programme va manipuler pour répondre à un besoin. Dans le cas de notre application les personnage et les monstres sont des objets métier, ainsi que les équipements du personnage. Dans une application de e-commerce, les articles et comptes sont des objet métier également.

Avant d'implémenter (coder) nos objets métiers nous allons un peu réfléchir à la meilleure façon de faire.

Git clone (TODO)

## 2 Modélisation

Avant de coder nous allons réfléchir à la meilleure conception possible pour réaliser nos personnages. Notre conception essayera au maximum de respecter la règle suivante : **forte cohésion, faible couplage**. En d'autre termes nous allons essayer de faire des classes les plus disjointes possible pour qu'une modification dans une classe ne nous demande pas de modifier les autre tout en essayant d'avoir les tâches réalisées pas une seule classe le plus lié possible.

> :sparkles: ​ Il faut garder en permanence cette règle en tête

### 2.1 Typons nos personnage par héritage

Nous savons que notre jeu doit proposer 3 types de personnage, Magicien, Voleur et Guerrier. Nous pourrions modéliser notre personnage de cette façon, avec type qui pourra prendre les valeurs magicien, guerrier, voleur.

```mermaid
classDiagram
	class Personange {
	+String personnage_type
	+String combat()
	}
```

Voilà le code python associé

```python
MAGICIEN = "magicien"
GUERRIER = "guerrier"
VOLEUR = "voleur"

class Personnage:
    def __init__(self, personnage_type):
        self.type = personnage_type
```

#### Exercice 1 :

 - Codez la méthode attaque(personnage) dans la classe PersonnageService qui prend en paramètre un personne et retourne :
   - "Lance une boule de feu" si le personnage à pour type magicien ;
   - "Donne un coup d'épée" si le personnage à pour type guerrier ;
   - "Tire à l'arc" si le personne à pour type voleur
- Codez la méthode defense(personnage) dans la classe PersonnageService qui prend en paramètre un personne et retourne :
  - "Utilise une barrière magique" si le personnage à pour type magicien ;
  - "Pare avec son bouclier" si le personnage à pour type guerrier ;
  - "Esquive adroitement l'attaque" si le personne à pour type voleur
- Testez votre code en utilisant la classe test_personnage_service. Pour cela il vous suffit de lancer les testes de la classe avec le bouton "play" au niveau de la classe. Si vous avez bien fait les points précédent 3 test doivent être en erreur. Corrigez-les pour avoir tout vos tests au vert.


<!--
````python
def combat(personnage):
    phrase = ''
    if personnage.type == MAGICIEN:
        phrase = "Lance une boule de feu"
    elif personnage.type == GUERRIER:
        phrase = "Donne un coup d'épée"
    elif personnage.type == VOLEUR:
        phrase = "Tire à l'arc"
    return phrase
````
-->

Maintenant imaginons que dans une mise à jour de notre jeu nous voulons ajouter 10 nouveaux types de personnage. Cela nous demande d'aller mettre à jour tous nos blocs *if/elif/else*. Actuellement nous en avons uniquement 2, un pour attaquer et un pour défendre, mais on peut imaginer avoir plus de comportement spécifique. Avec l'assurance d'en oublier. Et donc d'avoir des bugs. Cela crée donc un fort **couplage** entre notre classe personnage et les services qui vont l'utiliser.

La bonne solution est donc d'utiliser de l'héritage ! Cela donne le diagramme de classe suivant :

````mermaid
classDiagram
	class Personnage {
	 +String phrase_attaque
	 }
	 
	Personnage <|-- Magicien
	Personnage <|-- Guerrier
	Personnage <|-- Voleur
````

et le code python associé:

````python
class Personnage:
    def __init__(self, phrase_attaque,phrase_defense):
        self.phrase_attaque = phrase_attaque
        self.phrase_defense = phrase_defense
        
class Magicien(Personnage):
    def __init(self):
        super().__init__("Lance une boule de feu","Utilise une barrière magique" )
       
class Guerrier(Personnage):
    def __init(self):
        super().__init__("Donne un coup d'épée","Pare avec son bouclier"  )
        
class Voleur(Personnage):
    def __init(self):
        super().__init__("Tire à l'arc","Esquive adroitement l'attaque" )
````

Maintenant pour avoir l'effet d'une attaque il suffit d'appeler l'attribut phrase_attaque du personnage (pareil pour la défense).

````python
def combat(personnage):
    return personnage.phrase_attaque
````

On peut désormais faire autant de personnage que l'on souhaite sans difficulté et risque d'oubli ! Nous allons juste améliorer notre modélisation en créant une méthode "attaque" dans notre personnage. Cette méthode contiendra le code pour calculer les dégât de l'attaque, et retourne un objet AttaqueInfo contenant les dégâts et un texte. 

> :shield: On pourrait faire la même chose avec la défense. Pour alléger les diagrammes nous allons nous concentrer sur l'attaque pour le moment. Nous reviendrons sur la défense à la fin.

> :warning: Note : la flèche avec le label creates doit être en **pointillée**, l'outil que j'utilise refuse de produire la bonne flèche.



````mermaid
classDiagram
	class Personnage {
	 +String phrase_attaque
	 +String phrase_defense
	 +AttaqueInfo attaque()
	 }
	 
	 class AttaqueInfo {
	 +String phrase_attaque
	 +Int degat
	 }
	Personnage <|-- Magicien
	Personnage <|-- Guerrier
	Personnage <|-- Voleur
	Personnage ..> AttaqueInfo  : <<creates>>
````

````python
class Personnage:
    def __init__(self, phrase_attaque,phrase_defense):
        self.phrase_attaque = phrase_attaque
        self.phrase_defense = phrase_defense
        
    def attaque(self):
        """
        Définit le comportement d'une attaque. Doit être implémenté par toutes les classes qui héritent de personnage
        :return: les dégâts purs et le texte de l'attaque dans un objet AttaqueInfo
        :rtype: AttaqueInfo
        """
        pass
        
class Magicien(Personnage):
    def __init(self):
        super().__init__("Lance une boule de feu","Utilise une barrière magique" )
       
    def attaque(self):
        # code pour calculer les dégâts
        return AttaqueInfo(self.phrase, degat)
    
    
class Guerrier(Personnage):
    def __init(self):
        super().__init__("Donne un coup d'épée","Pare avec son bouclier"  )
 
    def attaque(self):
        # code pour calculer les dégâts
        return AttaqueInfo(self.phrase, degat)
        
        
class Voleur(Personnage):
    def __init(self):
        super().__init__("Tire à l'arc","Esquive adroitement l'attaque" )
        
    def attaque(self):
        # code pour calculer les dégâts
        return AttaqueInfo(self.phrase, degat)
````

Voilà une conception souple qui nous permet une évolutivité facile.

### 2.2 Un personnage "pur" n'est-il pas abstrait ?

 On pourrait s'arrêter là mais nous allons allez un cran plus loin en rendant Personnage **abstrait**. Cela signifie que l'on ne pourra pas *instancier* un objet qui aura pour seule classe Personnage. Il faudra forcément instancier un objet d'une classe fille. On va ainsi spécifier qu'un objet Personnage seul n'a pas de sens, et que seule les classes qui héritent de personne en ont. 

Pourquoi faire cela ? Actuellement la méthode attaque ne produit rien dans la classe Personnage. Donc si un objet qui a la classe Personnage venait à être instancié et que l'on appelle attaque, la méthode ne renverrait rien. Ce qui pourrait créer une erreur et faire crasher notre jeu, ou pire permettre un comportement anormal non détecté (typiquement ce qui permet de faire des *bug exploit* dans les jeux vidéo). La solution rapide peut être de remplacer la fonction actuelle par :

```python
class Personnage:
	def attaque(self):
        raise NotImplementedError
```

Si la méthode attaque est appelée sur un objet qui a pour classe Personnage une erreur sera levée que l'on pourra gérer, mais ce n'est pas propre et demande du travail supplémentaire. En plus cela va créer une erreur au *run time* (pendant l'exécution), ce qui ne nous arrange pas. On préfère avoir une erreur au *compile time* (pendant que le code se compile) et donc avant que notre jeu se lance. La bonne méthode est de rentre tout simplement Personnage abstrait, et donc de dire qu'il est impossible d'instancier un objet qui est seulement personnage. En plus on va passer un contrat avec les classes filles en les obligeant de définir la méthode attaque. Voilà la nouvelle modélisation

````mermaid
classDiagram
	class AbstractPersonnage {
	<<abstract>>
	 +String phrase_attaque
	 +String phrase_defense
	 +AttaqueInfo attaque()
	 }
	 
	 class AttaqueInfo {
	 +String phrase_attaque
	 +Int degat
	 }
	Magicien --|> AbstractPersonnage
	Guerrier --|> AbstractPersonnage
	Voleur --|> AbstractPersonnage
	AbstractPersonnage ..> AttaqueInfo  : <<creates>>
````

Et le code associé (je vais me limiter à une seule classe fille):

````python
from abc import ABC, abstractmethod
class AbstractPersonnage(ABC):
    def __init__(self, phrase_attaque, phrase_defense):
        self.phrase_attaque = phrase_attaque
        self.phrase_defense = phrase_defense
       
    @abstractmethod # décorateur qui définit une méthode comme abstraite
    def attaque(self):
        """
        Définit le comportement d'une attaque. Doit être implémenté par toutes les classe qui hérite de personnage
        :return: les dégâts purs et le texte de l'attaque dans un objet AttaqueInfo
        :rtype: AttaqueInfo
        """
        
class Magicien(AbstractPersonnage):
    def __init(self):
        super().__init__("Lance une boule de feu","Utilise une barrière magique" )
       
    def attaque(self):
        # code pour calculer les dégâts
        return AttaqueInfo(self.phrase, degat)
````

> :computer: ​ABC (*Abstract Base Class*) est un module python qui permet de créer des classes abstraites. Une classe abstraite doit hériter de ABC. On définit ensuite les méthodes abstraites avec le décorateur *abstractmethod*. Ces méthodes devront être définies dans les classes filles, sinon python ne permettra pas au programme de se lancer.

En procédant ainsi, et avec un IDE tel que PyCharm, si vous définissez une classe qui hérite d'une classe abstraite, il vous signalera que vous devez implémenter des méthodes provenant de la classe mère, et PyCharm vous permettra de les générer facilement avec un `Ctrl+i` (il vous faudra bien évidement remplir le corps des méthodes)

#### Exercice 2 :

En vous basant sur la modélisation précédente et le code fourni, codez  dans le package personnage et dans des fichiers séparés les classes:

- AbstractPersonnage
- Magicien
- Guerrier
- Voleur



### 2.3 Gestion des statistiques et composition

Nous allons maintenant voir comment gérer les caractéristiques de notre personnage. La solution évidente est de mettre toutes les statistiques comme des attributs de la classe:

````mermaid
classDiagram
	class AbstractPersonnage {
	<<abstract>>
	 +String phrase_attaque
	 +String phrase_defense
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
	 +AttaqueInfo attaque()
	 }
	 
````

Mais est-ce réellement la meilleure solution ? Nous savons déjà que nous voulons proposer une gestion de l'équipement dans notre jeu. Il y a de forte chance que notre équipement influe sur les statistiques du personnage. Donc cela veut dire que l'on risque d'avoir une modélisation de l'équipement qui ressemble à ça :

````mermaid
classDiagram
	class AbstractPersonnage {
	<<abstract>>
	 +String phrase_attaque
	 +String phrase_defense
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
	 +AttaqueInfo attaque()
	 }

class AbstractEquipement {
	<<abstract>>
	 +String nom
	 +int force_bonus
	 +int agilite_bonus
	 +int magie_bonus
	 +int defense_bonus
	 +int point_de_vie_bonus
	 }
````

> :mag: Remarquez que je pars du principe que je vais créer une classe abstraite pour les équipements. Cela ne coûte rien et permet un code évolutif et stable.

Si maintenant nous voulons ajouter une nouvelle caractéristique nous allons devoir l'ajouter dans AbstractPersonnage et dans AbstractEquipement, et potentiellement dans d'autres classes :scream: . Ce qui va sans aucun doute amener à des oublis (surtout si vous développez à plusieurs). La solution est de faire une classe Statistique qui va contenir les différentes statistiques que l'on utilise. On pourra ainsi les utiliser pour nos personnages et pour l'équipement. Et pour cela nos allons utiliser une relation de **composition**

> :book:Une **composition** est une association de type «est composé de» avec une relation de contenance forte. Les vies des objets composants et de l’objet composé sont étroitement liées : ils sont construits et détruits en même temps. Un objet composé ne peut exister sans ses objets composants, et inversement  

Voici le diagramme de classe (tronqué) que l'on obtient

````mermaid
classDiagram
class AbstractPersonnage {
	<<abstract>>
	 +String phrase_attaque
	 +String phrase_defense
	 +AttaqueInfo attaque()
	 }

class AbstractEquipement {
	<<abstract>>
	+String nom
	 }
	 
class Statistique {
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
}

AbstractPersonnage *--"1" Statistique
AbstractEquipement *--"1" Statistique
````

Une partie du code python associé : 

````python
from abc import ABC, abstractmethod
class AbstractPersonnage(ABC):
    def __init__(self, phrase_attaque, phrase_defense, force, agilite, magie, defense, point_de_vie):
        self.phrase_attaque = phrase_attaque
        self.phrase_defense = phrase_defense
        self.statistique = Statistique(force, agilite, magie, defense, point_de_vie)

class Statistique:
    def __init__(self, force, agilite, magie, defense, point_de_vie):
        self.force = force
        self.agilite = agilite
        self.magie = magie
        self.defense = defense
        self.point_de_vie = point_de_vie
````

#### Exercice 3 :

En vous basant sur la modélisation précédente et le code fourni :

- Mettez à jour la classe AbstractPersonnage
- Dans le package business_objet implémentez (codez) la classe Statistique
- Dans le package item implémentez la classe AbstractEquipement

À partir de maintenant on peut ajouter autant de nouvelles statistique qu'on le souhaite, nos personnages et nos équipements y auront accès, plus de risque d'oublie ! :relieved:

### 2.4 Gestion d'équipement et patron de conception *strategy*

Bon maintenant rentrons plus en détail dans la gestion des équipements. Actuellement notre jeu permet un comportement différent en fonction du personnage :

- Le magicien lance des boules de feu
- Le guerrier frappe à l'épée
- Le voleur tire à l'arc

C'est bien, mais ce n'est pas très personnalisable. Notre jeu doit proposer une texte spécifique à chaque équipement. On pourrait alors imaginer une solution comme celle là en utilisant une relation unidirectionnel (le personnage connait l'arme qu'il possède, mais la réciproque est fausse):

````mermaid
classDiagram
class AbstractPersonnage {
	<<abstract>>
	 +AttaqueInfo attaque()
	 }
	 

class AbstractEquipement {
	<<abstract>>
	+String nom
	 }
	 
class Statistique {
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
}


Magicien --|> AbstractPersonnage
Guerrier --|> AbstractPersonnage
Voleur --|> AbstractPersonnage

AbstractPersonnage *--"1" Statistique
AbstractEquipement *--"1" Statistique
AbstractEquipement <|-- Arme
AbstractPersonnage --> Arme

````

Puis ensuite on se base sur le nom de l'arme pour déterminer le texte de l'on affiche.

#### Exercice 4 :

En suivant la modélisation précédente :

- Codez une classe Arme qui hérite d'AbstractEquipement dans le package item

- Mettez à jour la classe AbstractPersonnage en ajoutant un attribut arme

- Mettez à jour le classe Magicien pour que le message retourné par la méthode attaque varie en fonction de l'arme équipée :

  - Si arme.nom == "Baton de feu" : "Lance des boules de feu"
  - Si arme.nom == "Baton de glace" : "Fait tomber des pic de glace"
  - Si arme.nom == "Necronomicon" :"Invoque un Grand Ancien"
  - Sinon levé l'exception ArmeInterditeException(self,arme) avec le code suivant `ArmeInterditeException(self,arme)`

  > :thinking: `raise ArmeInterditeException(self,arme)` fait référence à une exception personnalisée. Vous la trouverez dans le code fournie. Elle permet de dire qu'un le personnage possède une arme pour lequel il n'a pas la compétence et qu'il essaye de l'utiliser. Ce qui est théoriquement impossible, et signifie qu'il y a eu un problème quelque part. Car même si le code est bien fait et que ce cas ne devrait pas se produire car lors du changement d'équipement on doit vérifie que le personnage à bien le droit de s'équiper de cette arme, une erreur est toujours possible.

  

- Testez votre code avec la classe MagicienServiceTest. Si vous avez respecté les consignes, 1 seul test est en erreur. Corrigez-le pour que tous les tests soient au vert.

  <!--

````python
from abc import ABC, abstractmethod
class AbstractPersonnage(ABC):
    def __init__(self, arme):
        self.arme = arme
       
    @abstractmethod 
    def attaque(self):

               
class Magicien(Personnage):
    def __init(self):
        super().__init__(arme)
       
    def attaque(self):
        # code pour calculer les dégâts
        phrase=""
        if arme.nom == "Baton de feu":
            phrase = "Lance des boules de feu"
        elif arme.nom == "Baton de glace":
            phrase = "Fait tomber des pic de glace"
        elif arme.nom == "Necronomicon":
            phrase = "Invoque un Grand Ancien"
        else :
            raise ArmeInterditeException(self,arme)
        return AttaqueInfo(phrase, degat)
````

-->

Maintenant si nous avons 100 armes à gérer je vous laisser imaginer le calvaire :scream_cat: . Surtout si on veut permettre plusieurs classes de personnage à utiliser la même arme. Donc cette solution est rapidement ingérable.

La solution est du même style que celle utiliser dans [la partie 2.1](###2.1 Typons nos personnage par héritage), on va finalement dire que c'est l'arme qui va contenir le code décrivant son utilisation, et on va ajouter un nouveau niveau abstraction dans notre modélisation

````mermaid
classDiagram
class AbstractPersonnage {
	<<abstract>>
	 +AttaqueInfo attaque()
	 }
	 

class AbstractEquipement {
	<<abstract>>
	+String nom
	 }
	
class AbstractArme {
<<abstract>>
+String description_utilisation
+AttaqueInfo utiliserArme(Statistique stat_pers)
}
	 
	 	 	 
class Statistique {
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
}

Magicien --|> AbstractPersonnage
Guerrier --|> AbstractPersonnage
Voleur --|> AbstractPersonnage

AbstractPersonnage *--"1" Statistique
Statistique "1"--* AbstractEquipement
AbstractEquipement <|-- AbstractArme
AbstractPersonnage --> AbstractArme
Epee --|> AbstractArme
Baton --|> AbstractArme
Arc --|> AbstractArme
AbstractArme <|-- Couteau
AbstractArme <|-- Lance
AbstractArme <|-- Livre
````

En procédant ainsi on peut créer une grand nombre d'arme facilement, chacune ayant des règles d'utilisation différente, mais grâce à l'abstraction AbstractArme on sait que chaque arme dispose d'une méthode utiliserArme. Cette méthode aura un contenu différent pour chaque arme, mais s'appellera de la même manière pour toute et surtout devra retourner le même type d'objet. Remarquer qu'elle prend en paramètre un objet Statistique. Comme la relation qui lie AbstractPersonnage à AbstractArme et unidirectionnel il faut passer un paramètre qui contient les statistiques du personnage à l'arme. Tout cela permet que même si le code varie, l'utilisation sera la même. Par exemple :

````python
class AbstractArme(AbstractEquipement):
    def __init__(self, nom, description_utilisation, degat):
        super().__init__(nom)
        self.description_utilisation = description_utilisation
        self.degat = degat
        
    @abstractmethod
    def utiliserArme(stat_pers):
        

class Epee(AbstractArme):
    def __init(self,nom, description_utilisation):
        super().__init__(nom,description_utilisation, degat)
      
    def utiliserArme(stat_pers):
            degat_inflige = (stat_pers.force*1.1 * self.degat) +  stat_pers.force*1.4
            return AttaqueInfo(self.phrase, degat_inflige)

        
class Baton(AbstractArme):
    def __init(self,nom, description_utilisation):
        super().__init__(nom,description_utilisation, degat)
      
     def utiliserArme(stat_pers):
            degat_inflige = (stat_pers.force*0.7 * self.degat) +  (stat_pers.magie*1.2 * self.degat)
            return AttaqueInfo(self.phrase, degat_inflige)
            
            
# Et maintenant on peut générer une ininité d'arme toute unique, mais avec un comportement lié à son type.
baton_en_bois = Baton("Baton en bois", "Le lourd bâton de bois s'abat sur le crâne de l'enmemi", 10)
baton_de_fer = Baton("Baton de feu", "Lors de l'impact une explosion de calcine l'adversaire", 35)
epee_purificatrice = Epee("Master sword", "En éclair lumineux s'abatit sur le monstre", 750)
````

Cette solution utilise le *patron de conception Strategy*. Les patrons de conception sont des solutions à des problèmes de programmation récurrent. Ils sont indépendant du langage car ils proposent juste la modélisation d'une solution. Strategy permet de répondre au problème suivant : **Comment faire pour réaliser différentes opérations à un seul objet et les changer en cours d'exécution ?** Dans notre cas l'objet est le personnage et l'opération est attaquer. Pour ce faire on décide de transférer la responsabilité de l'attaque à l'arme. Maintenant il suffit de donner une arme différente à notre personnage pour changer sa façon d'attaquer.

> :thinking: Je vais revenir rapidement sur "faible couplage et forte cohérence". Dans cette partie on a **découplé** le comportement des armes et des personnages. Dans le code avec la structure if/elif/else c'était bien dans la classe qui hérite de Personnage qui définissait le comportement de l'arme, mais cela n'a pas réellement de sens. En effet, pourquoi le personnage devrait définir le comportement de l'arme ? Il est plus logique que ce soit l'arme elle même qui définisse son comportement. Et c'est ce que nous avons fait. Le comportement de l'arme dépend uniquement de l'arme. Et grâce à l'abstraction qu'apporte AbstractArme on sait comment appeler une arme. Et on sait ce qu'elle va nous retourner. Quelque soit l'arme ! Il "suffit" maintenant de coder le comportement des armes. Mais il n'y a plus de structure conditionnelle à maintenir. Et si cela apporte à terme un gain de temps considérable.

D'ailleurs une fois cela fait pour les armes il est facile de le faire pour les armures :

````mermaid
classDiagram
class AbstractPersonnage {
	<<abstract>>
	 +AttaqueInfo attaque()
	 +AttaqueInfo defense()
	 }
	 

class AbstractEquipement {
	<<abstract>>
	+String nom
	 }
	
class AbstractArme {
<<abstract>>
+String description_utilisation
+AttaqueInfo utiliserArme(Statistique stat_pers)
}
	 
class AbstractArmure {
<<abstract>>
+String description_utilisation
+DefenseInfo utiliserArmure(Statistique stat_pers)
}
	 	 	 
class Statistique {
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
}

Magicien --|> AbstractPersonnage
Guerrier --|> AbstractPersonnage
Voleur --|> AbstractPersonnage

AbstractPersonnage --> AbstractArmure
AbstractEquipement <|-- AbstractArmure
AbstractPersonnage *--"1" Statistique
Statistique "1"--* AbstractEquipement
AbstractEquipement <|-- AbstractArme
AbstractPersonnage --> AbstractArme
Epee --|> AbstractArme
Baton --|> AbstractArme
Arc --|> AbstractArme
AbstractArme <|-- Couteau
AbstractArme <|-- Lance
AbstractArme <|-- Livre

AbstractArmure <|--Robe
AbstractArmure <|--ArmureLegere
AbstractArmure <|--ArmureLourde
````

#### Exercice 5 :

- Ouvrez un nouveau terminal vers le cluster 

- Commitez le code que vous avez rédigez pour le moment. Dans le nouveau terminal tapez

  ````shell
  git add .
  git commit -m "TP1"
  ````

- Récupérer la branche avec le code à améliorer

  ```` shell
  git checkout strategy_pattern
  ````

- En vous basant sur le code fourni pour la gestion des armes implémentez (codez) la gestion des armures.
- Tester votre code avec la classe PersonnageServiceTest

### 2.5 Conclusion

Vous remarquerez qu'assez rapidement le diagramme de classe à grossit et peut-être que cela vous effraie. Il n'y a pas vraiment de raison. Il est assez facile d'imaginer que plus il y a de classe et plus un code est complexe et qu'une code avec peu de classe est facile. Et ce n'est pas juste car un code avec peu de classe peut être impossible à comprendre. La complexité de la modélisation ne provient pas du code mais du but recherché. Notre modélisation permet :

- Une gestion souple des types de personnage ;
- Une gestion souple de l'équipement ;
- La génération d'une infinité d'équipement tous différents, mais où les équipements d'un même type possède un comportement commun ;
- De ne pas avoir de redondance de code.

Ce qui est loin d'être triviale. La première solution avec des structures conditionnelles peut sembler simple car une structure *if/elif/else* est facile à comprendre. Mais rapidement on se retrouver avec des centaines de lignes de code sans la moindre plu value et où l'ajout ou la soustraction d'un cas devient un véritable casse tête car il faut partir à la chasse aux modifications. L'architecture proposée, bien qu'imposante à première abord est maintenable (on peut facilement ajouter/retirer des choses) et facile à faire évoluer (ajouter des armes, des armures, une nouvelle pièce d'équipement, des types de personnage etc)





## Pour aller plus loin

- [Patron de conception Strategy](https://www.codingame.com/playgrounds/10741/design-pattern-strategy/presentation) 