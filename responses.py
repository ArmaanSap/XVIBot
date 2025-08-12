#from random import choice, randint
import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
from geminitest import aigeneration


def getresponses(entry: str, user_id: str = None, user_obj = None):
    return aigeneration(entry, user_id, user_obj)

async def getresponses_async(entry: str, user_id: str = None, user_obj = None):
    """Async wrapper to prevent blocking the Discord event loop"""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, aigeneration, entry, user_id, user_obj)
