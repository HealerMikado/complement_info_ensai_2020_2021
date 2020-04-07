from business_objects.personnage.personnage import MAGICIEN, VOLEUR, GUERRIER


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
        :type personnage: Personnage.personnage
        :return: la phrase de l'attaque
        :rtype: str
        """
        phrase = ""
        if personnage.personnage_type == MAGICIEN:
            phrase = "Lance une boule de feu"
        elif personnage.personnage_type == VOLEUR:
            phrase = "Tire à l'arc"
        elif personnage.personnage_type == GUERRIER:
            phrase = "Donne un coup d'épée"

        return phrase

    @staticmethod
    def defense(personnage):
        """
        Détermine à partir d'un personnage le texte de sa defense
        :param personnage: le personnage qui defend
        :type personnage: Personnage.personnage
        :return: la phrase de la defense
        :rtype: str
        """
        phrase = ""
        if personnage.personnage_type == MAGICIEN:
            phrase = "Utilise une barrière magique"
        elif personnage.personnage_type == VOLEUR:
            phrase = "Esquive adroitement l'attaque"
        elif personnage.personnage_type == GUERRIER:
            phrase = "Pare avec son bouclier"

        return phrase
