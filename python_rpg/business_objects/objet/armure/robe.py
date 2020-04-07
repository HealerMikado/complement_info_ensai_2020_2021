from business_objects.objet.armure.abstract_armure import AbstractArmure


class Robe(AbstractArmure):
    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus, description_defense,
                 defense):
        super().__init__(nom, force_bonus, agilite_bonus, magie_bonus,
                         defense_bonus, point_de_vie_bonus, description_defense,
                         defense)

    def utiliser_armure(self, statistique_pers, attaque_info):
        degats_finaux = attaque_info.degats_attaque - (
                statistique_pers.magie + statistique_pers.defense) * self.defense \
                       / 100
        attaque_info.degats_finaux = degats_finaux
        attaque_info.phrase_defense = self.description_defense
        return attaque_info
