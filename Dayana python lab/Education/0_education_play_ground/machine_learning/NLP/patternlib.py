import pattern
from pattern.en import tag
tweet_ = "I hope it is going good for you!"
tweet_l = tweet_.lower()
tweet_tags = tag(tweet_l)
print(tweet_tags)