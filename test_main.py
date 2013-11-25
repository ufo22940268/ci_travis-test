#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 garlic <garlic@localhost>
#
# Distributed under terms of the MIT license.

"""

"""

import os
import run

def test_main():
    app = run.app.test_client()
    rv = app.get('/test')
    assert rv.data == 'Hello World!'
