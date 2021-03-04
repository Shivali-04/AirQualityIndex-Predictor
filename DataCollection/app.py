"""
created on 31st Dec
"""
import os
import time
import requests
import sys

def get_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month <10):
                url="https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month,year) #or {} empty placeholders
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)  # or {} empty placeholders

            #Now retrieve the html data in text using requests
            texts= requests.get(url)
            # now t=do the YTF encoding to remove the special characters:
            text_utf= texts.text.encode('utf=8')
            if not os.path.exists("Data/html_data/{}".format(year)):
                os.makedirs("Data/html_data/{}".format(year))
            with open("Data/html_data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
        sys.stdout.flush()

if __name__=="__main__" :  ##entry point for this program
    start_time=time.time()
    get_html()
    end_time= time.time()
    print('Time Taken: {}'.format(end_time-start_time))

