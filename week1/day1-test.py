from openai import OpenAI
import os
from dotenv import load_dotenv
from scraper import fetch_website_contents # function to fetch website contents
from IPython.display import display,Markdown

load_dotenv(override=True)

client = OpenAI()


def summarize_website_contents(url, user_prompt):
    website_content = fetch_website_contents(url)
    system_prompt = f"""
    You are a helpful assistant that summarizes website contents.
    Provide a short summary of the given website.
    If it includes news or announcements, then summarize these too.
    Respond in markdown.
    Response should be in listicle format.
    Response should be in 2000 characters or less and should be concise and easy to consume.
    Here is the website content in ``` ``` this block of text.
    ``` {website_content} ```
    """
    input_messages = [
        {"role": "system", "content":system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response = client.responses.create(model='gpt-4.1-nano', input=input_messages)
    return response.output[0].content[0].text

def main():
    user_input_url = input("Website URL: ")
    user_input_prompt = input("Prompt: ")
    summary = summarize_website_contents(user_input_url, user_input_prompt)
    display(Markdown(summary)) # use print instead here
 

main()