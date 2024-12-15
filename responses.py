#from random import choice, randint
import os
from dotenv import load_dotenv
import google.generativeai as genai
from geminitest import googlegeneration



def getresponses(entry: str):
    return googlegeneration(entry)






