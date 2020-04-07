from business_objects.attaque_info import AttaqueInfo
from business_objects.personnage.abstract_personnage import AbstractPersonnage


class Magicien(AbstractPersonnage):
    def __init__(self):
        super().__init__("Lance une boule de feu",
                         "Utilise une barrière magique")

    def attaque(self):
        degat = 10
        return AttaqueInfo(self.phrase_attaque, degat)