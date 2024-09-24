import aiohttp
import asyncio 
import json
import pprint
from os import environ
from dotenv import load_dotenv
load_dotenv()
base_url = environ.get('URL')

async def enter(email:str, password:str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{base_url}/api/login", json={"username": email, "password": password}) as response:
                if response.status == 200:
                    result = await response.json()
                    return (1, result["token"])
                elif response.status > 399 and response.status < 500:
                    return (0, "Не верные данные")
                else:
                    return (-1, "Ошибка сервера")
    except:  
        return (-1, "Ошибка сервера")
    finally:
        #pass
        return (1, "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjcxMDAzODIsImV4cCI6MTcyNzcwNTE4Miwicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoibmV3QWNjb3VudCJ9.BwC06ZnFsgQpQDu1nf2I4ryQrM8Z7DmcVY-AC5PK0HtnW1fAatKpxeUOMLlnNTuTvYz5PxxCzqy925l__VQiwy9y1dYB0cQBmZ4nsdVhB9aAn3sx5w4ymNsarNe-Ke1ZVDBHAew80owl5O5299GahfczQBM8u2HbCOrPYI_OyNRlrFqPsNSdtM5FWN5_V0GJKhXkoWwuec9bEcSapCUrWI2SpeR_4xiC9xJYmnmQF1qBFaSeMY-5uvU1V8eJu7yF2LDnUE5rW1b166BYW45EOFlINzD-lUJv35wXuHs1izuD-LJdu0FXfkCWbEG-brfBxryVuhynSirKPZbEHmhtww")

async def get_list_printers():
    pass

#email = input("Введите email: ")
#password = input("Введите пароль: ")
#print(asyncio.run(enter(email, password)))


'''
with open('test.json') as f:
    templates = json.load(f)
    print( templates["token"])
    '''