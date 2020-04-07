from abc import abstractmethod

from business_objects.objet.abstract_equipement import AbstractEquipement
from business_objects.attaque_info import AttaqueInfo


class AbstractArme(AbstractEquipement):
    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus, description_attaque, degat):
        super().__init__(nom, force_bonus, agilite_bonus, magie_bonus,
                         defense_bonus, point_de_vie_bonus)
        self.description_attaque = description_attaque
        self.degat = degat

    @abstractmethod
    def utiliser_arme(self, statistique_pers):
        """
        Détermine comment une arme s'utilise. Chaque arme doit surcharger cette
        méthode pour donner son comportement spécifique
        :param statistique_pers: les stats du personnage qui désire utiliser
        l'arme
        :type statistique_pers: Statistique
        :return: Le résultat de l'attaque dans un objet AttaqueInfo
        :rtype: AttaqueInfo
        """
