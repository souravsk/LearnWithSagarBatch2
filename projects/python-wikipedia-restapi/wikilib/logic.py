from typing import Union

from fastapi import FastAPI
import wikipedia
import uvicorn
from textblob import TextBlob, Word

def summary_wiki(name: str):
    try:
        wikipedia_summary = wikipedia.summary(name)
        return wikipedia_summary
    except wikipedia.exceptions.DisambiguationError as e:
        print("Try correct keyword to get better result")


def search_wiki(name: str):
    try:
        wikipedia_search_result = wikipedia.search(name)
        return wikipedia_search_result
    except Exception as e:
        print("We got an exception")


def phrase_wiki(name: str):
    try:
        blob = TextBlob(name)
        return blob.noun_phrases
    except Exception as e:
        print("We got an exception")

def spellcorrect_wiki(statement: str):
    try:
        correctword = Word(statement)
        return correctword.correct()
    except Exception as e:
        print("We got an exception")

def spellcheck_wiki(statement: str):
    try:
        correctword = Word(statement)
        return correctword.spellcheck()
    except Exception as e:
        print("We got an exception")
