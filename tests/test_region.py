# -*- coding: utf-8 -*-

""" Test suite for the function src.lol_ping.region_builder """
import unittest
from .context import region_builder


class RegionBuilderTest(unittest.TestCase):
    """ Defines the tests of the suite. """

    def test_empty(self):
        """
        Tests the region builder output when the given entry array is empty.
        """
        output = region_builder(['REG'])
        expected = {'index': -1, 'region': 'REG ', 'average': '',
                    'maximum': '', 'color': '| color=#444'}
        self.assertEqual(expected, output)

    def test_green(self):
        """
        Tests the region builder output when the given entry is a 'green'
        """
        output = region_builder(['REG', 85, 95, 'ms'])
        expected = {'index': 85.0, 'region': 'REG :', 'average': '85 ms',
                    'maximum': '(max 95 ms)', 'color': '|color=#0A640C'}
        self.assertEqual(expected, output)

    def test_yellow(self):
        """
        Tests the region builder output when the given entry is a 'yellow'
        """
        output = region_builder(['REG', 100, 145, 'ms'])
        expected = {'index': 100.0, 'region': 'REG :', 'average': '100 ms',
                    'maximum': '(max 145 ms)', 'color': '|color=#FEC041'}
        self.assertEqual(expected, output)

    def test_red(self):
        """
        Tests the region builder output when the given entry is a 'yellow'
        """
        output = region_builder(['REG', 150, 195, 'ms'])
        expected = {'index': 150.0, 'region': 'REG :', 'average': '150 ms',
                    'maximum': '(max 195 ms)', 'color': '|color=#FC645F'}
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
