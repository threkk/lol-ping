#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO: Add docstring
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division
from platform import system

import subprocess
import sys
import re

# Extracted from
# https://www.reddit.com/r/leagueoflegends/comments/4efy17/how_to_check_your_ping_without_getting_into_the/d20167p
SERVER = {
    'NA': '104.160.131.3',
    'EUW': '104.160.141.3',
    'EUNE': '104.160.142.3',
    'OCE': '104.160.156.1',
    'LAN': '104.160.136.3',
}


def ping(host):
    """
    Calls the native ping function of OS X to extract the average time, the
    maximum time and the unit of the connection to the given server.

    :param host: str IP of the server.
    :return: dictionary average time, maximum time
    """

    # We call the native ping command from OS X.
    cmd = subprocess.Popen(
        ['ping', '-c', '4', host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    out, err = cmd.communicate()

    # Invalid host
    if err:
        return []

    else:
        # Grabs the average, max and the unit
        regexp = re.compile(r'round-trip min/avg/max/stddev ='
                            r' \d+.\d+/(\d+.\d+)/(\d+.\d+)/\d+.\d+ (\w+)$')
        match = re.search(regexp, out)

        return list(match.group(1, 2, 3)) if match else []


def region_builder(data):

    if len(data) == 1:
        return {'index': -1, 'region': data[0].ljust(4), 'average': '',
                'maximum': '', 'color': '|color=#444'}

    index = float(data[1])
    region = '{region}:'.format(region=data[0].ljust(4))
    average = '{average} {unit}'.format(average=data[1], unit=data[3])
    maximum = '(max {maximum} {unit})'.format(maximum=data[2], unit=data[3])

    if index < 100:
        color = '|color=#0A640C'  # Green
    elif index < 150:
        color = '|color=#FEC041'  # Yellow
    else:
        color = '|color=#FC645F'  # Red

    return {'index': index, 'region': region, 'average': average,
            'maximum': maximum, 'color': color}


def display(data):

    average_max_len = max(list(map(lambda x: len(x['average']), data)))
    maximum_max_len = max(list(map(lambda x: len(x['maximum']), data)))

    # Fixes an encoding issue with Bitbar. Usually this would not be needed
    # due to the import of unicode literals from future.
    if sys.version[0] == 3:
        print('𝐋')
    else:
        print('𝐋'.encode('utf-8'))

    print(u'---')
    for item in data:

        region = item['region']
        color = item['color']

        if item['index'] == -1:
            row = '{region} is not reacheable at the moment.{clr}'.format(
                   region=region, clr=color)

        else:
            raw_row = '{region} {average} {maximum} {clr} font=Menlo'

            average = item['average'].rjust(average_max_len)
            maximum = item['maximum'].rjust(maximum_max_len)

            row = raw_row.format(region=region, average=average,
                                 maximum=maximum, clr=color)
        print(row)
    print('Update now | color=#B8BABC refresh=true')

if __name__ == '__main__':

    if system().lower() == 'darwin':

        # For every region, calculates the ping and orders it speed.
        ping_per_region = []
        for region in SERVER:
            ping_in_region = ping(SERVER[region])
            region_data = region_builder([region] + ping_in_region)

            ping_per_region.append(region_data)

        ping_per_region.sort(key=lambda x: (1/float(x['index'])), reverse=True)
        display(ping_per_region)

    else:
        print(system().lower())
