#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 garlic <garlic@localhost>
#
# Distributed under terms of the MIT license.

"""

"""
from flask import Flask

app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
