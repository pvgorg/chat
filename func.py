from requests import get,post
from phpthon import *
from json import loads
from os import *
from pathlib import Path

def gpt(text):
    text = text.replace(" ","+")
    try:
        api = loads(get(f"https://mrapiweb.ir/api/chatbot.php?key=testkey&question={text}").text)
        return api["javab"]
    except Exception as er:
        return er

def codeai(text):
    text = text.replace(" ","-")
    try:
        api = get(f"https://mrapiweb.ir/apitest/aiblack.php?text={text}").text
        return api
    except Exception as er:
        return er

def aisearch(text):
    text = text.replace(" ","-")
    try:
        api = get(f"https://mrapiweb.ir/api/aiblack.php?text={text}").text
        return api
    except Exception as er:
        return er

def image_gen(text):
    text = text.replace(" ","-")
    try:
        api = get(f"https://mrapiweb.ir/akssaz?text={text}").text
        return api
    except Exception as er:
        return er

def gemini(text):
    text = text.replace(" ","-")
    try:
        api = get(f"http://mrapiweb.ir/api/geminiai.php?question={text}").text
        return api
    except Exception as er:
        return er

class ephoto:
    def write_text(text,effect):
        try:
            return loads(get(f"https://mrapiweb.ir/api/ephoto.php?action=write_text&text={text}&effect={effect}").text)["image"]
        except Exception as er:
            return er
    def get_effects():
        return get("https://mrapiweb.ir/api/ephoto.php?action=get_effects").text
    def effect_info(effect):
        try:
            return get(f"https://mrapiweb.ir/api/ephoto.php?action=get_effect_info&effect={effect}").text
        except Exception as er:
            return er



def rextester(lang, code):
    import requests
    import json
    URL = "https://rextester.com/rundotnet/Run"
    languages = {
        "c#": 1,
        "csharp": "c#",
        "vb.net": 2,
        "vb": 2,
        "visual_basic_dotnet": 2,
        "f#": 3,
        "fsharp": 3,
        "java": 4,
        "python2": 5,
        "py2": 5,
        "c_gcc": 6,
        "gcc": 6,
        "c": ("gcc", "clang", "visual_c"),
        "cplusplus_gcc": 7,
        "cplusplus": "c++",
        "g++": 7,
        "c++": ("cplusplus_gcc", "cplusplus_clang", "visual_cplusplus"),
        "cpp_gcc": 7,
        "cpp": "c++",
        "php": 8,
        "pascal": 9,
        "pas": 9,
        "fpc": 9,
        "objective_c": 10,
        "objc": 10,
        "haskell": 11,
        "ruby": 12,
        "perl": 13,
        "lua": 14,
        "nasm": 15,
        "asm": 15,
        "sql_server": 16,
        "v8": 17,
        "common_lisp": 18,
        "clisp": 18,
        "lisp": ("common_lisp", "scheme"),
        "prolog": 19,
        "golang": 20,
        "go": 20,
        "scala": 21,
        "scheme": 22,
        "node": 23,
        "javascript": 23,
        "js": "javascript",
        "python3": 24,
        "py3": 24,
        "python": ("python3", "python2"),
        "c_clang": 26,
        "clang": 26,
        "cplusplus_clang": 27,
        "cpp_clang": 27,
        "clangplusplus": 27,
        "clang++": 27,
        "visual_cplusplus": 28,
        "visual_cpp": 28,
        "vc++": 28,
        "msvc": 28,
        "visual_c": 29,
        "d": 30,
        "r": 31,
        "tcl": 32,
        "mysql": 33,
        "postgresql": 34,
        "oracle": 35,
        "swift": 37,
        "bash": 38,
        "ada": 39,
        "erlang": 40,
        "elixir": 41,
        "ocaml": 42,
        "kotlin": 43,
        "brainfuck": 44,
        "fortran": 45
    }

    if lang not in languages:
        return "The entered language is incorrect!"

    data = {
        "LanguageChoiceWrapper": languages[lang],
        "Program": code
    }

    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(URL, data=data, headers=headers)

    if response.status_code != 200:
        return "Failed to connect to Rextester API!"

    response_json = response.json()
    result = response_json["Result"]
    try:
        return result
    except:
        return "Rextester Error"

    
    
