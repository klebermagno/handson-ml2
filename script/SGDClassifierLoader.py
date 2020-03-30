#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_openml

import numpy as np
import joblib

loaded_model = joblib.load(filename)

