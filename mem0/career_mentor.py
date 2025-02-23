import os
from openai import OpenAI
from mem0 import Memory



class AICareerMentor:
    def __init__(self):
        """
        Initialize the AI Career Mentor with memory storage and OpenAI.
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333,
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = OpenAI()
        self.app_id = "career-mentor"

    def get_career_advice(self, query, user_id=None):
        """
        Provide career guidance and store past interactions for personalized advice.
        """
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "You are an AI career mentor, helping with resume building, job search, and interviews."},
                {"role": "user", "content": query}
            ]
        )

        self.memory.add(query, user_id=user_id, metadata={"app_id": self.app_id})

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve past career-related queries and suggestions.
        """
        return self.memory.get_all(user_id=user_id)

# Usage
career_mentor = AICareerMentor()
user_id = "job_seeker_456"

# Ask for career guidance
career_mentor.get_career_advice("Can you suggest some skills I should learn for a software engineer role?", user_id=user_id)

# Fetching Memories
memories = career_mentor.get_memories(user_id=user_id)
print("memories are printed here")
for m in memories:
    print(m['memory'])





# OUTPUT 

# Certainly, here are some key skills you should focus on for a Software Engineer role:

# 1. Programming Languages: Depending on what you will be developing, learning programming languages is a must. Some of the most popular and in-demand languages are Python, Java, JavaScript, C++, C#, Ruby, etc.

# 2. Code Versioning Tools: Familiarize yourself with tools like Git, Mercurial or SVN. These are essential for any programming job.

# 3. Databases: Understanding database management (SQL, Oracle, etc.) is important, as well as being familiar with NoSQL databases like MongoDB.

# 4. Web Development: For many roles, proficiency in HTML, CSS, and JavaScript, as well as frameworks like React, AngularJS, or Vue.js, are necessary.

# 5. Problem-Solving Skills: Being able to identify, analyze, and solve problems is probably the most important skill for any software engineer.

# 6. Backend Frameworks: Node.js, Django, Ruby on Rails, or Laravel, will add a great value to your portfolio.

# 7. Understanding of Algorithms and Data Structures: Knowledge of these is crucial, as they form the basis of programming.

# 8. Soft Skills: Though not specific to software engineering, communication, teamwork, adaptability, and time management are all key skills to have.

# 9. Testing: Familiarity with test-driven development and able to write unit tests and UI tests. Tools can include Jest, Mocha, Jasmine, etc.

# 10. Agile Methodologies: Many companies use agile development methods, so understanding Agile/Scrum can be very beneficial. 

# Remember that the specific skills you'll need to focus on will depend on the particular job you're interested in, so always carefully read job postings and tailor your skill set accordingly.