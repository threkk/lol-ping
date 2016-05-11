"""
TODO: Add docstring
"""
from __future__ import print_function
from __future__ import unicode_literals
import subprocess
import re
from platform import system

# Extracted from
# https://www.reddit.com/r/leagueoflegends/comments/4efy17/how_to_check_your_ping_without_getting_into_the/d20167p
SERVER = {
    'NA': '104.160.131.3',
    'EUW': '104.160.141.3',
    'EUNE': '104.160.142.3',
    'OCE': '104.160.156.1',
    'LAN': '104.160.136.3'
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


def display_builder(data):
    index = float(data[1])
    region = '{region}:'.format(region=data[0].ljust(4))
    average = '{average} {unit}'.format(average=data[1], unit=data[3])
    maximum = '(max {maximum} {unit})'.format(maximum=data[2], unit=data[3])

    return {index: index, region: region, average: average, maximum: maximum}


if __name__ == '__main__':

    if system().lower() == 'darwin':

        # For every region, calculates the ping and orders it speed.
        ping_per_region = []
        for region in SERVER:
            ping_in_region = ping(SERVER[region])
            str_format = display_builder([region] + ping_in_region)

            ping_per_region.append((ping_in_region, str_format))

        ping_per_region.sort(key=lambda x: float(x[1][1]))
        print(ping_per_region)

    else:
        print(system().lower())
