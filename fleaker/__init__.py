# ~*~ coding: utf-8 ~*~
"""
fleaker
~~~~~~

A framework built on top of the wonderful Flask with the goal of making
everything easier.

:copyright: (c) 2016 by Croscon Consulting.
:license: BSD, see LICENSE for more details.
"""

__version__ = '0.1.0-dev'

from .app import App
from .component import Component
from .json import FleakerJSONEncoder, FleakerJSONApp
