from business_objects.attaque_info import AttaqueInfo
from business_objects.personnage.abstract_personnage import AbstractPersonnage
from exceptions.arme_interdite_exception import ArmeInterditeException


class Magicien(AbstractPersonnage):
    def __init__(self, arme, force, agilite, magie, defense, point_de_vie):
        super().__init__(arme, force, agilite, magie, defense, point_de_vie)

    def attaque(self):
        pass