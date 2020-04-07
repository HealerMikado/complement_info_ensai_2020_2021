class ArmeInterditeException(Exception):
    def __init__(self, personnage, arme):
        """
        Une exception personnalisé qui sera utile à partir de l'exercice 4
        :param personnage: le personne qui a une arme interdite qui lui est 
        interdite
        :type personnage: AbstractPersonnage         
        :param arme: l'arme interdite
        :type arme: AbstractEquipemet
        """
        self.personnage = personnage
        self.arme = arme

    def __str__(self):
        return 'Un objet de classe {} utilise {} qui lui est interdite'.format(
            self.personnage.__class__.__name__, self.arme.nom)
