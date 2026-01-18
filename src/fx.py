# fx.py
# Simple FX module with a fixed USD→GBP exchange rate

def get_fx_rate():
    """
    Returns a fixed USD to GBP exchange rate.
    This avoids external API calls so the GitHub Action
    can run without network or authentication failures.
    """

    # Hard‑coded rate as of 18 Jan 2026
    return 0.75
