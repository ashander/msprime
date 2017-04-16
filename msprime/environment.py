#
# Copyright (C) 2016 University of Oxford
#
# This file is part of msprime.
#
# msprime is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# msprime is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with msprime.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Common environment methods used to determine the state and versions
of various dependencies and the OS.
"""
from __future__ import print_function
from __future__ import division

import platform
import warnings

import _msprime

__version__ = "undefined"
try:
    from . import _version
    __version__ = _version.version
except ImportError:
    pass

# warnings at the end of the filter have least precedence by putting a filter at
# the end so clients of this module can override by importing warnings and
# running ``warnings.simplefilter("ignore", category=RuntimeWarning)
# before import
warnings.simplefilter("always", category=RuntimeWarning, append=True)


def have_numpy():
    """
    Returns true if numpy meets requirements

    Warns with RuntimeWarning (printed by defuault but can be suppressed by
    ``warnings.simplefilter("ignore", category=RuntimeWarning)``.
    """
    try:
        import numpy as np
        version = tuple(map(int, np.__version__.split(".")))
        if version < (1, 7, 0):
            warnings.warn("numpy version is too old: " +
                          "version 1.7 or newer needed",
                          RuntimeWarning)
            return False
        else:
            return True
    except:
        warnings.warn("Numpy not available. Some features will not work.",
                      RuntimeWarning)
        return False


def get_environment():
    """
    Returns a dictionary describing the environment in which msprime
    is currently running.
    """
    env = {
        "hdf5": {
            "version": _msprime.get_hdf5_version()
        },
        "gsl": {
            "version": _msprime.get_gsl_version()
        },
        "os": {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
        },
        "python": {
            "implementation": platform.python_implementation(),
            "version": platform.python_version_tuple(),
        }
    }
    return env


HAVE_NUMPY = have_numpy()  # Run check for numpy on import
