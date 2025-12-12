from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=" * 60)
print("EXPERIMENT: What happens when we give GPT just a URL?")
print("=" * 60)

# Test 1: Famous website GPT knows about
print("\n📌 TEST 1: Famous Website (HuggingFace)")
print("-" * 60)

response1 = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "user", "content": "Create a brochure for:\nCompany: HuggingFace\nURL: https://huggingface.co"}
    ]
)
print(response1.choices[0].message.content)

# Test 2: Fake/Unknown website
print("\n\n📌 TEST 2: Fake Website GPT Cannot Know About")
print("-" * 60)

response2 = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "user", "content": "Create a brochure for:\nCompany: SuperTechXYZ\nURL: https://supertechxyz-fake-company-12345.com"}
    ]
)
print(response2.choices[0].message.content)

# Test 3: Asking GPT to scrape
print("\n\n📌 TEST 3: Explicitly Asking GPT to Scrape")
print("-" * 60)

response3 = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "user", "content": "Please scrape https://huggingface.co and tell me what's on the homepage right now."}
    ]
)
print(response3.choices[0].message.content)

print("\n" + "=" * 60)
print("CONCLUSION:")
print("=" * 60)
print("""
1. For famous websites: GPT uses MEMORIZED knowledge from training
2. For unknown websites: GPT will HALLUCINATE or admit it can't access
3. When asked to scrape: GPT will say it CANNOT access websites

GPT NEVER actually sees the real website content unless you scrape it first!
""")
