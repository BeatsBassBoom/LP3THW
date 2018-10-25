# Learning to Speak Object Oriented
'''
Words
class - Tell Python to make a new type of thing.
object - Two meanings: the most basic type of thing, and any instance of some thing.
instance - What you get when you tell Python to create a class.
def - How you define a function inside a class.
self - Inside the fucntion in a class, self is a variable for the instance/object being accessed.
inheritance - The concept that one class can inherit traits from another class, much like you and your parents.
composition - The concept that a class can be composed of other classes as parts, much like how a car has wheels.
attribute - A property classes have that are from composition and are usually variables.
is-a - A phrase to say that something inherits from another, as in a "salmon" is a "fish".
has-a - A phrase to say that something is composed of other things or has a trait, as in "salmon has a mounth".

Phrases
class X(Y) ”Make a class named X that is-a Y.”
class X(object): def __init__(self, J) ”class X has-a __init__ that takes self and J parameters.”
class X(object): def M(self, J) ”class X has-a function named M that takes self and J parameters.” foo = X() ”Set foo to an instance of class X.”
foo.M(J) ”From foo, get the M function, and call it with parameters self, J.”
foo.K = Q ”From foo, get the K attribute, and set it to Q.”
'''


'''
Ansible Analysis
1. For each class give its name and what other classes it inherits from.
2. Under that, list every function it has and the parameters they take.
3. List all of the attributes it uses on its self.
4. For each attribute, give the class this attribute is.

1.
classes =
2.
    ResultsCollector
    __init__(self,args,kwargs)
    v2_runner_on_unreachable(self,result)
    v2_runner_on_unreachable(self,result)
    v2_runner_on_ok(self,result,args,kwargs)
    v2_runner_on_failed(self,result,args,kwargs)
3.
self.host_ok
self.host_unreachable
self.host_failed

4.
ResultsCollector
'''


import random
from urllib.request import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"

WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***,***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***,*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)            
        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")

    