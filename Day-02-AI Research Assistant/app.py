#importing the libraries
import re
import urllib.parse
from typing import List

import requests
from bs4 import BeautifulSoup
from ollama import chat
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

default_url="https://en.wikipedia.org/wiki/Artificial_Intelligence"

#function for downloading the webpage

def fetch_page_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    session.mount("http://", HTTPAdapter(max_retries=retries))

    resp = session.get(url, headers=headers, timeout=15)
    if resp.status_code == 403 and "wikipedia.org" in url:
        # fallback to MediaWiki API
        try:
            title = url.rstrip("/").rsplit("/", 1)[-1]
            domain = url.split("/")[2]
            api = f"https://{domain}/w/api.php"
            params = {"action": "parse", "page": title, "prop": "text", "format": "json"}
            api_resp = session.get(api, headers=headers, params=params, timeout=15)
            api_resp.raise_for_status()
            data = api_resp.json()
            html = data["parse"]["text"]["*"]
            soup = BeautifulSoup(html, "html.parser")
        except Exception:
            resp.raise_for_status()  # re-raise original 403 if fallback fails
    else:
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = "\n".join(
        p.get_text(" ", strip=True)
        for p in soup.find_all(["p", "h1", "h2", "h3"])
    )
    text = re.sub(r"\s+", " ", text).strip()
    return text[:5000]


def build_prompt(question: str , content: str) -> List[dict]:
    return [
        {
            "role": "system",
            "content": "You are a helpful research assistant. Summarize the provided content clearly and concisely.",
        },
        {
            "role": "user",
            "content": f"Research question: {question}\n\nSource content: \n{content}",
        },
    ]

def get_summary(question: str, url: str) -> str:
    content=fetch_page_text(url)
    response=chat(
        model="phi3",
        messages=build_prompt(question, content),
    )
    return response["message"]["content"]

def search_wikipedia(query: str) -> str | None:
    """Return the top Wikipedia URL for query, or None if not found."""
    base_api = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 1,
    }
    resp = requests.get(base_api, params=params, timeout=10, headers={"User-Agent": "ai-research-assistant/1.0"})
    resp.raise_for_status()
    data = resp.json()
    results = data.get("query", {}).get("search", [])
    if not results:
        return None
    title = results[0]["title"]
    title_enc = urllib.parse.quote_plus(title.replace(" ", "_"))
    return f"https://en.wikipedia.org/wiki/{title_enc}"

def main() -> None:
    print("AI Research Assistant")

    question=input("Enter your research question: ").strip()
    if not question:
        question="What is this page about ??"

    url=input(f"enter a source URL (leave blank to auto-find): ").strip()
    if not url:
        url = search_wikipedia(question)
        if url:
            print(f"Auto-selected source: {url}")
        else:
            print("No Wikipedia match found. Please provide a URL or try a different question.")
            return

    print("\nFetching content and generating the summary.. \n")

    try:
        summary=get_summary(question,url)
        print(summary)
        print(url)
    except Exception as exc:
        print(exc)
        print("\nIf Ollama is not running, start it and make sure the phi3 model is available.")
    
if __name__ == "__main__":
    main()
