from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

try:
    with open("Modules/keyword_list.txt", "r") as keyword_file:
        lines = keyword_file.readlines()
        keywords = []
        for line in lines:
            line = line.strip()  # remove newline character
            if line:  # check if line is not empty
                keyword_list = line.split(", ")
                if keyword_list:  # check if keyword_list is not empty
                    keywords.append(keyword_list[0])
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print("An error occurred: ", str(e))
      
keywords = [keyword.strip('"') for keyword in keywords]       

    

from keybert import KeyBERT

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal).
         A supervised learning algorithm analyzes the training data and produces an inferred function,
         which can be used for mapping new examples. An optimal scenario will allow for the
         algorithm to correctly determine the class labels for unseen instances. This requires
         the learning algorithm to generalize from the training data to unseen situations in a
         'reasonable' way (see inductive bias).
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)