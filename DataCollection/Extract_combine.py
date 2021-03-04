from Plot_AQI import avg_data
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv


def met_data(month,year):
    file_html= open('Data/html_data/{}/{}.html'.format(year,month),'rb')
    plain_text= file_html.read()

    tempD=[]
    finalD=[]
    soup=BeautifulSoup(plain_text,"html.parser")
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a=tr.get_text()
                tempD.append(a)
    rows=len(tempD)/15

    for n in range(round(rows)):
        newtempD=[]
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
    length=len(finalD)

    finalD.pop(-1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(14)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(6)
        finalD[a].pop(4)
        finalD[a].pop(0)

    return finalD
#############################################

def data_combine(year,cs):
    for a in pd.read_csv('Data/Real-Data/real_{}.csv'.format(year),chunksize= cs):
        df=pd.DataFrame(a)
        mylist=df.values.tolist()
    return mylist

################################################
if __name__== '__main__':
    if not os.path.exists('Data/Real-Data'):
        os.makedirs('Data/Real-Data')
    for year in range(2013,2017):
        final_data=[]
        with open('Data/Real-Data/real_'+str(year) +'.csv','w') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            wr.writerow(['T','TM','Tm','H','W','V','VM','PM2.5'])
        for month in range(1,13):
            temp=met_data(month,year)
            final_data= final_data+temp

        #pm= getattr(sys.modules[__name__],'avg_data()')(year)
        pm = avg_data(year)
        if len(pm)==364:
            pm.insert(364,'-')
        for i in range(len(final_data)-1):
            final_data[i].insert(8,pm[i])

        with open('Data/Real-Data/real_{}.csv'.format(year),'a') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            for row in final_data:
                flag=0
                for elem in row:
                    if elem=="" or elem=="-":
                        flag=1
                if flag!=1:
                    wr.writerow(row)
    data_2013=data_combine(2013,500)
    data_2014 = data_combine(2014, 500)
    data_2015 = data_combine(2015, 500)
    data_2016 = data_combine(2016, 500)

    combine_data= data_2013+data_2014+data_2015+data_2016
    with open('Data/Real-Data/real_comb.csv','w') as csvfile:
        wr= csv.writer(csvfile,dialect='excel')
        wr.writerow(['T', 'TM', 'Tm', 'H', 'W', 'V', 'VM', 'PM2.5'])
        wr.writerows(combine_data)

