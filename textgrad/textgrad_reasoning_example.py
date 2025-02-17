import textgrad as tg
from rich.markdown import Markdown
from rich.console import Console

console= Console()

tg.set_backward_engine("gpt-4o", override=True)

# Step 1: Get an initial response from an LLM for the question.
model= tg.BlackboxLLM('gpt-4o')

question_string = ("If 3 painters can paint a wall in 4 hours, "
                   "how long would it take 6 painters to paint the same wall? "
                   "Assume all painters work at the same rate. "
                   "Reason step by step")

# Create variable for the question
question= tg.Variable(question_string,
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
evaluation_instruction= (f"Here's a question: {question_string}. "
                           "Evaluate any given answer to this question, "
                           "be smart, logical, and very critical. "
                           "Just provide concise feedback.")

# Create loss function for the question
loss_fn= tg.TextLoss(evaluation_instruction)


# Step 3: Compute loss and update answer
loss= loss_fn(answer)
loss.backward()
optimizer.step()

print("Final answer of the question is:")
print(answer)






# Final OUTPUT:  

# Final answer of the question is:
# 6 painters would take 2 hours to paint the same wall. Here's why: If 3 painters take 4 hours, the total work is 12 painter-hours (3 painters × 4 hours). With 6 painters, divide the total work by the number of painters: 12 painter-hours ÷ 6 painters = 2 hours.



# Output Before step 2 and 3:  

# To solve this problem, we need to understand the relationship between the number of painters, the time it   
# takes to paint the wall, and the work done.

#  1 Determine the total work done in painter-hours:
#     • If 3 painters can paint the wall in 4 hours, the total work required to paint the wall is calculated  
#       as: [ \text{Total work} = \text{Number of painters} \times \text{Time} = 3 \text{ painters} \times 4  
#       \text{ hours} = 12 \text{ painter-hours} ]
#     • This means it takes 12 painter-hours to complete the job.
#  2 Calculate the time it takes for 6 painters:
#     • Now, we have 6 painters working on the same wall. We need to find out how long it will take them to   
#       complete the same 12 painter-hours of work.
#     • Let ( t ) be the time in hours it takes for 6 painters to paint the wall. The equation for the total  
#       work done is: [ 6 \text{ painters} \times t \text{ hours} = 12 \text{ painter-hours} ]
#     • Solving for ( t ), we divide both sides by 6: [ t = \frac{12 \text{ painter-hours}}{6 \text{
#       painters}} = 2 \text{ hours} ]

# Therefore, it would take 6 painters 2 hours to paint the same wall.


