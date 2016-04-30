# doing-crypto
[![Build Status](https://travis-ci.org/micha-k/doing-crypto.svg?branch=master)](https://travis-ci.org/micha-k/doing-crypto)
[![Coverage Status](https://coveralls.io/repos/github/micha-k/doing-crypto/badge.svg?branch=master)](https://coveralls.io/github/micha-k/doing-crypto?branch=master)

This is a repo where I spent some of my rare spare time hours to keep my computer skills in shape. Therefore I'll try to re-implement a few of the most common historic and modern crypto algorithms in python.

_Warning:_ This is just for fun! I DO NOT encourage anybody to use my implementations anywhere. They are probably full of bugs, flaws and use insecure random numbers! Use industry standard implementations. I do in production environments as well.


## Getting started

Create an use virtual environment

    virtualenv -p /usr/bin/python2.7 venv    # First time only
    source venv/bin/activate


Update dependencies

    pip install -r requirements.txt


Run all tests

    nosetests -v


## Literature

* A great book for getting started is _Understanding Crpytography_ by Christof Paar and Jan Pelzl, ISBN: 978-3-642-04100-6
