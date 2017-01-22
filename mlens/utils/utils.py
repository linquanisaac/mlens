#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ML-ENSEMBLE

author: Sebastian Flennerhag
date: 10/01/2017
licence: MIT
"""

from __future__ import division, print_function, with_statement

from time import time
from pandas import DataFrame, Series

try:
    import cPickle as pickle
except Exception:
    import pickle


def _slice(Z, idx):
    """Utility function for slicing either a DataFrame or an ndarray"""
    # determine training set
    if idx is None:
        z = Z.copy()
    else:
        if isinstance(Z, (DataFrame, Series)):
            z = Z.iloc[idx].copy()
        else:
            z = Z[idx].copy()
    return z


def pickle_save(obj, name):
    """Utility function for pickling an object"""
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)


def pickle_load(name):
    """Utility function for loading pickled object"""
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def print_time(t0, message='', **kwargs):
    """Utility function for printing time"""
    if len(message) > 0:
        message += ' | '

    r, s = divmod(time() - t0, 60)  # get sec
    h, m = divmod(r, 60)  # get h, min
    print(message + '%02d:%02d:%02d\n' % (h, m, s), **kwargs)
