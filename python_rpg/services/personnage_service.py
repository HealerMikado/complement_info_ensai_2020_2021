from business_objects.personnage.abstract_personnage import AbstractPersonnage


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
        :return: la phrase de l'attaque
        :rtype: str
        """
        return personnage.attaque()

    @staticmethod
    def defense(personnage):
        """
        Détermine à partir d'un personnage le texte de sa defense
        :param personnage: le personnage qui defend
        :type personnage: Personnage.personnage
        :return: la phrase de la defense
        :rtype: str
        """
        pass
