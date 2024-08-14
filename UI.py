import pandas as pd
import matplotlib.pyplot as plt

quit = False

airplane_delays_df = pd.read_csv('Data/airplane_delays.csv')
print(airplane_delays_df)
    
def most_delayed_airline():
    if airplane_delays_df['DEP_DEL15'] == 1:
        return airplane_delays_df['DEP_DEL15']
    else:
        airplane_delays_df=airplane_delays_df['DEP_DEL15'].drop
        
most_delayed_airline()
