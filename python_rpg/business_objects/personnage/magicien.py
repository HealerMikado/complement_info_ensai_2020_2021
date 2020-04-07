from business_objects.attaque_info import AttaqueInfo
from business_objects.personnage.abstract_personnage import AbstractPersonnage
from exceptions.arme_interdite_exception import ArmeInterditeException


class Magicien(AbstractPersonnage):
    def __init__(self, arme, force, agilite, magie, defense, point_de_vie):
        super().__init__(arme, force, agilite, magie, defense, point_de_vie)

    def attaque(self):
        degat = 10
        phrase = ""
        if self.arme.nom == "Baton de feu":
            phrase = "Lance des boules de feu"
        elif self.arme.nom == "Baton de glace":
            phrase = "Fait tomber des pic de glace"
        elif self.arme.nom == "Necronomicon":
            phrase = "Invoque un Grand Ancien"
        else:
            raise ArmeInterditeException(self, self.arme)
        return AttaqueInfo(phrase, degat)