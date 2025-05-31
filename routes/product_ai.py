from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def generate_product_description(product_name):
    llm = ChatOpenAI(
        model="gpt-4.1-nano", 
        )

    return llm.invoke(f"Write a usage guide for {product_name}. Only return the steps in a bulleted list for using the product, do not return anything else.").content.strip()

