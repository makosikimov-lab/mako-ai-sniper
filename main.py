from scanner import get_pairs

pairs = get_pairs()

print(f"Found {len(pairs)} pairs")

for pair in pairs[:10]:

    symbol = pair["baseToken"]["symbol"]

    liquidity = pair["liquidity"]["usd"]

    volume = pair["volume"]["h24"]

    print(symbol, liquidity, volume)
