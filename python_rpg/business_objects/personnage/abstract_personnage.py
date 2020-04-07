from abc import ABC, abstractmethod

from business_objects.attaque_info import AttaqueInfo
from business_objects.statistique import Statistique
from business_objects.objet.armure.abstract_armure import AbstractArmure
from business_objects.objet.arme.abstract_arme import AbstractArme


class AbstractPersonnage(ABC):
    def __init__(self, arme, armure, force, agilite, magie, defense, \
                 point_de_vie):
        """
        Constructeur commun à tous les personnages
        :param arme: l'arme du personnage
        :type arme: AbstractArme
        :param armure: l'armure du personnage
        :type armure: AbstractArmure
        :param force: la force du personnage
        :type force: int
        :param agilite: l'agilite du personnage
        :type agilite: int
        :param magie: la magie du personnage
        :type magie: int
        :param defense: la défense du personnage
        :type defense: int
        :param point_de_vie: les point de vie du personnage
        :type point_de_vie: int
        """
        self.statistique = Statistique(force, agilite, magie, defense,
                                       point_de_vie)
        self.arme = arme
        self.armure = armure

    @abstractmethod  # décorateur qui définit une méthode comme abstraite
    def attaque(self):
        """
        Définit le comportement d'une attaque. Doit être implémenté par
        toutes  les classe qui héritent de personnage
        :return: les dégâts purs et le texte de l'attaque dans un objet AttaqueInfo
        :rtype: AttaqueInfo
        """

    @abstractmethod  # décorateur qui définit une méthode comme abstraite
    def defense(self,attaque_info):
        """
        Définit la défense d'un personnage Doit être implémenté par toutes les
        classe qui héritent de personnage
        :param attaque_info: information sur l'attaque qui arrive
        :type attaque_info: AttaqueInfo
        :return: l'bjet AttaqueInfo mise à jour avec la défense
        :rtype: AttaqueInfo
        """
