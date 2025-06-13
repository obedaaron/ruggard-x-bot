import tweepy

# HARDCODED CREDENTIALS (TEMPORARY)
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKPkxgEAAAAAS%2Fl108jDMwe5e2VarZi8G2zGAno%3D88KuAJIT50JgB1YqvBvHRyRrbOBxT3jSEjSFNTSF5rz6m6OWh0"
consumer_key = "m2efVMNq3zoWg21n0gsEKrasl"
consumer_secret = "y2LmQ2gtaYmUr0t6ROsrAAXTJcUd3osYusprpoocIvNvznqJRX"
access_token = "1717449291688558592-L3f9cgXxVo7imI3KQY9shKhha35tpw"
access_token_secret = "hBRBNnLfbO0etksKX6nmUDsJtvYws9cDVcoEQuz87AslH"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token)
