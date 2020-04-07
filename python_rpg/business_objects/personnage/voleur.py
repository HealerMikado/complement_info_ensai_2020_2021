from business_objects.attaque_info import AttaqueInfo
from business_objects.personnage.abstract_personnage import AbstractPersonnage


class Voleur(AbstractPersonnage):
    def __init__(self):
        super().__init__("Tire à l'arc","Esquive adroitement l'attaque" )

    def attaque(self):
        degat = 10
        return AttaqueInfo(self.phrase_attaque, degat)