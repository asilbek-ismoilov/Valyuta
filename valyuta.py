import requests

def get_val_malum(val):
    url = f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url=url)

    if response.status_code != 200:
        return None
    
    data = response.json()

    for currency in data:
        if currency['Ccy'] == val:
            if val == 'USD':
                return f'Sana: {data[0]["Date"]} \n1 dollar = {data[0]["Rate"]} \nnomi : {data[0]["CcyNm_UZ"]}'
                 
        else: 
            return "Bunday qiymat mavjud emas !"


