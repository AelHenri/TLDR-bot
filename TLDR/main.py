from newspaper import Article
from splitText import SplitText
from summarizer import Summarizer
from summarizingFuncs import naiveTextRank
TEST_ARTICLE = "http://www.lemonde.fr/idees/article/2017/10/07/budget-2018-injustice-fiscale_5197670_3232.html"

def main():
    test_article = Article(url=TEST_ARTICLE)
    test_article.download()
    test_article.parse()
    text = SplitText(test_article.text)
    text.splitIntoParts("french")

    tldr = Summarizer(text)
    tldr.summarize(naiveTextRank)
    print(tldr.summary)

if __name__ == '__main__':
    main()

