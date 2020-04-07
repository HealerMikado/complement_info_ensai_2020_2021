from business_objects.attaque_info import AttaqueInfo
from business_objects.objet.arme.abstract_arme import AbstractArme


class Lance(AbstractArme):

    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus, description_attaque, degat):
        super().__init__(nom, force_bonus, agilite_bonus, magie_bonus,
                         defense_bonus, point_de_vie_bonus, description_attaque,
                         degat)

    def utiliser_arme(self,stat_pers):
        degat_inflige = (stat_pers.magie * 1.1 * self.degat) + \
                        stat_pers.agilite * 1.4
        return AttaqueInfo(self.description_attaque, degat_inflige)