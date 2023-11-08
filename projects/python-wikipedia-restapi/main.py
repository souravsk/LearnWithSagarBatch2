from typing import Union
from fastapi import FastAPI
import wikipedia
import uvicorn
from textblob import TextBlob, Word
from wikilib.logic import summary_wiki, search_wiki, phrase_wiki, spellcheck_wiki, spellcorrect_wiki


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "WIKIPEDIA API. Call /search, /wiki, /phrase for more information."}


@app.get("/wiki/{name}")
async def wiki(name: str):
    try:
        wikipedia_summary = summary_wiki(name)
        return { "summary": wikipedia_summary }
    except wikipedia.exceptions.DisambiguationError as e:
        print("Try correct keyword to get better result")

@app.get("/search/{name}")
async def search(name: str):
    try:
        wikipedia_search_result = search_wiki(name)
        return { "summary": wikipedia_search_result }
    except Exception as e:
        print("We got an exception")


@app.get("/phrase/{name}")
async def phrase(name: str):
    try:
        return phrase_wiki(name)
    except Exception as e:
        print("We got an exception")

@app.get("/spellcorrect/{statement}")
async def spellcorrect(statement: str):
    try:
        return spellcorrect_wiki(statement)
    except Exception as e:
        print("We got an exception")

@app.get("/spellcheck/{statement}")
async def spellcheck(statement: str):
    try:
        return spellcheck_wiki(statement)
    except Exception as e:
        print("We got an exception")

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
