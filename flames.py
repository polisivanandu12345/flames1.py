#!/usr/bin/env python
# coding: utf-8

# In[1]:


def flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    common_letters = set(name1) & set(name2)

    # Remove common letters from both names
    for letter in common_letters:
        name1 = name1.replace(letter, "", 1)
        name2 = name2.replace(letter, "", 1)

    total_letters = len(name1) + len(name2)
    flames_letters = "FLAMES"

    # Perform FLAMES algorithm to get the relationship status
    while len(flames_letters) > 1:
        idx = (total_letters % len(flames_letters)) - 1
        flames_letters = flames_letters[:idx] + flames_letters[idx + 1:]

    relationship_status = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return relationship_status[flames_letters]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
relationship = flames(name1, name2)
print(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {relationship}")


# In[ ]:




