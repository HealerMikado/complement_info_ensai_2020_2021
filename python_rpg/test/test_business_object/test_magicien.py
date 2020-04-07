from unittest import TestCase

from business_objects.item.arme import Arme
from business_objects.personnage.magicien import Magicien
from exceptions.arme_interdite_exception import ArmeInterditeException


class TestMagicien(TestCase):
    def test_arme_baton_de_feu(self):
        # GIVEN
        arme = Arme("Baton de feu", 0, 0, 0, 0, 0)
        magicien = Magicien(arme=arme, force=0, agilite=0, magie=0,
                    defense=0, point_de_vie=0)
        expected_output = "Lance des explosions de feu"
        # WHEN
        actual_output = magicien.attaque().phrase_attaque
        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_arme_baton_de_feu(self):
        # GIVEN
        arme = Arme("", 0, 0, 0, 0, 0)
        magicien = Magicien(arme=arme, force=0, agilite=0, magie=0,
                    defense=0, point_de_vie=0)
        expected_output = "Fait tomber des pic de glace"
        # WHEN
        actual_output = magicien.attaque().phrase_attaque
        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_arme_baton_de_feu(self):
        # GIVEN
        arme = Arme("Necronomicon", 0, 0, 0, 0, 0)
        magicien = Magicien(arme=arme, force=0, agilite=0, magie=0,
                            defense=0, point_de_vie=0)
        expected_output = ""
        # WHEN
        actual_output = magicien.attaque().phrase_attaque
        # THEN
        self.assertEqual(expected_output, actual_output)


    def test_ArmeInterditeException(self):
        # GIVEN
        arme = Arme("", 0, 0, 0, 0, 0)
        magicien = Magicien(arme=arme, force=0, agilite=0, magie=0,
                            defense=0, point_de_vie=0)
        # WHEN
        # THEN
        with self.assertRaises(ArmeInterditeException):
            magicien.attaque().phrase_attaque
