from transformers import MBartTokenizer, MBartForConditionalGeneration
import torch
def summary(sum_text):
    model_name = "mbart_ru_sum_gazeta"
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    model.to(device)
    article_text = sum_text
    input_ids = tokenizer(
        [article_text],
        max_length=600,
        truncation=False,
        return_tensors="pt",
    )["input_ids"].to("cpu")
    print(input_ids)
    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]
    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary