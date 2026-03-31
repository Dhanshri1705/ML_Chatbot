import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader
def get_links():
    url = "https://www.geeksforgeeks.org/machine-learning/machine-learning/"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.find_all("a", href=True):
        link = a["href"]
        if "machine-learning" in link:
            links.append(link)

    return list(set(links))


def load_documents():
    links = get_links()
    docs = []

    print(f"🔗 Total links found: {len(links)}")
    print("📥 Loading content from first 20 links...\n")

    for link in links[:20]:   # LIMIT
        try:
            print(f"Loading: {link}")
            loader = WebBaseLoader(link)
            docs.extend(loader.load())
        except Exception as e:
            print(f"Skipped: {link}")

    print(f"\n✅ Total documents loaded: {len(docs)}")
    return docs


if __name__ == "__main__":
    load_documents()