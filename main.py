import pandas as pd
import matplotlib.pyplot as plt

airplane_delays_df = pd.read_csv('Data/full_data_flightdelay.csv', on_bad_lines='warn')
print(airplane_delays_df)