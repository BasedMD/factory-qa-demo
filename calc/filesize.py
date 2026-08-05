_SUFFIXES = ["kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]


def natural_size(num_bytes):
    """Human-readable DECIMAL (base-1000) size string for a non-negative int.

    Values below 1000 render in bytes ("999 B"). Unit-suffixed values render
    with one decimal place ("1.5 kB"). Rollover happens exactly at each power
    of 1000 for integer inputs of ANY magnitude: exactly 1000**8 bytes is
    "1.0 YB" — never "1000.0 ZB". Values past the top suffix stay in the top
    suffix ("1000.0 YB" and up).
    """
    if num_bytes < 1000:
        return f"{num_bytes} B"
    size = float(num_bytes)
    for suffix in _SUFFIXES:
        size /= 1000.0
        if size < 1000.0:
            return f"{size:.1f} {suffix}"
    return f"{size:.1f} {_SUFFIXES[-1]}"
