from transformers import MBartTokenizer, MBartForConditionalGeneration
HF_DATASETS_OFFLINE=1 
HF_HUB_OFFLINE=1

def summary(sum_text):
    model_path = "/home/kali/1233/Models/mbart_ru_sum_gazeta"
    tokenizer = MBartTokenizer.from_pretrained(model_path)
    model = MBartForConditionalGeneration.from_pretrained(model_path,local_files_only=True)
    model.to("cpu")
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