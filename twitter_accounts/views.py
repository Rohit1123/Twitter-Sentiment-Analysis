from glob import escape
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
from .models import Twitter_account, Tweet
from .nlp import sentiment_analysis


def index(request):
    twitter_accounts = [twitter_account for twitter_account in Twitter_account.objects.all()]

    if request.method == 'POST':
        tweet_all = ""
        hashtag = request.POST['hashtag']
        limit = 50
        count = 0
        
        for tweet in sntwitter.TwitterSearchScraper(hashtag).get_items():
            if count < limit:
                count = count + 1
                new_account = Twitter_account(name = tweet.user.username, hash_tag = hashtag)
                new_account.save()
                new_tweet = Tweet(twitter_account= tweet.user.username, tweet = tweet.content, date = tweet.date, hash_tag = hashtag)
                new_tweet.save()
            else:
                break
        tweets = Tweet.objects.filter(hash_tag=hashtag)
        for tweet in tweets:
            tweet_all = tweet_all + tweet.tweet
            score = sentiment_analysis(tweet.tweet)
            tweet.__setattr__("score_compound", score["compound"])
            tweet.__setattr__("score_pos", score["pos"])
            tweet.__setattr__("score_neg", score["neg"])
            tweet.__setattr__("score_neu", score["neu"])
        
        selected_hash_tag = Tweet.objects.filter(hash_tag=hashtag)
        score = sentiment_analysis(tweet_all)
        selected_hash_tag.__setattr__("score_compound", score["compound"])
        selected_hash_tag.__setattr__("score_pos", score["pos"])
        selected_hash_tag.__setattr__("score_neg", score["neg"])
        selected_hash_tag.__setattr__("score_neu", score["neu"])
    else:
        tweets = Tweet.objects.all()
        selected_hash_tag = twitter_accounts[0]
        selected_hash_tag.__setattr__("score_compound", 0)
        selected_hash_tag.__setattr__("score_pos", 0)
        selected_hash_tag.__setattr__("score_neg", 0)
        selected_hash_tag.__setattr__("score_neu", 0)

    context = {
        "twitter_accounts": twitter_accounts,
        "selected_hash_tag": selected_hash_tag,
        "tweets" : tweets,
    }

    print(context)

    return render(request, "index.html", context)

def nlp(request):
    score = sentiment_analysis("I love this")
    context = {
        "score": score,
    }

    return render(request, "analysis.html", context)

def about(request):
    return render(request, "about.html", {})