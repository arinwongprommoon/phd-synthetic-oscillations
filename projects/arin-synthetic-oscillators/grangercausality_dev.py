#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

# Granger causality
if False:
    grangercausality_dict = grangercausalitytests(
        pd.concat(
            [
                strain_mCherry_processed.T.iloc[:, 0],
                strain_flavin_processed.T.iloc[:, 0],
            ],
            axis=1,
        ),
        maxlag=[3],
    )

# Granger causality loop-through population
if False:
    f_values = []
    p_values = []
    for cellno in range(len(strain_mCherry_processed)):
        grangercausality_dict = grangercausalitytests(
            pd.concat(
                [
                    strain_mCherry_processed.T.iloc[:, cellno],
                    strain_flavin_processed.T.iloc[:, cellno],
                ],
                axis=1,
            ),
            maxlag=[3],
        )
        f_values.append(grangercausality_dict[3][0]["ssr_ftest"][0])
        p_values.append(grangercausality_dict[3][0]["ssr_ftest"][1])
    plt.scatter(f_values, -np.log2(p_values))
    plt.xlabel("F")
    plt.ylabel("-log2(p)")
    plt.show()
