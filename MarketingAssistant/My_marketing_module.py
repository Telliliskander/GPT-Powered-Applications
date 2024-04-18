from openai import OpenAI
import os
from IPython.display import display, HTML

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

api_key  = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)




def get_completion(fact_sheet_chair, model="gpt-3.5-turbo"):
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    At the end of the description, include every 7-character 
    Product ID in the technical specification.

    After the description, include a table that gives the 
    product's dimensions. The table should have two columns.
    In the first column include the name of the dimension. 
    In the second column include the measurements in inches only.

    Give the table the title 'Product Dimensions'.

    Format everything as HTML that can be used in a website. 
    Place the description in a <div> element.

    Technical specifications: ```{fact_sheet_chair}```
    """

 
    messages =  [  {'role' : 'system', 'content' : 'you are marketing expert'},
                   {'role':'user', 'content':prompt}  ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
 
    return response.choices[0].message.content

get_completion("the chair is heavy, and make out of wood")