import pandas as pd
import matplotlib.pyplot as plt

airplane_delays_df = pd.read_csv('data/full_data_flightdelay.csv', on_bad_lines='warn')

airplane_delays_df = airplane_delays_df.drop(columns=['DISTANCE_GROUP',
                                                      'SEGMENT_NUMBER',
                                                      'NUMBER_OF_SEATS',
                                                      'AIRPORT_FLIGHTS_MONTH',
                                                      'AIRLINE_FLIGHTS_MONTH',
                                                      'AIRLINE_AIRPORT_FLIGHTS_MONTH',
                                                      'AVG_MONTHLY_PASS_AIRPORT',
                                                      'AVG_MONTHLY_PASS_AIRLINE',
                                                      'FLT_ATTENDANTS_PER_PASS',
                                                      'GROUND_SERV_PER_PASS',
                                                      'LATITUDE',
                                                      'LONGITUDE',
                                                      'PREVIOUS_AIRPORT'])

airplane_delays_df['PRCP_CM'] = airplane_delays_df.PRCP * 2.54
airplane_delays_df['SNOW_CM'] = airplane_delays_df.SNOW * 2.54
airplane_delays_df['TMAX_CELSIUS'] = (airplane_delays_df.TMAX-32) * 5/9

airplane_delays_df = airplane_delays_df[airplane_delays_df['DEP_DEL15'] == 1]
print(airplane_delays_df)


airplane_delays_df.to_csv('airplane_delays.csv', index=False)
