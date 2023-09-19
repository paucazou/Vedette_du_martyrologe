import re
with open('fr_martyrology.txt') as f:
    text = f.read()

def most_used_words(text, exclude):
  """Returns a list of the 100 most used words starting with a Capital letter in a string, excluding a list of words.

  Args:
    text: A string.
    exclude: A list of words to exclude.

  Returns:
    A list of the 100 most used words starting with a Capital letter in the string, excluding the list of words.
  """

  # Split the text into words.
  words = re.split(r'\W+', text)
  exclude = exclude.split()

  # Create a dictionary to store the word counts.
  word_counts = {}
  for word in words:
    if not word:
        continue
    if word[0].isupper() and word not in exclude:
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1

  # Sort the dictionary by word count, in descending order.
  sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

  # Return the top 100 words.
  return sorted_word_counts

ex= "À En Le Il Au Comme Sans Sous Dans Ordre Saint Sa Après De Durant Église Foi L IX XIII Par Ils XI Près Mineurs Pour Chrétiens Elle On Congrégation Grand XII Apostat Les Apôtres Vierge La Son Frères Ier Avec Mère Pendant Mont Célèbre Chrétienne Chrétien Catholique Sainte Évangile Saints Apôtre Compagnie"
for i, x in enumerate(most_used_words(text, ex)):
    print(f"{i+1}: {x[0]} - {x[1]}")
