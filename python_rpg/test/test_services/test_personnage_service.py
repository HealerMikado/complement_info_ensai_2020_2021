from unittest import TestCase

from business_objects.personnage.guerrier import Guerrier
from business_objects.personnage.magicien import Magicien
from business_objects.personnage.voleur import Voleur
from services.personnage_service import PersonnageService


class TestPersonnageService(TestCase):
    def test_attaque_magicien(self):
        #GIVEN un personnage de type magicien
        magicien = Magicien()
        expected_output = "Lance une boule de feu"

        #WHEN
        actual_output = PersonnageService.attaque(magicien)

        #THEN
        self.assertEqual(expected_output, actual_output.phrase_attaque)

    def test_attaque_guerrier(self):
        #GIVEN un personnage de type guerrier
        guerrier = Guerrier()
        expected_output = "Donne un coup d'épée"

        #WHEN
        actual_output = PersonnageService.attaque(guerrier)

        #THEN
        self.assertEqual(expected_output, actual_output.phrase_attaque)

    def test_attaque_voleur(self):
        #GIVEN un personnage de type voleur
        voleur = Voleur()
        expected_output = "Tire à l'arc"

        #WHEN
        actual_output = PersonnageService.attaque(voleur)

        #THEN
        self.assertEqual(expected_output, actual_output.phrase_attaque)

