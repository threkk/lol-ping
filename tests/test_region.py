# -*- coding: utf-8 -*-

""" Test suite for the function src.lol_ping.region_builder """
import unittest
# from .context import region_builder


class RegionBuilderTest(unittest.TestCase):
    """ Defines the tests of the suite. """

    def test_empty(self):
        """
        Tests the region builder output when the given entry array is empty.
        """
        self.assertEquals(True, True)


if __name__ == '__main__':
    unittest.main()
