from unittest import TestCase

from business_objects.personnage.personnage import Personnage, MAGICIEN, GUERRIER, VOLEUR
from services.personnage_service import PersonnageService


class TestPersonnageService(TestCase):
    def test_attaque_magicien(self):
        #GIVEN un personnage de type magicien
        magicien = Personnage(MAGICIEN)
        expected_output = "Lance une boule de feu"

        #WHEN
        actual_output = PersonnageService.attaque(magicien)

        #THEN
        self.assertEqual(expected_output, actual_output)

    def test_attaque_guerrier(self):
        #GIVEN un personnage de type guerrier
        guerrier = Personnage(GUERRIER)
        expected_output = "Donne un coup d'épée"

        #WHEN
        actual_output = PersonnageService.attaque(guerrier)

        #THEN
        self.assertEqual(expected_output, actual_output)

    def test_attaque_voleur(self):
        #GIVEN un personnage de type voleur
        voleur = Personnage(VOLEUR)
        expected_output = "Tire à l'arc"

        #WHEN
        actual_output = PersonnageService.attaque(voleur)

        #THEN
        self.assertEqual(expected_output, actual_output)


    def test_defense_magicien(self):
        # GIVEN un personnage de type magicien
        magicien = Personnage(MAGICIEN)
        expected_output = "Utilise une barrière magique"

        # WHEN
        actual_output = PersonnageService.defense(magicien)

        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_defense_guerrier(self):
        # GIVEN un personnage de type magicien
        guerrier = Personnage(GUERRIER)
        expected_output = "Pare avec son bouclier"

        # WHEN
        actual_output = PersonnageService.defense(guerrier)

        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_defense_voleur(self):
        # GIVEN un personnage de type voleur
        voleur = Personnage(VOLEUR)
        expected_output = "Esquive adroitement l'attaque"

        # WHEN
        actual_output = PersonnageService.defense(voleur)

        # THEN
        self.assertEqual(expected_output, actual_output)
