from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

def keywords(test_text):
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
    sequence_to_classify = test_text
    candidate_labels = ["хорошо", "плохо", "war", "животные", "technology"]
    output = classifier(sequence_to_classify, candidate_labels, multi_label=False,)

