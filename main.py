# Import the required modules
import json, requests
from pprint import pprint

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

def Advice_by_query():
    '''Getting an advice using id'''

    base_url = 'https://api.adviceslip.com/advice/search/'
    query = 0
    
    
    try:
        
        
        for i in range(5):
            query += 1
            url = f'{base_url}{query}'
            req = requests.get(url)
            req.raise_for_status

            # Storing the json data
            with open(f'Json_data_2/advice{i}.json','w') as f:
                source = req.json()
                f.write(json.dumps(source,indent=2))

           
    except Exception as e:
        print('Something Went Wrong ',e)

if __name__ == "__main__":

    Random_advice(END_POINT_1)  
    Advice_by_query()  

    print('Code Completed 🔥')
