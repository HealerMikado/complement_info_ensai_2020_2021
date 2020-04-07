from business_objects.objet.abstract_equipement import AbstractEquipement


class Arme(AbstractEquipement):
    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus):
        super().__init__(nom, force_bonus, agilite_bonus, magie_bonus,
                         defense_bonus, point_de_vie_bonus)
