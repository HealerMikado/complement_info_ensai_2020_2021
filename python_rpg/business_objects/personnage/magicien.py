from business_objects.attaque_info import AttaqueInfo
from business_objects.personnage.abstract_personnage import AbstractPersonnage
from exceptions.arme_interdite_exception import ArmeInterditeException


class Magicien(AbstractPersonnage):
    def __init__(self, arme, armure, force, agilite, magie, defense,
                 point_de_vie):
        super().__init__(arme, armure, force, agilite, magie, defense,
                         point_de_vie)

    def attaque(self):
        #code spécifique au magicien ici
        return self.arme.utiliser_arme(self.statistique)

    def defense(self, attaque_info):
        # code spécifique au magicien ici
        return self.armure.utiliser_armure(self.statistique, attaque_info)

