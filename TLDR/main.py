from newspaper import Article
from splitText import SplitText

TEST_ARTICLE = "http://www.leparisien.fr/politique/rentree-universitaire-macron-surveille-le-chaudron-etudiant-11-09-2017-7250250.php#xtor=AD-1481423553"

def main():
    test_article = Article(url=TEST_ARTICLE)
    test_article.download()
    test_article.parse()
    text = SplitText(test_article.text)
    text.splitIntoParts("french")
    print(text.paragraphs)

if __name__ == '__main__':
    main()

