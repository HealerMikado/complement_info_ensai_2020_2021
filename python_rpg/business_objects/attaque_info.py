class AttaqueInfo:
    def __init__(self, phrase_attaque, degat):
        """
        Contient les informations nécessaire pour décrire une attaque
        :param phrase_attaque: le phrase associée à l'attaque
        :type phrase_attaque: str
        :param degat: les dégâts pur de l'attaque
        :type degat: int
        """
        self.phrase_attaque = phrase_attaque
        self.degat = degat