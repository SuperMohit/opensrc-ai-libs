import textgrad as tg
from rich.markdown import Markdown
from rich.console import Console

console = Console()

tg.set_backward_engine("claude-3-opus-20240229", override=True)

model = tg.BlackboxLLM('claude-3-opus-20240229')

question_string = ("Write a function to find the first non-repeated character in a string. "
                  "For example, if the input string is 'leetcode', return 'l'. "
                  "If the input string is 'loveleetcode', return 'v'. "
                  "If every character repeats, return None. "
                  "Optimize your solution for time complexity.")


question = tg.Variable(question_string,
                      role_description="question to the LLM",
                      requires_grad=False)

answer = model(question)

answer_text = str(answer.value)

console.print(Markdown(answer_text))






# OUTPUT 

# Here's an optimized solution to find the first non-repeated character in a string:


#  def firstNonRepeatedChar(s):
#      char_count = {}

#      # Count the occurrences of each character
#      for char in s:
#          char_count[char] = char_count.get(char, 0) + 1

#      # Find the first character with count 1
#      for char in s:
#          if char_count[char] == 1:
#              return char
                                                                                                           
#      return None
                                                                                                           

# Explanation:

#  1 We start by creating an empty dictionary called char_count to store the count of each character in the  
#    string.
#  2 We iterate through each character in the string using a for loop. For each character, we update its     
#    count in the char_count dictionary. If the character is not already in the dictionary, we initialize its
#    count to 0 using the get() method and then increment it by 1. If the character is already in the        
#    dictionary, we simply increment its count by 1.
#  3 After counting the occurrences of each character, we iterate through the string again using another for 
#    loop. This time, we check the count of each character in the char_count dictionary. If the count of a   
#    character is 1, it means it is the first non-repeated character, so we return that character.
#  4 If we have iterated through the entire string and haven't found any character with a count of 1, it     
#    means every character repeats. In this case, we return None.

# Time Complexity:

#  • The first for loop iterates through the string once to count the occurrences of each character, which   
#    takes O(n) time, where n is the length of the string.
#  • The second for loop also iterates through the string once to find the first non-repeated character,     
#    which takes O(n) time.
#  • Therefore, the overall time complexity of this solution is O(n), as we iterate through the string twice.

# Space Complexity:

#  • The space complexity is O(k), where k is the number of unique characters in the string. In the worst    
#    case, all characters in the string are unique, so the space complexity would be O(n), where n is the    
#    length of the string.

# This solution optimizes the time complexity by using a dictionary to count the occurrences of each
# character, allowing us to find the first non-repeated character in a single pass through the string.
