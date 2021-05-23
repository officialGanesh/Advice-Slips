# Import the required modules
import json, requests
from pprint import pprint
import pandas as pd


END_POINT_1 = 'https://api.adviceslip.com/advice'


def Random_advice(url):
    '''Getting the random advice using first api link or url'''

    r = requests.get(END_POINT_1)
    r.raise_for_status

    try:

        with open('Json_data_1.json','w') as f:
            source = r.json()
            f.write(json.dumps(source,indent=2))        

    except Exception as e:
        print('Something Went Wrong ',e)



if __name__ == "__main__":

    Random_advice(END_POINT_1)
    
    print('Code Completed 🔥')
