"""
Utility functions for link extraction and URL validation.
"""

def resolve_absolute_url(href: str, base_url: str = "https://books.toscrape.com/") -> str:
    """
    Cleans up and returns the resolved absolute URL string, or None if the link should be ignored.
    """
    if not href:
        return None
        
    href = href.strip()

    if not href or href.startswith("#") or href.startswith("javascript:"):
        return None
        
    if href.startswith("http://") or href.startswith("https://"):
        return href
 
    clean_href = href.replace("../", "")
    
    # Match layout path patterns to build the right destination
    if clean_href == "index.html":
        return f"{base_url}index.html"
    elif clean_href.startswith("catalogue/"):
        return f"{base_url}{clean_href}"
    else:
        return f"{base_url}catalogue/{clean_href}"