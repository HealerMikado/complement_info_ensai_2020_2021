from business_objects.objet.abstract_equipement import AbstractEquipement
from business_objects.attaque_info import AttaqueInfo
from business_objects.statistique import Statistique


class AbstractArmure(AbstractEquipement):
    def __init__(self, nom, force_bonus, agilite_bonus, magie_bonus,
                 defense_bonus, point_de_vie_bonus, description_defense,
                 defense):
        super().__init__(nom, force_bonus, agilite_bonus, magie_bonus,
                         defense_bonus, point_de_vie_bonus)
        self.description_defense = description_defense
        self.defense = defense

    def utiliser_armure(self, statistique_pers, attaque_info):
        """
        Détermine la défenser d'une armure. Chaque armure doit surcharger cette
        méthode pour donner son comportement spécifique
        :param statistique_pers: les stats du personnage qui désire utiliser
        l'armure
        :type statistique_pers: Statistique
        :param attaque_info: les différentes informations de l'attaque dont il faut se défendre
        :type attaque_info: AttaqueInfo
        :return: Le résultat de la défense dans un objet AttaqueInfo mise à jour
        :rtype: AttaqueInfo
        """