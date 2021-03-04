import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def avg_data(y):
                #temp_i = 0
                average=[]
                for rows in pd.read_csv('Data/AQI/aqi{}.csv'.format(y),chunksize=24):
                    add_vars=0
                    avg=0.0
                    data=[]
                    df=pd.DataFrame(rows)
                    for index,row in df.iterrows():
                        data.append(row['PM2.5'])
                    for k in data:
                        if type(k)  is float or type(k) is int:
                            add_vars+=k
                        elif type(k) is str:
                            if k not in ['NoData','PwrFail','---','InVld']:
                                temp=float(k)
                                add_vars+=temp
                        avg=add_vars/24
                    average.append(avg)
                return average


if __name__=='__main__':
    k=avg_data(2013)
    plt.plot(range(0, len(k)), k, label='2013 Data')
    plt.show()

    """"
    print(len(k[0]))
    print(len(k[1]))
    print(len(k[2]))
    print(len(k[3]))
    print(len(k[4]))
    print(len(k[5]))
    
    fig,axs=plt.subplots(3,2)
    axs[0,0].plot(range(0,len(k[0])),k[0],label='2013 Data')
    axs[0,1].plot(range(0, len(k[1])),k[1], label='2014 Data')
    axs[1,0].plot(range(0, len(k[2])), k[2], label='2015 Data')
    axs[1,1].plot(range(0, len(k[3])), k[3], label='2016 Data')
    axs[2,0].plot(range(0, len(k[4])), k[4], label='2017 Data')
    axs[2,1].plot(range(0, len(k[5])), k[5], label='2018 Data')
    plt.show()
    """