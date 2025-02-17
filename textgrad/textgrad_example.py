import textgrad as tg
from rich.markdown import Markdown
from rich.console import Console

console = Console()

tg.set_backward_engine("gpt-4o", override=True)

# Step 1: Get an initial response from an LLM for the question.
model= tg.BlackboxLLM('gpt-4o')

question_string = ("A train travels from City A to City B at 60 mph and returns at 40 mph. "
                  "If the total journey takes 5 hours, what is the distance between the cities? "
                  "Solve this step by step, explaining your reasoning.")

# Create variable for the question
question = tg.Variable(question_string,
                       role_description="question to the LLM",
                       requires_grad=False)

# Get answer for the question
answer= model(question)

# answer_text= str(answer.value)

# console.print(Markdown(answer_text))

answer.set_role_description("concise and accurate answer to the question")

# Step 2: Define optimizer for the answer
optimizer = tg.TGD(parameters=[answer])

# Evaluation instruction for the question
evaluation_instruction = (f"Here's a question: {question_string}. "
    "Evaluate the answer based on:\n"
    "1. Mathematical accuracy - Are all calculations and formulas correct?\n"
    "2. Problem setup - Are variables and equations properly defined?\n"
    "3. Solution steps - Is the reasoning clear and logically connected?\n"
    "4. Final answer - Is it complete with proper units and context?\n"
    "Provide specific feedback on errors or improvements needed.")

# Create loss function for the question
loss_fn= tg.TextLoss(evaluation_instruction)

# Step 3: Compute loss and update answer
loss= loss_fn(answer)
loss.backward()
optimizer.step()

answer_text = str(answer.value)

console.print(Markdown(answer_text))



# Final Output 

# To find the distance between City A and City B, given the speeds and total travel time, we can set up   
# the following equation:

# Let ( d ) be the distance between the cities. The time taken from City A to City B is ( \frac{d}{60} )  
# hours, and the return time is ( \frac{d}{40} ) hours. The total journey time is 5 hours, so:

# [ \frac{d}{60} + \frac{d}{40} = 5 ]

# Finding a common denominator (120) and solving for ( d ):

# [ \frac{2d}{120} + \frac{3d}{120} = 5 \quad \Rightarrow \quad \frac{5d}{120} = 5 ]

# Multiply both sides by 120:

# [ 5d = 600 \quad \Rightarrow \quad d = 120 ]

# Thus, the distance between City A and City B is 120 miles. Understanding such problems is useful in     
# real-world travel planning. An alternative approach could involve calculating the average speed for the 
# round trip.





# OUTPUT 

# To solve this problem, we need to determine the distance between City A and City B, given the speeds and total travel time.

# Let's denote the distance between the two cities as ( d ).

#  1 Calculate the time taken for each leg of the journey:
#     • From City A to City B:
#        • Speed = 60 mph
#        • Distance = ( d )
#        • Time = Distance / Speed = ( \frac{d}{60} ) hours
#     • From City B to City A:
#        • Speed = 40 mph
#        • Distance = ( d )
#        • Time = Distance / Speed = ( \frac{d}{40} ) hours
#  2 Set up the equation for the total journey time:
#    The total time for the round trip is given as 5 hours. Therefore, we can write the equation:
#    [ \frac{d}{60} + \frac{d}{40} = 5 ]
#  3 Find a common denominator and solve for ( d ):
#    The common denominator for 60 and 40 is 120. Rewrite the equation with this common denominator:
#    [ \frac{d}{60} = \frac{2d}{120} \quad \text{and} \quad \frac{d}{40} = \frac{3d}{120} ]
#    Substitute these into the equation:
#    [ \frac{2d}{120} + \frac{3d}{120} = 5 ]
#    Combine the fractions:
#    [ \frac{5d}{120} = 5 ]
#  4 Solve for ( d ):
#    Multiply both sides by 120 to clear the fraction:
#    [ 5d = 600 ]
#    Divide both sides by 5:
#    [ d = 120 ]

# Thus, the distance between City A and City B is 120 miles.