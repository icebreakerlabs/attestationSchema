import os
from dotenv import load_dotenv
from langfuse import Langfuse
import json
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

load_dotenv(dotenv_path="../.env")
# Get keys for your project
os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
os.environ["LANGFUSE_HOST"] = os.getenv("LANGFUSE_HOST")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

langfuse = Langfuse()

langfuse.auth_check()

system_prompt = """You are given a list of skills (schemaNameString), each starting with "Skill:".
Given a text, return the exact names of any skills from schemaNameString that are positively recommended or endorsed in the text.
Only return skills from schemaNameString that start with "Skill:".
If none are positively recommended, return 'undefined'.

Ignore negative statements, criticisms, or skills not in schemaNameString.

SchemaNameString: {schemaNameString}

Return your answer as the schemaName of the skill that is postively reccomended or 'undefined' if none are postively reccomended. (e.g. "Skill: Engineering")
"""

user_prompt = "text: {{text}}"

# pull the skills from the attestationSchemas.json file
with open('../typescript/attestationSchemas.json', 'r') as f:
    attestationSchemas = json.load(f)

schemaNameString = [schema['name'] for schema in attestationSchemas if schema['name'].startswith('Skill:')]

system_prompt = system_prompt.format(schemaNameString=schemaNameString)

langfuse.create_prompt(
    name="attestation-schema",
    type="chat",
    prompt=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    config={
        "model": "gpt-4.1-nano",
        "temperature": 0
    },
    labels=['production']
)




