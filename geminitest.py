import os
from dotenv import load_dotenv
import google.generativeai as genai


def googlegeneration(userinput):
    load_dotenv()


    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


    # Create the model
    generation_config = {
      "temperature": 0.8,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-2.0-flash-exp",
      generation_config=generation_config,
        system_instruction="""You are a discord bot called XIV Bot, a test bot made by Armaans_YT 
        and are an AI utility bot to serve the community.You were founded on the 14th of December 2024, 
        Powered by Google. Be inquisitive and cool bot"""


    )

    chat_session = model.start_chat(
          history=[]
        )


    while True:



        response = chat_session.send_message(userinput)

        modelresponse = response.text

        return modelresponse











