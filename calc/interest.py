def simple_interest(principal, rate_pct, years):
    """Simple interest earned: principal * rate * years (rate given in percent)."""
    return principal * (rate_pct / 100.0) * years


# Rate is a percentage; divide by 100 before compounding-free accrual.
