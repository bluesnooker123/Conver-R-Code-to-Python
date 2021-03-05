
import pandas as pd
import pylogit as pl
from collections import OrderedDict
import numpy as np
import warnings; warnings.filterwarnings("ignore")

df = pd.read_csv('1.csv', delimiter=",")
df = df.sort_values(by="uri")

basic_specification = OrderedDict()
basic_names = OrderedDict()

range = list(range(6))
basic_specification["sp"] = "all_same"
basic_names["sp"] = "sp"		

basic_specification["xp"] = "all_same"
basic_names["xp"] = "xp"

basic_specification["tim"] = "all_same"
basic_names["tim"] = "tim"

custom_alt_id = "r_box"
obs_id_column = "uri"

x_model = pl.create_choice_model(data=df,
							alt_id_col=custom_alt_id,
							obs_id_col=obs_id_column,
							choice_col="win",
							specification=basic_specification,
							model_type="MNL",
							names=basic_names)

x_model.fit_mle(np.zeros(3))

summary = x_model.get_statsmodels_summary()
print(summary)





