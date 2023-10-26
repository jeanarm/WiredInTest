#Define the function
def can_form_chain(words):
    if not words:
        return "No"

    # Check if each word is a valid word (1 to 8 characters without spaces).
    if any(len(word) < 1 or len(word) > 8 or ' ' in word for word in words):
        return "No"

    # Create a list to keep track of used words.
    used_words = [False] * len(words)

    # Start from the first word and try to form a chain.
    chain = [words[0]]
    used_words[0] = True

    for _ in range(len(words) - 1):
        last_letter = chain[-1][-1]
        next_word_index = next((i for i, word in enumerate(words) if not used_words[i] and word[0] == last_letter), None)
        if next_word_index is not None:
            chain.append(words[next_word_index])
            used_words[next_word_index] = True
        else:
            return "No"  # Chain cannot be completed.

    if chain[0][0] == chain[-1][-1]:
        return "Yes", ' '.join(chain)
    else:
        return "No"

# Testing the function with the words that can make a chain
canMakeChain = ["elephant", "tigerlil", "llamaana", "antelope"]
result1, chain = can_form_chain(canMakeChain)
print("Can form Chain:", result1)
if result1 == "Yes":
    print("Chain of words:", chain)

# Checking the function with the words that cannot make a chain
canNotMakeChain = ["rainfall", "firewood", "baseball", "football"]
result2= can_form_chain(canNotMakeChain)
print("Can form Chain:", result2)

