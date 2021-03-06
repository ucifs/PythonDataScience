import pandas as pd
import numpy as np
alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
                         (1.31, 0.54, 1.16),
                         ]
                        , columns=("Beer", "Wine", "Spirits"),
                        index=("South Carolina", "South Dakota"))
alco2009.index.name = "State"

s_stats = [state for state in alco2009.index if state[0] == 'S'] + ["Samoa"]
drinks = list(alco2009.columns) + ["Water"]
nan_alco = alco2009.reindex(s_stats, columns=drinks)

print(nan_alco)
print(nan_alco.max())
print(nan_alco.min(axis=1))
print(nan_alco.sum())