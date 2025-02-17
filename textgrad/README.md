<p align="center">
    <h1 align="center">TextGrad</h1> 
</p>

`TextGrad` is a framework for `gradient-based optimization of text prompts` used in large language models (LLMs). It helps refine prompts automatically instead of relying on manual engineering.

`Gradient-based optimization` means that instead of relying on trial and error, TextGrad `treats prompts as trainable parameters` and refines them using differential objectives to improve performance.

Unlike human engineering where we have to `manually tweak and test prompts` which is time-consuming, inconsistent and non-optimal.

We can understand this by the `example` given below.

## Installation

```bash
pip install textgrad
```

## QuickStart

Let us understand with a simple example using GPT-4o to solve a simple reasoning problem.

```python
import textgrad as tg

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
```

> :warning: **To solve this problem, we need to understand the relationship between the number of painters, the time it  
> takes to paint the wall, and the work done.** > **1 Determine the total work done in painter-hours:**
> • If 3 painters can paint the wall in 4 hours, the total work required to paint the wall is calculated  
>  as: [ \text{Total work} = \text{Number of painters} \times \text{Time} = 3 \text{ painters} \times 4\text{ hours} = 12 \text{ painter-hours} ]
> • This means it takes 12 painter-hours to complete the job.
> **2 Calculate the time it takes for 6 painters:**
> • Now, we have 6 painters working on the same wall. We need to find out how long it will take them to  
>  complete the same 12 painter-hours of work.
> • Let ( t ) be the time in hours it takes for 6 painters to paint the wall. The equation for the total  
>  work done is: [ 6 \text{ painters} \times t \text{ hours} = 12 \text{ painter-hours} ]
> • Solving for ( t ), we divide both sides by 6: [ t = \frac{12 \text{ painter-hours}}{6 \text{painters}} = 2 \text{ hours} ]
>
> **Therefore, it would take 6 painters 2 hours to paint the same wall.**

As we can see the answer is too long and without optimization. We can optimize the answer using TextGrad.

```python
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
```

```python
# Step 3: Compute loss and update answer
loss= loss_fn(answer)
loss.backward()
optimizer.step()
print(answer)
```

> :white_check_mark: ** answer: 6 painters would take 2 hours to paint the same wall. Here's why: If 3 painters take 4 hours, the total work is 12 painter-hours (3 painters × 4 hours). With 6 painters, divide the total work by the number of painters: 12 painter-hours ÷ 6 painters = 2 hours.**

### Explanation :

1. Initial Answer Generation
   GPT-4o generates a first attempt at solving the math problem.

2. Setting up gradient-based optimization

```python
answer.set_role_description("concise and accurate answer to the question")

optimizer = tg.TGD(parameters=[answer])
```

The `set_role_description` function `clarifies what the answer should be`, guiding optimization process.

`tg.TGD` is an `optimizer` that will adjust the `answer` based on computed gradients.

3. Defining the Loss Function

```python
evaluation_instruction= (f"Here's a question: {question_string}. "
                           "Evaluate any given answer to this question, "
                           "be smart, logical, and very critical. "
                           "Just provide concise feedback.")

loss_fn= tg.TextLoss(evaluation_instruction)
```

The `evaluation instruction` describes how the answer should be graded.

`tg.TextLoss(evaluation_instruction)` acts as a `loss function`, where the model will evaluate the answer based on `accuracy, reasoning, and completeness`.

This `loss guides the optimizer` to improve the answer iteratively.

4. Computing the loss and updating the answer

```python
loss= loss_fn(answer)
loss.backward()
optimizer.step()
```

The `loss is computed` by evaluating how well the generated answer follows the given criteria.

`.backward()` computes `gradients`, determining how to improve the answer.

`optimizer.step()` updates the answer based on the computed gradients.
