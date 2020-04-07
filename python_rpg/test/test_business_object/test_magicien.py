from unittest import TestCase

from business_objects.item.arme import Arme
from business_objects.personnage.magicien import Magicien
from exceptions.arme_interdite_exception import ArmeInterditeException


class TestMagicien(TestCase):
    def test_arme_baton_de_feu(self):
        # GIVEN
        arme = Arme("Baton de feu", 0, 0, 0, 0, 0)
        magicien = Magicien(arme, 0, 0, 0, 0, 0)
        expected_output = "Lance des boules de feu"
        # WHEN
        actual_output = magicien.attaque().phrase_attaque
        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_arme_baton_de_feu(self):
        # GIVEN
        arme = Arme("Baton de glace", 0, 0, 0, 0, 0)
        magicien = Magicien(arme, 0, 0, 0, 0, 0)
        expected_output = "Fait tomber des pic de glace"
        # WHEN
        actual_output = magicien.attaque().phrase_attaque
        # THEN
        self.assertEqual(expected_output, actual_output)

    def test_arme_baton_de_feu(self):
        # GIVEN
        arme = Arme("Necronomicon", 0, 0, 0, 0, 0)
        magicien = Magicien(arme, 0, 0, 0, 0, 0)
        expected_output = "Invoque un Grand Ancien"
        # WHEN
        actual_output = magicien.attaque().phrase_attaque
        # THEN
        self.assertEqual(expected_output, actual_output)


    def test_ArmeInterditeException(self):
        # GIVEN
        arme = Arme("", 0, 0, 0, 0, 0)
        magicien = Magicien(arme, 0, 0, 0, 0, 0)
        # WHEN
        # THEN
        with self.assertRaises(ArmeInterditeException):
            magicien.attaque().phrase_attaque
