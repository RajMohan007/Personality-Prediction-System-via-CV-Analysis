import re

# Sample CV text (replace with actual CV text)
cv_text = """
I am a highly motivated and enthusiastic individual with excellent problem-solving skills. 
I am known for my strong work ethic, attention to detail, and ability to work effectively in a team. 
In my previous role, I demonstrated leadership qualities by leading a project to successful completion. 
I am passionate about continuous learning and always eager to take on new challenges.
"""

# Define a dictionary of personality trait keywords
personality_traits = {
    'Motivated': ['motivated', 'enthusiastic', 'driven'],
    'Detail-Oriented': ['attention to detail', 'meticulous'],
    'Team Player': ['team player', 'collaborative', 'cooperative'],
    'Leadership': ['leadership', 'leader', 'initiative'],
    'Adaptable': ['adaptive', 'flexible', 'open to change'],
}

# Initialize a dictionary to store trait scores
trait_scores = {trait: 0 for trait in personality_traits}

# Tokenize the CV text into words
words = re.findall(r'\b\w+\b', cv_text.lower())

# Check for trait keywords in the CV text
for trait, keywords in personality_traits.items():
    for keyword in keywords:
        if keyword in words:
            trait_scores[trait] += 1

# Determine the personality trait with the highest score
predicted_personality_trait = max(trait_scores, key=trait_scores.get)

# Print the predicted personality trait
print("Predicted Personality Trait:", predicted_personality_trait)
