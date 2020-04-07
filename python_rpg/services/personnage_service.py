from business_objects.personnage.abstract_personnage import AbstractPersonnage
from business_objects.attaque_info import AttaqueInfo

class PersonnageService:
    """
    PesonnageService va manipuler les personnages pour qu'ils agissent. Toutes
    les méthodes de la classe sont statiques car PersonnageService n'a pas
    d'état. Il va seulement manipuler les personnages qu'on lui passe en
    paramètre de ces fonctions.
    """

    @staticmethod
    def attaque(personnage):
        """
        Détermine à partir d'un personnage le texte de son attaque
        :param personnage: le personnage qui attaque
        :type personnage: AbstractPersonnage
        :return: l'attaque effectuée
        :rtype: AttaqueInfo
        """
        return personnage.attaque()

    @staticmethod
    def defense(personnage, attaque_info):
        """
        Détermine à partir d'un personnage le texte de sa defense
        :param personnage: le personnage qui defend
        :type personnage: AbstractPersonnage
        :param attaque_info : les informations de l'attaque
        :type attaque_info : AttaqueInfo
        :return: l'attaque effectuée mise à jour de la défense
        :rtype: AttaqueInfo
        """
        return personnage.defense(attaque_info)
