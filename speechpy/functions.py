"""function module.

This module demonstrates documentation for the calculation of
necessary functions required for the packages.


Attributes:

    frequency_to_mel: Converting the frequency to Mel scale.
        This is necessary for filterback energy calculation.
    mel_to_frequency: Converting the Mel to frequency scale.
        This is necessary for filterback energy calculation.
    triangle: Creating a triangle for filtebanks.
        This is necessary for filterback energy calculation.
    zero_handling: Hanlding zero values due to the possible
        issues regarding the log functions.
"""

from __future__ import division

import numpy as np


def frequency_to_mel(f):
    """converting from frequency to Mel scale.

    :param f: The frequency values(or a single frequency) in Hz.
    :returns: The mel scale values(or a single mel).
    """
    return 1127 * np.log(1 + f / 700.)


def mel_to_frequency(mel):
    """converting from Mel scale to frequency.

    :param mel: The mel scale values(or a single mel).
    :returns: The frequency values(or a single frequency) in Hz.
    """
    return 700 * (np.exp(mel / 1127.0) - 1)


def triangle(x, left, middle, right):
    out = np.zeros(x.shape)
    out[x <= left] = 0
    out[x >= right] = 0
    first_half = np.logical_and(left < x, x <= middle)
    out[first_half] = (x[first_half] - left) / (middle - left)
    second_half = np.logical_and(middle <= x, x < right)
    out[second_half] = (right - x[second_half]) / (right - middle)
    return out


def zero_handling(x):
    """
    This function handle the issue with zero values if the are exposed
    to become an argument for any log function.
    :param x: The vector.
    :return: The vector with zeros substituted with epsilon values.
    """
    return np.where(x == 0, np.finfo(float).eps, x)
