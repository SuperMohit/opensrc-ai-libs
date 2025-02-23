import os
from openai import OpenAI
from mem0 import Memory


class PersonalAIHealthCoach:
    def __init__(self):
        """
        Initialize the PersonalAIHealthCoach with memory configuration and OpenAI client.
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
        self.app_id = "health-coach"

    def track_progress(self, user_input, user_id=None):
        """
        Store health-related interactions and provide personalized fitness/wellness advice.
        """
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "You are a personal AI health coach, providing fitness and wellness guidance."},
                {"role": "user", "content": user_input}
            ]
        )

        self.memory.add(user_input, user_id=user_id, metadata={"app_id": self.app_id})

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve past health records and progress.
        """
        return self.memory.get_all(user_id=user_id)

# Usage
health_coach = PersonalAIHealthCoach()
user_id = "fitness_enthusiast"

# Track health progress
health_coach.track_progress("I did a 5km run today. What should I do next?", user_id=user_id)

# Fetching Memories
memories = health_coach.get_memories(user_id=user_id)
print("memories are printed here")
for m in memories:
    print(m['memory'])


# OUTPUT 

# Good job on your run today! It's important to replenish your body after a workout. You can start by cooling down with some stretches to prevent muscle soreness and stiffness. 

# Next, have a balanced meal or snack that includes both protein and carbohydrates. This could be something like grilled chicken with brown rice or a protein shake with a banana. The protein will help repair and build muscles, while the carbs will help replenish your energy stores.

# Also, remember to hydrate your body. Water is a great option, but you can also consider drinks with electrolytes if you sweated heavily.

# If you're planning your next workout, consider cross-training which involves a different type of exercise. This allows different muscle groups to work and recover, reducing the risk of injury. For instance, if you ran today, you might want to consider swimming or cycling next, or doing strength training.

# Rest is just as important in any fitness routine to allow your body to recover, so make sure you're getting adequate sleep as well.

# And last but not least, listen to your body. If you're feeling exceptionally tired or sore, give yourself permission to take a rest day. Your body will thank you for it. 

# Remember, consistency in your workouts is more important than intensity. Gradually increase the distance or pace of your runs instead of pushing too hard all at once.

# Body weight is about 70kg
# Did a 5km run today