# SPDX-FileCopyrightText: 2015 Eric Larson
#
# SPDX-License-Identifier: Apache-2.0

"""CacheControl import Interface.

Make it easy to import from cachecontrol without long namespaces.
"""
__author__ = "Eric Larson"
__email__ = "eric@ionrock.org"
__version__ = "0.12.6"

from .adapter import SyncHTTPCacheTransport
from .controller import CacheController
