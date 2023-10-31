# Chatbot
## Installation
pip install -r requirement.txt

## Image 
![chatbot](https://github.com/mehrnazsalehi/chatbot/assets/149144017/d0803341-f07e-4ba6-b1c9-ec581a4c84c8)
## Movie


https://github.com/mehrnazsalehi/chatbot/assets/149144017/4e5fb4f8-471f-4f09-ae22-6204de52384e

A chatbot is an artificial intelligence-powered piece of software in a device (Siri, Alexa, Google Assistant, etc.), application, website, or other networks.
In retrieval-based models, a chatbot uses some heuristic to select a response from a library of predefined responses.
The chatbot uses the message and context of the conversation to choose the best response from a predefined list of bot messages.
The context can include a current position in the dialogue tree, all previous messages in the conversation, and previously saved variables (e.g., username).
Heuristics for selecting a response can be engineered in many different ways, from rule-based if-else conditional logic to machine learning classifiers.
## Building the Bot
### Pre-requisites
Hands-on knowledge of scikit library and NLTK is assumed. However, if you are new to NLP, you can still read the article and then refer back to resources.
### NLP 
NLTK(Natural Language Toolkit) is a leading platform for building Python programs to work with human language data.
It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification,
tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries.

### Downloading and installing NLTK
Install NLTK: run 
pip install nltk
Test installation: run python then type import nltk

### Installing NLTK Packages
import NLTK and run nltk.download().
This will open the NLTK downloader from where you can choose the corpora and models to download. You can also download all packages at once.
### Text Pre- Processing with NLTK
Tokenization
Removing Noise
Removing Stop words
Stemming
Lemmatization
### Bag of Words
After the initial preprocessing phase, we need to transform the text into a meaningful vector (or array) of numbers. 
The bag-of-words is a representation of text that describes the occurrence of words within a document. It involves two things:
•A vocabulary of known words.
•A measure of the presence of known words.
Why is it called a “bag” of words? That is because any information about the order or structure of words in the document is discarded,
and the model is only concerned with whether the known words occur in the document, not where they occur in the document.
The intuition behind the Bag of Words is that documents are similar if they have identical content. 
Also, we can learn something about the meaning of the document from its content alone.
For example, if our dictionary contains the words {Learning, is, the, not, great}, and we want to vectorize the text “Learning is great,” we would have the following vector:
return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]

### Reading in the data
with open('intents.json', 'r') as f:
    intents = json.load(f)
nltk.download('punkt') # first-time use only
Finally, we will feed the lines that we want our bot to say while starting and ending a conversation, depending upon the user’s input.

