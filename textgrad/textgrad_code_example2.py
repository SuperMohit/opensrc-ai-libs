import textgrad as tg
from rich.markdown import Markdown
from rich.console import Console

console = Console()

# Change the engine to Claude
tg.set_backward_engine("gpt-4o", override=True)

# Initialize Claude model instead of GPT-4
model = tg.BlackboxLLM('gpt-4o')

question_string = ("Write a function to find the longest common prefix among an array of strings. "
                  "If there is no common prefix, return an empty string. "
                  "Example 1: Input: ['flower', 'flow', 'flight'] → Output: 'fl' "
                  "Example 2: Input: ['dog', 'racecar', 'car'] → Output: '' "
                  "Provide a solution with optimal time complexity and explain your approach.")

question = tg.Variable(question_string,
                      role_description="question to the LLM",
                      requires_grad=False)

answer = model(question)

answer_text = str(answer.value)

console.print(Markdown(answer_text))





# OUTPUT 

# To solve the problem of finding the longest common prefix among an array of strings, we can use a        
# straightforward approach that is both efficient and easy to understand. The optimal solution involves    
# comparing characters of the strings in a vertical manner, which ensures that we only traverse each       
# character once, leading to a time complexity of O(S), where S is the sum of all characters in all        
# strings.

# Here's a step-by-step explanation of the approach:

#  1 Edge Case Handling: If the input array is empty, return an empty string immediately.
#  2 Initialize the Prefix: Start by assuming the first string in the array is the common prefix. This is a
#    reasonable assumption because the longest common prefix cannot be longer than the shortest string.    
#  3 Iterate Over the Strings: For each subsequent string in the array, compare it character by character  
#    with the current prefix. Update the prefix by trimming it to the length where the characters match.   
#  4 Early Termination: If at any point the prefix becomes an empty string, you can terminate early and    
#    return an empty string, as no common prefix exists.
#  5 Return the Result: After processing all strings, the remaining prefix is the longest common prefix.   

# Here's the implementation of the above approach in Python:

                                                                                                         
#  def longest_common_prefix(strs):
#      if not strs:
#          return ""
                                                                                                         
#      # Start with the first string as the initial prefix
#      prefix = strs[0]
                                                                                                         
#      # Compare the prefix with each string in the array
#      for string in strs[1:]:
#          # Update the prefix by comparing it with the current string
#          while string[:len(prefix)] != prefix and prefix:
#              # Trim the prefix by one character from the end
#              prefix = prefix[:-1]
                                                                                                         
#          # If the prefix becomes empty, return immediately
#          if not prefix:
#              return ""
                                                                                                         
#      return prefix
                                                                                                         
#  # Example usage:
#  print(longest_common_prefix(['flower', 'flow', 'flight']))  # Output: 'fl'
#  print(longest_common_prefix(['dog', 'racecar', 'car']))     # Output: ''
                                                                                                         

#                                      Explanation of Time Complexity:

#  • Time Complexity: O(S), where S is the total number of characters in all strings. In the worst case, we
#    might have to compare each character of each string with the prefix.
#  • Space Complexity: O(1), as we are using only a fixed amount of extra space for the prefix variable.   

# This approach efficiently finds the longest common prefix by leveraging the fact that the prefix can only
# get shorter as we compare it with more strings.