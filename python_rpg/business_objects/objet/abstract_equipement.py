from abc import ABC

from business_objects.statistique import Statistique


class AbstractEquipement(ABC):
    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus):
        """
        Constructeur commun à tous les equipements. Crée l'attribut
        statistique_bonus
        :param nom:
        :type nom: str
        :param force_bonus:
        :type force_bonus: int
        :param agilite_bonus:
        :type agilite_bonus: int
        :param magie_bonus:
        :type magie_bonus: int
        :param defense_bonus:
        :type defense_bonus: int
        :param point_de_vie_bonus:
        :type point_de_vie_bonus: int
        """
        self.nom = nom
        self.statistique_bonus = Statistique(force_bonus, agilite_bonus,
                                             magie_bonus, defense_bonus,
                                             point_de_vie_bonus)
