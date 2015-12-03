# RelatedWordsBot

https://twitter.com/relatedwordsbot

ReverseImageBot is a Twitter bot that creates generative art content utilizing Bing Image Search and a dictionary of related words.

RelatedWordsBot works as follows:

1.	Selects a random word from a list of all words in the English language.

2.	Performs a Bing Image Search using the randomly generated word as the search term and uploads the first image result to Twitter.

3.	Retrieves the word used to generate the image uploaded most recently to the Twitter account and uses a dictionary database to generate a related word from that word.

4.	Performs a Bing Image Search using the related word as the search term and retrieves the first image result.

5.	Using the image just retrieved and the image uploaded most recently to the Twitter account, merges the two images together using an overlay, and uploads the generated image to Twitter.

6.	Repeats steps 3 – 5. Stops when no related word can be found for the given word or the related word generated is a word that was previously generated.


RelatedWordsBot exists as two Python scripts, “RelatedWordsBot_initialization.py” and “RelatedWordsBot_search&combine.py”. “RelatedWordsBot_initialization.py” initializes the system by generating a random word and image from that word. “RelatedWordsBot_search&combine.py” runs repeatedly and generated new words and images from the previous content. 
