import os
import uuid
from cryptography.fernet import Fernet
import hashlib
import random
import string
import requests
from requests.exceptions import RequestException
import carpet.terminal as t
import numpy as np
import webview
import enum
import sys
import subprocess
import base64
import carpet.file_operations as fo
import tkinter as tk
import easygui

class gui:
    def __tkExitOnClose__(widget: tk.Tk):
        widget.protocol("WM_DELETE_WINDOW", lambda:sys.exit(0))
    def terms(title="Terms Of Service", terms='By clicking "I agree", you agree to ...'):
        while True:
            _ = easygui.buttonbox(terms, title, ["I agree", "I disagree"])
            if _ == "I disagree" or not _:
                continue
            else:
                break
    def terms2(title="Terms Of Service", terms='By clicking "I agree", you agree to ...'):
        t = tk.Tk()
        t.geometry(f"{round(900+len(terms))}x{round(600+len(terms)/10)}")
        t.title(title)

        gui.__ExitOnClose__(t)

        __tLabel__ = tk.Label(t, text=terms)
        __tLabel__.pack()

        __agree__ = tk.Button(t, text="I agree", command=t.destroy)
        __disagree__ = tk.Button(t, text="I disagree", command=lambda:sys.exit(0))

        __agree__.pack()
        tk.Label(t, text="").pack()
        __disagree__.pack()

        t.mainloop()

def percent_of(num_a, num_b):
    try:
        return (num_a / num_b) * 100
    except ZeroDivisionError:
        return 0

class hash:
    def sha256(text):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()
    def md5(text):
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    def sha1(text):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    def sha224(text):
        return hashlib.sha224(text.encode('utf-8')).hexdigest()

class text_encodings:
    utf8 = "UTF-8"

def Inputs(inputs = []):
    vals = []
    for i in range(len(inputs)):
        n = input(str(inputs[i]))
        vals.append(n)
    return vals

def genKey():
    return Fernet.generate_key()

def encrypt(contents, key):
    contents_encrypted = Fernet(key).encrypt(bytes(contents, text_encodings.utf8))
    return contents_encrypted

def decrypt(contents, key):
    contents_decrypted = Fernet(key).decrypt(bytes(contents))
    return contents_decrypted

def encryptList(list, key):
    outlist = []
    for i in range(len(list)):
        n = encrypt(list[i], key)
        outlist.append(n)
    return outlist

def decryptList(list, key):
    outlist = []
    for i in range(len(list)):
        n = decrypt(list[i], key)
        outlist.append(n)
    return outlist

def encryptFile(fileName, key):
    with open(fileName, "rb") as opentag:
        contents = opentag.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(fileName, "wb") as opentag:
        opentag.write(contents_encrypted)

def decryptFile(fileName, key):
    with open(fileName, "rb") as opentag:
        contents = opentag.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(fileName, "wb") as opentag:
        opentag.write(contents_decrypted)

def mkdir(dirname):
    os.mkdir(dirname)
def mkdirs(dirnames = []):
    for i in range(len(dirnames)):
        os.makedirs(dirnames[i])

class commands:
    def exec(commandtoexecute):
        os.system(command=commandtoexecute)

def rstring(length = 16):
    if type(length) == str:
        length = len(length)
    result = ''.join(random.choices(string.ascii_letters, k=length))
    return result

class text_operations:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    digits = [0,1,2,3,4,5,6,7,8,9]
    digits_txt = ["0","1","2","3","4","5","6","7","8","9"]

def randList(list):
    return random.choice(list)

hashtype = {"md5":"HASH_MD5","sha256":"HASH_SHA256", "sha224":"HASH_SHA224", "sha1":"HASH_SHA1"}

def hashInput(prompt, hashType):
    unhashed_input = input(prompt)
    if hashType == "HASH_MD5":
        return [unhashed_input, hash.md5(unhashed_input)]
    if hashType == "HASH_SHA256":
        return [unhashed_input, hash.sha256(unhashed_input)]
    if hashType == "HASH_SHA224":
        return [unhashed_input, hash.sha224(unhashed_input)]
    if hashType == "HASH_SHA1":
        return [unhashed_input, hash.sha1(unhashed_input)]
    else:
        return False

