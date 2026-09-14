# import yfinance as yf
# # a= yf.download("TCS.NS", start = "2026-08-19", end= "2026-08-29")
# # print(a)
# a= yf.download("BHARTIAXA")
# print(a)

import yfinance as yf

data = yf.download(
    "BHARTIARTL.NS",
    period="1d",
    interval="5m"
)

print(data)