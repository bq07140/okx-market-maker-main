import os

# # api key credential
# API_KEY = "8bcfbe4c-2134-49f2-acfa-acac8a6de0af"
# API_KEY_SECRET = "8CF5749F577E3AB6C6B4AA4B7DDECBBC"
# API_PASSPHRASE = "Bq013317,."

# 模拟
API_KEY = "1ab03901-cc1d-4de0-bd70-281ebf17ae00"
API_KEY_SECRET = "2C45504B74D1F8AC6DF12B4C9842B605"
API_PASSPHRASE = "Bq013317,."

IS_PAPER_TRADING = True

# market-making instrument
TRADING_INSTRUMENT_ID = "BTC-USDT-SWAP"
TRADING_MODE = "cross"  # "cash" / "isolated" / "cross"

# default latency tolerance level
# Warning if OrderBook not updated for these seconds, potential issues from wss connection
ORDER_BOOK_DELAYED_SEC = 60
# Warning if Account not updated for these seconds, potential issues from wss connection
ACCOUNT_DELAYED_SEC = 60

# risk-free ccy
RISK_FREE_CCY_LIST = ["USDT", "USDC", "DAI"]

# params yaml path
PARAMS_PATH = os.path.abspath(os.path.dirname(__file__) + "/params.yaml")



