import os
from openai import OpenAI
from mem0 import Memory



class AICodingAssistant:
    def __init__(self):
        """
        Initialize the AI Career Mentor with memory storage and OpenAI.
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = OpenAI()
        self.app_id = "coding-mentor"

    def get_coding_advice(self, query, user_id):
        """
        Provide career guidance and store past interactions for personalized advice.
        """
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "You are an AI coding assistant, helping with programming, debugging, and best practices."},
                {"role": "user", "content": query}
            ]
        )

        self.memory.add(query, user_id=user_id, metadata={"app_id": self.app_id})

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id):
        """
        Retrieve past career-related queries and suggestions.
        """
        return self.memory.get_all(user_id=user_id)

# Usage

user_id = "job_seeker_456"

ai_coding_assistant = AICodingAssistant()


def main():
    print("Welcome to your AI Coding Assistant! Ask me anything about programming, debugging, or best practices.")
    while True:
        question = input("Question: ")
        if question.lower() in ['q', 'exit']:
            print("Exiting... Happy coding!")
            break

        answer = ai_coding_assistant.get_coding_advice(question, user_id=user_id)
        print(f"Answer: {answer}")
        memories = ai_coding_assistant.get_memories(user_id=user_id)
        print("Previous Coding Discussions:")
        for memory in memories:
            print(f"- {memory}")
        print("-----")

if __name__ == "__main__":
    main()
