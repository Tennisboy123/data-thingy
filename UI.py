import pandas as pd
import matplotlib.pyplot as plt

quit = False

airplane_delays_df = pd.read_csv('Data/airplane_delays.csv')

show_most_delayed_time_block = airplane_delays_df['DEP_TIME_BLK'].mode()
#print(show_most_delayed_time_block)

show_most_delayed_airline = airplane_delays_df['CARRIER_NAME'].mode()
#print("The most delayed airline in 2019 was " + show_most_delayed_airline)


    
