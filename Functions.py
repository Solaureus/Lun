from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import random

random.seed()
analyzer = SentimentIntensityAnalyzer()
translator = Translator()


def factorial(n):
    a = 1
    for number in range(1, n + 1):
        a *= number
    return a


def sentiment_analysis(text):
    trans = translator.translate(text).text
    score = analyzer.polarity_scores(trans)
    lb = score['compound']
    if lb >= 0.05:
        return 'This phrase is positive. Compound score: ' + str(lb) + ' (-1 most negative and 1 most positive).'
    elif (lb > -0.05) and (lb < 0.05):
        return 'This phrase is neutral. Compound score: ' + str(lb) + ' (-1 most negative and 1 most positive).'
    else:
        return 'This phrase is negative. Compound score: ' + str(lb) + ' (-1 most negative and 1 most positive).'


def combinations(n, r):
    return int((factorial(n))/(factorial(r) * factorial(n-r)))


def coin_flip():
    return "Heads!" if random.randint(0, 1) else "Tails!"


def magic_eight_ball():
    switcher = {
            1: "Really? That was the best question you could come up with?",
            2: "Yes.",
            3: "No.",
            4: "LOL! As IF!",
            5: "The answer is, unfortunately, yes.",
            6: "The law requires me to answer no.",
            7: "Yes. Don't waste my time.",
            8: "No, never, under no circumstances, not on your life.",
            9: "Beyond all expectation, yes.",
            10: "FUCK NO!",
            11: "As if it wasn't blindingly obvious, yes."
        }
    return switcher.get(random.randint(1, 11))
