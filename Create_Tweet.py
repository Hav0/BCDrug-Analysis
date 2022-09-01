import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("NBDZSFWkpppG57vldhlESp5VW", "9ZLJDdxYWlmBkeVC3CLam3WigqZaE01dAIetzMqGNMOZB1PbsK")
auth.set_access_token("1551006127512399872-Ba2E4vryyZLhDy4cz8Poe3Sy6c102I", "tPTyighDtMfHhbatP9EnRXSkC6k5H1pS0p6SL2kQ3Uiy8")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy (Test)")