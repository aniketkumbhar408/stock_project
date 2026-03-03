from nsetools import Nse
from csv import writer
import os


nse = Nse()

BASE_DIR = os.path.dirname(__file__)
SECTOR_MAPPING_FILE = os.path.join(BASE_DIR, "symbol_sector_mapping.txt")


def _get(d, *keys):
    for k in keys:
        if k in d:
            return d[k]
    return None


def _parse_pct(val):
    """
    Convert a percentage-like value (e.g. '2.34', '2.34%', 2.34) to float.
    Returns None if parsing fails.
    """
    if val is None:
        return None
    try:
        s = str(val).replace('%', '').strip()
        return float(s)
    except (ValueError, TypeError):
        return None


def _load_sector_mapping():
    """
    Load symbol->sector mapping from symbol_sector_mapping.txt (tab-separated).
    Returns a dict with UPPERCASE symbols as keys.
    """
    mapping = {}
    if not os.path.exists(SECTOR_MAPPING_FILE):
        return mapping

    with open(SECTOR_MAPPING_FILE, "r", encoding="utf-8") as f:
        # Skip header
        next(f, None)
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            symbol, sector = parts[0].strip(), parts[1].strip()
            if symbol:
                mapping[symbol.upper()] = sector
    return mapping


SECTOR_MAP = _load_sector_mapping()


def _get_sector(symbol):
    """
    Get sector for a symbol from pre-seeded mapping file.
    Returns sector string or None if not found.
    """
    if not symbol:
        return None
    return SECTOR_MAP.get(str(symbol).upper())


header = [
    'Stock name',
    'Sector',
    '% change',
    'Open price',
    'High price',
    'Low price',
    'Volume',
    'Ltp',
]

# top gainers
top_gainers = nse.get_top_gainers()

with open('topGainers.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(header)

    for r in top_gainers:
        pct_change = _get(r, 'perChange', 'pChange', 'percentChange', 'p_change')
        pct_val = _parse_pct(pct_change)
        # Only include stocks with absolute % change below 3%
        if pct_val is None or abs(pct_val) >= 3:
            continue

        stock_name = _get(r, 'symbol')
        sector = _get_sector(stock_name)

        open_price = _get(r, 'openPrice', 'open_price', 'open')
        volume = _get(r, 'trade_quantity', 'tradedQuantity', 'traded_quantity')
        high_price = _get(r, 'highPrice', 'high_price')
        low_price = _get(r, 'LowPrice', 'lowPrice', 'low_price')
        ltp = _get(r, 'ltp')

        csv_writer.writerow(
            [
                stock_name,
                sector or 'N/A',
                pct_change,
                open_price,
                high_price,
                low_price,
                volume,
                ltp,
            ]
        )

# top losers
top_losers = nse.get_top_losers()

with open('topLosers.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(header)

    for r in top_losers:
        pct_change = _get(r, 'perChange', 'pChange', 'percentChange', 'p_change')
        pct_val = _parse_pct(pct_change)
        # Only include stocks with absolute % change below 3%
        if pct_val is None or abs(pct_val) >= 3:
            continue

        stock_name = _get(r, 'symbol')
        sector = _get_sector(stock_name)

        open_price = _get(r, 'openPrice', 'open_price', 'open')
        volume = _get(r, 'trade_quantity', 'tradedQuantity', 'traded_quantity')
        high_price = _get(r, 'highPrice', 'high_price')
        low_price = _get(r, 'LowPrice', 'lowPrice', 'low_price')
        ltp = _get(r, 'ltp')

        csv_writer.writerow(
            [
                stock_name,
                sector or 'N/A',
                pct_change,
                open_price,
                high_price,
                low_price,
                volume,
                ltp,
            ]
        )