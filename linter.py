# Original by Jon Surrell
# Copyright (c) 2014 Jon Surrell
# License: MIT
# Change for CudaLint by Alexey T.

import os
from cuda_lint import Linter, util

if os.name=='nt':
    _exe = os.path.join(os.path.dirname(__file__), 'gotype', 'gotype.exe')
else:
    _exe = 'gotype'

class Gotype(Linter):
    """Provides an interface to gotype."""

    syntax = 'Go'
    cmd = (_exe, '-e')
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    error_stream = util.STREAM_STDERR
