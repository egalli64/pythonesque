"""
CodeEval Discount Offers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/48/
"""
import unittest
from ce.c048 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('21.00', solution('Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow'))

    def test_provided_2(self):
        self.assertEqual('83.50', solution('Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,16lb bowling ball,Red Swingline Stapler,Printer paper,Vibe Magazine Subscriptions - 40 pack'))

    def test_provided_3(self):
        self.assertEqual('71.25', solution('Jareau Wade,Rob Eroh,Mahmoud Abdelkader,Wenyi Cai,Justin Van Winkle,Gabriel Sinkin,Aaron Adelson;Batman No. 1,Football - Official Size,Bass Amplifying Headphones,Elephant food - 1024 lbs,Three Wolf One Moon T-shirt,Dom Perignon 2000 Vintage'))

    def test_no_customer(self):
        self.assertEqual('0.00', solution(';Batman No. 1,Football - Official Size'))

    def test_no_product(self):
        self.assertEqual('0.00', solution('Jareau Wade,Rob Eroh;'))

if __name__ == '__main__':
    unittest.main()
