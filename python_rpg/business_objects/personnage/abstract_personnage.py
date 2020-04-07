from abc import ABC, abstractmethod


class AbstractPersonnage(ABC):
    def __init__(self, phrase_attaque, phrase_defense):
        self.phrase_attaque = phrase_attaque
        self.phrase_defense = phrase_defense

    @abstractmethod  # décorateur qui définit une méthode comme abstraite
    def attaque(self):
        """
        Définit le comportement d'une attaque. Doit être implémenté par toutes les classe qui hérite de personnage
        :return: les dégâts purs et le texte de l'attaque dans un objet AttaqueInfo
        :rtype: AttaqueInfo
        """