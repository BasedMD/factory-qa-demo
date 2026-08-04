def slugify(text):
    """Turn a title into a URL slug: lowercase, words joined by single hyphens."""
    return text.replace(" ", "-")
