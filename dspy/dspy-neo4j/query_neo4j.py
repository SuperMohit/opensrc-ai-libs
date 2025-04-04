"""
Text -> Knowledge Graph
1. Question -> Cypher -> Query Neo4j -> Response
"""

import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
import dspy
from src.neo4j import Neo4j

# Set up Neo4j using NEO4J_URI
neo4j = Neo4j(uri=os.getenv("NEO4J_URI"), user=os.getenv("NEO4J_USER"), password=os.getenv("NEO4J_PASSWORD"))

# Configure the language model
lm = dspy.OpenAI(
    model="gpt-4",
    max_tokens=1024,
)
dspy.configure(lm=lm)

class QuestionToCypher(dspy.Signature):
    """Instructions:
    Generate a Cypher query to answer the user's question based on the provided schema.
    - Use the schema to guide the query generation.
    - Ensure the query retrieves the necessary data to answer the question."""

    question = dspy.InputField(desc="User's question about the data in the Neo4j database.")
    neo4j_schema = dspy.InputField(desc="Current graph schema in Neo4j as a list of NODES and RELATIONSHIPS.")
    cypher_query = dspy.OutputField(desc="Cypher query to retrieve the data needed to answer the question.")

generate_cypher_query = dspy.ChainOfThought(QuestionToCypher)

class CypherToResponse(dspy.Signature):
    """Instructions:
    Generate a user-friendly response to the original question based on the query results."""

    question = dspy.InputField(desc="User's original question.")
    query_results = dspy.InputField(desc="Results of the Cypher query executed on the Neo4j database.")
    response = dspy.OutputField(desc="User-friendly response to the original question.")

generate_response = dspy.ChainOfThought(CypherToResponse)

if __name__ == "__main__":
    while True:
        try:
            # Step 1: Get user question
            question = input("\nEnter your question: ")

            # Step 2: Extract the schema from Neo4j
            schema = neo4j.fmt_schema()

            # Step 3: Generate Cypher query using the schema and question
            cypher = generate_cypher_query(question=question, neo4j_schema=schema)
            print(f"\nGenerated Cypher Query:\n{cypher.cypher_query}")

            # Step 4: Execute the Cypher query in Neo4j
            query_results = neo4j.query(cypher.cypher_query.replace('```', ''))
            print(f"\nQuery Results:\n{query_results}")

            # Step 5: Format query results for the LLM
            formatted_results = "\n".join([f"- {list(result.values())[0]}" for result in query_results])

            # Step 6: Generate a user-friendly response based on the query results
            response = generate_response(question=question, query_results=formatted_results)
            print(f"\nResponse:\n{response.response}")

        except Exception as e:
            print(f"Error: {e}")
            print("Please try again.")
            continue

        except KeyboardInterrupt:
            print("\nExiting...")
            break


# OUTPUT: 

# Enter your question: what are the dream destinations where alex want to visit ?

# Generated Cypher Query:
# ```
# MATCH (p:Person {name: 'Alex'})-[:DREAM_DESTINATION]->(d:Destination)
# RETURN d.name as Dream_Destinations
# ```

# Query Results:
# [{'Dream_Destinations': 'Japan'}, {'Dream_Destinations': 'Iceland'}, {'Dream_Destinations': 'New Zealand'}]

# Response:
# Alex's dream destinations to visit are Japan, Iceland, and New Zealand.





# Enter your question: what is the age of Alex ?

# Generated Cypher Query:
# ```cypher
# MATCH (p:Person {name: 'Alex'})
# RETURN p.age
# ```

# Query Results:
# [{'p.age': 28}]

# Response:
# Alex is 28 years old.