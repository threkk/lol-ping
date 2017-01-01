# -*- coding: utf-8 -*-

""" Test suite for the function src.lol_ping.ping """
import unittest
from os import environ
from .context import ping


class PingTest(unittest.TestCase):
    """ Defines the tests of the suite. """

    def test_invalid_url(self):
        """ Tests if given an invalid string as url, it returns false. """
        output = ping('not a url')
        self.assertEqual(output, ['not a url'])

    def test_timeout(self):
        """ Tests if in case of time out, it returns false. """
        if environ.get('TRAVIS') == 'TRAVIS':
            self.skipTest(r'Test skipped due to TRAVIS not being '
                          r'able to call the ping command')
        else:
            output = ping('INV')
            self.assertEqual(output, ['INV'])

    def test_valid_url(self):
        """
        Tests if in case the function is successful, it return an array
        with exactly 3 elements.
        """
        if environ.get('TRAVIS') == 'TRAVIS':
            self.skipTest(r'Test skipped due to TRAVIS not being '
                          r'able to call the ping command')
        else:
            output = ping('LOC')
            self.assertTrue(output)
            self.assertEqual('LOC', output[0])
            self.assertTrue(len(output) == 4)


if __name__ == '__main__':
    unittest.main()
