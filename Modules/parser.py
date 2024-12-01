import spacy
from spacy import displacy
from bs4 import BeautifulSoup
import requests

# Load the English language model
nlp = spacy.load("ru_core_news_md")

def fetch_news_article(url):
    """
    Fetch the news article from the given URL
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_element = soup.find('div', {'class': 'article__body'})
    if article_element:
        article = article_element.text
    else:
        article = "Failed to find article content"
    return article

def parse_news_article(article):
    """
    Parse the news article and extract title, entities, and keywords
    """
    doc = nlp(article)
    
    # Extract title
    title = [sent.text for sent in doc.sents][0]
    
    # Extract entities
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    
    # Extract keywords
    keywords = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    
    return title, entities, keywords

# Example usage
import Note_modules  # Assuming this is the module you want to use

# Example usage
url = "https://www.vedomosti.ru/business/articles/2024/10/03/1066145-pivovarennaya-kompaniya-osporila-zapret-na-halyalnie-energetiki"  # Replace with a real URL
article = fetch_news_article(url)
if article != "Failed to find article content":
    title, entities, keywords = parse_news_article(article)
    print("Title:", title)
    print("Entities:")
    for entity in entities:
        print(f"  {entity[0]} ({entity[1]})")
    print("Keywords:")
    for keyword in keywords:
        print(f"  {keyword}")

    # Create a note using note_modules
    note_title = title
    note_content = f"Entities: {', '.join([entity[0] for entity in entities])}\nKeywords: {', '.join(keywords)}"
    Note_modules.CreateNote(note_title)
    Note_modules.WriteToNote(note_content)
else:
    print("Failed to parse article")