def Hash(txt, hashType):
    unhashed_input = txt
    if hashType == "HASH_MD5":
        return hash.md5(unhashed_input)
    if hashType == "HASH_SHA256":
        return hash.sha256(unhashed_input)
    if hashType == "HASH_SHA224":
        return hash.sha224(unhashed_input)
    if hashType == "HASH_SHA1":
        return hash.sha1(unhashed_input)
    else:
        return False

def download(URL, OutputFile, AllowRedirects: bool = True):
    try:
        with requests.get(URL, allow_redirects=AllowRedirects) as r:
            open(OutputFile, "wb").write(r.content)
    except RequestException as e:
            print(e)
    return

def getURLDataBytes(URL, AllowRedirects: bool = True):
    try:
        with requests.get(URL, allow_redirects=AllowRedirects) as r:
            return r.content
    except RequestException as e:
            print(e)

def getURLData(URL, AllowRedirects: bool = True):
    try:
        with requests.get(URL, allow_redirects=AllowRedirects) as r:
            return r.text
    except RequestException as e:
            print(e)

def show_terminal_image(image_path):
    t.show_image(image_path)

def cgen(length: int):
    random_source = string.ascii_letters + string.digits + string.punctuation
    out = random.choice(string.ascii_lowercase)
    out += random.choice(string.ascii_uppercase)
    out += random.choice(string.digits)
    out += random.choice(string.punctuation)
    for i in range(length):
        out += random.choice(random_source)
    out_list = list(out)
    random.SystemRandom().shuffle(out_list)
    out = ''.join(out_list)
    return out

def rUUID(rLevel: int = 48):
    return uuid.UUID(Hash(rstring(rLevel), hashtype['md5']))

def sqrt(num: int):
    return np.sqrt(num)

def Oppose(l: list):
    return {'max':max(l), 'min':min(l)}

def avg(arr):
    return np.average(arr)

def c_arr(s: str):
    return [*s]

def splitspaces(s: str):
    return s.split(" ")

def createWebWindow(title: str, URL: str, w: int = 1000, h: int = 800):
    webview.create_window(title, URL, width=w, height=h)
    webview.start()


class CleanTypes(enum.Enum):
    FULL_CLEAN = 0
    REMOVE_SPACES = 1
    REVERSE_STRING = 2
    SHUFFLE = 3

class String(str):
    def __init__(self, s: str, ) -> None:
        self.s = s
    def Clean(self, ct: CleanTypes):
        if ct == CleanTypes.FULL_CLEAN:
            return ''.join(self.s.split()).strip().lower()
        elif ct == CleanTypes.REMOVE_SPACES:
            return ''.join(self.s.split())
        elif ct == CleanTypes.REVERSE_STRING:
            return ''.join(self.s[len(self.s)::-1])
        elif ct == CleanTypes.SHUFFLE:
            _c_arr = c_arr(self.s)
            return ''.join(random.sample(_c_arr, len(_c_arr)))
        else:
            return



#@deprecation.deprecated(deprecated_in="1.0", current_version="1.0", details="The function 'clear' uses an unsafe method of clearing the screen. Use clscr instead.")
def clear(deprication_understood: bool=False) -> None:
    if sys.platform not in ('win32', 'cygwin'):
        subprocess.call('clear')
    else:
        subprocess.call('cls')
    if not deprication_understood:
        print("The function 'clear' uses an unsafe method of clearing the screen. Use clscr instead.")
    return


class Settings():
    def __init__(self, file) -> None:
        self.file = file
        if not os.path.isfile(self.file):
            fo.write(self.file, '{}')
        elif not fo.read(self.file).__contains__("{") or not fo.read(self.file).__contains__("}"):
            fo.write(self.file, '{}')
    
    def set(self, data_name, data_value):
        fo.append_json({data_name: data_value}, self.file)
    def d_set(self, d: dict):
        fo.append_json(d, self.file)
    
    def read(self):
        return fo.read_json(self.file)


