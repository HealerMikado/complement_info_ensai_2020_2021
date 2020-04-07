class AttaqueInfo:
    def __init__(self, phrase_attaque, degats_attaque):
        """
        Contient les informations nécessaire pour décrire une attaque
        :param phrase_attaque: le phrase associée à l'attaque
        :type phrase_attaque: str
        :param degat_attaque: les dégâts pur de l'attaque
        :type degat_attaque: int
        """
        self.phrase_attaque = phrase_attaque
        self.degats_attaque = degats_attaque
        self.phrase_defense = None
        self.degats_finaux = None
