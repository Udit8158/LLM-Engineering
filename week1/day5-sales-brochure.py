from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)

system_prompt = """
 You're a sale brochure writer. You are givven a company name and their main website url.
 You need to generate a sales brochure for the company for their prospect and investors.
 The brochure should be 1 page long, well structured and easy to read.
 The brochure should have the following sections:
 1. Introduction
 2. Problem
 3. Solution
 4. Technology
 5. Market
 6. Traction
 7. Team
 8. Ask
"""

company_name = input("Enter the company name: ")
company_url = input("Enter the company url: ")

user_prompt = f"""
Company Name: {company_name}
Company URL: {company_url}
"""

def generate_brochure():
    response = openai.chat.completions.create(model = "gpt-5-nano", messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ])
    return response.choices[0].message.content

brochure = generate_brochure()
print(brochure)