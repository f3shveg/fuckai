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

    
def keywordss(test_text):
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
    sequence_to_classify = test_text
    candidate_labels = keywords
    output = classifier(sequence_to_classify, candidate_labels, multi_label=True,)
    print(output)

