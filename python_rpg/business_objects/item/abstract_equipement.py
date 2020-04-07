from abc import ABC

from business_objects.statistique import Statistique


class AbstractEquipement(ABC):
    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus):
        self.nom = nom
        self.statistique_bonus = Statistique(force_bonus, agilite_bonus,
                                             magie_bonus, defense_bonus,
                                             point_de_vie_bonus)
