class Solution(object):
    def findWords(self, words):
        # Define the 3 rows of the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # Initialize the result list
        result = []
        
        # Iterate through each word in the input list
        for word in words:
            # Convert the word to lowercase to handle case insensitivity
            lowercase_word = word.lower()
            
            # Check if all characters of the word are in one of the rows
            if all(char in row1 for char in lowercase_word):
                result.append(word)
            elif all(char in row2 for char in lowercase_word):
                result.append(word)
            elif all(char in row3 for char in lowercase_word):
                result.append(word)
        
        # Return the final result after processing all words
        return result