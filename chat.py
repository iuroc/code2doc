import openai
import time
import os
from dotenv import load_dotenv

load_dotenv()

def get_result(text: str) -> str:
    '''获取 ChatGPT 回复

    Parameters
    ----------
    text : str
        问题内容

    Returns
    -------
    str
        回复内容
    '''
    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text},
            ],
        )
    except:
        print('正在重试')
        time.sleep(5)
        return get_result(text)
    return response['choices'][0]['message']['content']
