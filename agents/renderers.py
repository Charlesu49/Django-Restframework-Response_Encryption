import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from rest_framework.renderers import BaseRenderer
from dotenv import load_dotenv
import os
import json

load_dotenv()


AES_SECRET_KEY = bytes(os.getenv('AES_SECRET_KEY'), 'utf-8')
AES_IV = bytes(os.getenv('AES_IV'), 'utf-8')


# AES_SECRET_KEY= b'hdhdgdhdgdhdgdhd'
# AES_IV= b'hdhdgdhdgdhdgdhd'





class CustomAesRenderer(BaseRenderer):
    media_type = 'application/octet-stream'
    format = 'aes'

    def render(self, data, media_type=None, renderer_context=None):
        plaintext = json.dumps(data)
        padded_plaintext = pad(plaintext.encode(), 16)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        ciphertext = cipher.encrypt(padded_plaintext)
        ciphertext_b64 = base64.b64encode(ciphertext).decode()
        response = {'ciphertext': ciphertext_b64}
        return json.dumps(response)
    
    
    # def render(self, data, media_type=None, renderer_context=None):
    #     data = json.dumps(data)
    #     data= pad(data.encode(),16)
    #     cipher = AES.new(AES_SECRET_KEY,AES.MODE_CBC,AES_IV)
    #     return base64.b64encode(cipher.encrypt(data))
