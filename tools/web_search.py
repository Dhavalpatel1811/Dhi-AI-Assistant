# tools/web_search.py — DuckDuckGo web search tool

from ddgs import DDGS
from datetime import datetime


def web_search(query: str, max_results: int = 6) -> str:
    """
    Search the web using DuckDuckGo.
    Returns a clean, well formatted string of results for the LLM.
    """
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append({
                    "title": r.get("title", "").strip(),
                    "snippet": r.get("body", "").strip(),
                    "url": r.get("href", "").strip()
                })

        if not results:
            return f"No web results found for '{query}'. Please try a different search query."

        # Current timestamp so LLM knows data is fresh
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        formatted = f"[Web Search Results — {timestamp}]\n"
        formatted += f"Query: '{query}'\n"
        formatted += f"{'='*50}\n\n"

        for i, r in enumerate(results, 1):
            formatted += f"Result {i}: {r['title']}\n"
            formatted += f"{r['snippet']}\n"
            formatted += f"Source: {r['url']}\n"
            formatted += f"{'-'*40}\n\n"

        formatted += "IMPORTANT: Use the above search results to answer the user. Trust this data over your training knowledge as it is current and real-time.\n"

        return formatted

    except Exception as e:
        return f"Search failed with error: {str(e)}. Please try again."