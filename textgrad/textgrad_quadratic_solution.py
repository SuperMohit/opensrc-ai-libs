import textgrad as tg

tg.set_backward_engine("gpt-4o")

initial_solution = """To solve the equation 3x^2 - 7x + 2 = 0, we use the quadratic formula:
x = (-b ± √(b^2 - 4ac)) / 2a
a = 3, b = -7, c = 2
x = (7 ± √((-7)^2 - 4 * 3(2))) / 6
x = (7 ± √(7^3) / 6
The solutions are:
x1 = (7 + √73)
x2 = (7 - √73)"""

# Define the variable to optimize, let requires_grad=True to enable gradient computation
solution = tg.Variable(initial_solution,
                       requires_grad=True,
                       role_description="solution to the math question")

# Define the optimizer, let the optimizer know which variables to optimize, and run the loss function

loss_fn = tg.TextLoss("You will evaluate a solution to a math question. Do not attempt to solve it yourself, do not give a solution, only identify errors. Be super concise.")

optimizer = tg.TGD(parameters=[solution])
loss = loss_fn(solution)

# print(loss)

loss.backward()
optimizer.step()
print(solution.value)





# OUTPUT 

# To solve the equation 3x^2 - 7x + 2 = 0, we use the quadratic formula:
# x = (-b ± √(b^2 - 4ac)) / 2a
# where a = 3, b = -7, c = 2.

# First, calculate the discriminant:
# b^2 - 4ac = (-7)^2 - 4 * 3 * 2 = 49 - 24 = 25.

# Now, substitute into the quadratic formula:
# x = (7 ± √25) / 6.

# The solutions are:
# x1 = (7 + 5) / 6 = 12 / 6 = 2,
# x2 = (7 - 5) / 6 = 2 / 6 = 1/3.

# Therefore, the correct solutions are x1 = 2 and x2 = 1/3.