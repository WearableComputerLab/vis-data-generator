#!/usr/bin/env python
import settings

import math
import plotly.express as px
import numpy as np
import pandas as pd
import json
import random


element_names = json.load(open('FakeElementNames.txt'))
random.shuffle(element_names)

# generate random data
rdata = []
for i in range(settings.N_DIMENSIONS):
    n = np.random.normal(0, 1, 100)
    rdata.append(n)

# correlate two or more dimensions randomly selected
cdims = random.sample(rdata, settings.N_CORRELATIONS)
for c1, c2 in zip(cdims, cdims[1:]): # we zip to get each consecutive pair, then we manipulate the data in each pair to get the correlation we want
    for i in range(len(c2)):
       c2[i] = c1[i] * settings.R_COEFFICIENT + c2[i] * math.sqrt(1 - settings.R_COEFFICIENT ** 2)

# derive the dataframe
df_dict = {}
for n in rdata:
    df_dict[element_names.pop()] = n
df = pd.DataFrame(df_dict)

# visualise the data
fig = px.scatter_matrix(df)
fig.update_traces(diagonal_visible=False)
fig.show()
