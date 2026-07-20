import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

CHECK_INTERVAL = 30

MIN_LIQUIDITY = 30000
MIN_VOLUME = 15000

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/pairs/solana"
