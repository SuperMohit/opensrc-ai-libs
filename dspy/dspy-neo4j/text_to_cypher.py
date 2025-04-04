"""
Text -> Knowledge Graph
1. text -> cypher

Constraints:
- Use the existing schema before creating new nodes and relationships.
"""
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
import dspy
from src.neo4j import Neo4j

# set up Neo4j using NEO4J_URI
neo4j = Neo4j(uri=os.getenv("NEO4J_URI"), user=os.getenv("NEO4J_USER"), password=os.getenv("NEO4J_PASSWORD"))

lm = dspy.OpenAI(
    model="gpt-4",
    max_tokens=1024,
)
dspy.configure(lm=lm)

class CypherFromText(dspy.Signature):
    """Instructions:
    Create a Cypher MERGE statement to model all entities and relationships found in the text following these guidelines:
    - Refer to the provided schema and use existing or similar nodes, properties or relationships before creating new ones.
    - Use generic categories for node and relationship labels."""

    text = dspy.InputField(desc="Text to model using nodes, properties and relationships.")
    neo4j_schema = dspy.InputField(desc="Current graph schema in Neo4j as a list of NODES and RELATIONSHIPS.")
    statement = dspy.OutputField(desc="Cypher statement to merge nodes and relationships found in the text.")

generate_cypher = dspy.ChainOfThought(CypherFromText)

if __name__ == "__main__":
    from pathlib import Path

    while True:
        try:
            text = input("\nEnter text: ")
            cypher = generate_cypher(text=text.replace("\n", " "), neo4j_schema=neo4j.fmt_schema())
            neo4j.query(cypher.statement.replace('```', ''))

        except Exception as e:
            print(e)
            print("Please input one paragraph at a time.")
            continue
        
        except KeyboardInterrupt:
            break




# Below is an example that you can enter.

# Enter text:  Alex is an adventurous 28-year-old with a passion for photography and hiking. In his free time, he enjoys capturing landscapes, experimenting with new recipes, and listening to indie music. His favorite foods are sushi and pizza, though he’s always up for trying new dishes from different cultures. Alex loves to travel, with his dream destinations being Japan, Iceland, and New Zealand. He holds a degree in Environmental Science, which fuels his interest in nature and sustainability. When he’s not out exploring the outdoors, you can find him reading books on history and science or hanging out with friends at a local coffee shop.