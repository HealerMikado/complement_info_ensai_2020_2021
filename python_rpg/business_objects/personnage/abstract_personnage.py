from abc import ABC, abstractmethod

from business_objects.attaque_info import AttaqueInfo
from business_objects.statistique import Statistique


class AbstractPersonnage(ABC):
    def __init__(self, arme, force, agilite, magie, defense, point_de_vie):
        self.statistique = Statistique(force, agilite, magie, defense,
                                       point_de_vie)
        self.arme = arme

    @abstractmethod  # décorateur qui définit une méthode comme abstraite
    def attaque(self):
        """
        Définit le comportement d'une attaque. Doit être implémenté par toutes les classe qui hérite de personnage
        :return: les dégâts purs et le texte de l'attaque dans un objet AttaqueInfo
        :rtype: AttaqueInfo
        """
