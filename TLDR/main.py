from newspaper import Article
from splitText import SplitText
from summarizer import Summarizer
from summarizingFuncs import naiveTextRank
TEST_ARTICLE = "http://www.lefigaro.fr/vie-bureau/2017/10/06/09008-20171006ARTFIG00032-japon-une-journaliste-meurt-apres-159-heures-sup-en-un-mois.php"
TEST_ARTICLE2 = "http://www.lemonde.fr/international/article/2017/10/07/prix-nobel-de-la-paix-le-combat-tres-symbolique-de-l-ican_5197546_3210.html"


def main():
    test_article = Article(url=TEST_ARTICLE2)
    test_article.download()
    test_article.parse()
    text = SplitText(test_article.text)
    text.splitIntoParts("french")

    tldr = Summarizer(text)
    tldr.summarize(naiveTextRank)
    print(test_article.title)
    print(tldr.summary)

if __name__ == '__main__':
    main()

