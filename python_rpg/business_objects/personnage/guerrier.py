from business_objects.attaque_info import AttaqueInfo
from business_objects.personnage.abstract_personnage import AbstractPersonnage


class Guerrier(AbstractPersonnage):
    def __init__(self):
        super().__init__("Donne un coup d'épée", "Pare avec son bouclier")

    def attaque(self):
        degat = 10
        return AttaqueInfo(self.phrase_attaque, degat)