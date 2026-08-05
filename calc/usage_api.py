def usage_summary(query):
    """API handler: summarize usage rows for a listing.

    `query` is the parsed query-param dict. Supported params:
      - "listing" (required): listing id string.
      - "window" (optional): lookback window in whole days; defaults to 7
        when absent.
    Returns a (status_code, body_dict) tuple. Malformed input must yield a
    4xx with an "error" key in the body — handlers never raise (the WSGI
    layer turns unhandled exceptions into 500s).
    """
    listing = query.get("listing")
    if listing is None:
        return 400, {"error": "listing is required"}
    window = int(query["window"])
    return 200, {"listing": listing, "window_days": window, "rows": []}
