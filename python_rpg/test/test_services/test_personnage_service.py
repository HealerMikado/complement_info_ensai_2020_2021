from unittest import TestCase

from business_objects.attaque_info import AttaqueInfo
from business_objects.objet.arme.arc import Arc
from business_objects.objet.arme.baton import Baton
from business_objects.objet.arme.epee import Epee
from business_objects.personnage.guerrier import Guerrier
from business_objects.personnage.magicien import Magicien
from business_objects.personnage.voleur import Voleur
from services.personnage_service import PersonnageService


class TestPersonnageService(TestCase):
    def test_attaque_magicien_baton_en_bois(self):
        # GIVEN
        expected_output = "Le lourd bâton de bois s'abat sur le crâne de l'enmemi"
        baton_en_bois = Baton(
            "Baton en bois"
            , 0, 0, 0, 0, 0
            , expected_output
            , 10)
        magicien = Magicien(
            baton_en_bois
            , Robe("Robe", 0, 0, 0, 0, 0, "", 0)
            , 1, 1, 1, 1, 1)

        # WHEN
        actual_output = PersonnageService.attaque(magicien).phrase_attaque

        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_attaque_guerrier_master_sword(self):
        # GIVEN
        expected_output = "En éclair lumineux s'abatit sur le monstre"
        master_sword = Epee(
            "Master sword"
            , 0, 0, 0, 0, 0
            , expected_output
            , 750)
        guerrier = Guerrier(
            master_sword
            , ArmureLourde("Harnois complet", 0, 0, 0, 0, 0, "", 0)
            , 1, 1, 1, 1, 1)

        # WHEN
        actual_output = PersonnageService.attaque(guerrier).phrase_attaque

        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_attaque_voleur_arc_de_lynel(self):
        # GIVEN
        expected_output = "Trois flèches se fichèrent dans le crâne de " \
                          "l'adversaire"
        arc_de_lynel = Arc(
            "arc du dieu bestial"
            , 0, 0, 0, 0, 0
            , expected_output
            , 10)
        voleur = Voleur(
            arc_de_lynel
            , ArmureLegere("Armure de cuir", 0, 0, 0, 0, 0, "", 0)
            , 1, 1, 1, 1, 1)

        # WHEN
        actual_output = PersonnageService.attaque(voleur).phrase_attaque

        # THEN
        self.assertEqual(expected_output, actual_output)
