def resolve_current(records, key):
    """Resolve the current value for `key` from an append-only record log.

    Records are dicts: {"id": str, "key": str, "value": object | None,
    "ts": int, "supersedes": str | None}. A record with `supersedes` set
    marks the referenced record as superseded (corrections form chains).
    The current value for a key is the value of its LIVE record — the one
    no other record supersedes. A correction may WITHHOLD its replacement
    (value None); the current value is then None, and callers must treat
    it as unknown rather than fall back to stale data. Supersession links
    outrank timestamps (corrections can be backfilled with earlier ts).
    Returns None when no record matches `key`.
    """
    candidates = [r for r in records if r["key"] == key and r.get("value") is not None]
    if not candidates:
        return None
    return max(candidates, key=lambda r: r["ts"])["value"]
