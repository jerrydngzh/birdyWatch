import requests
import wikipedia

def nameToParsedWikiArticleTest(name: str) -> str:
    """Takes a name and returns the parsed wiki article for that name.

    Args:
        name (str): The name of the wiki article to be parsed.

    Returns:
        str: The parsed wiki article for the given name.
    """

    output = "A parsed wiki article for " + name
    return output


def nameToParsedWikiArticle(name: str) -> str:
    """Takes a name and returns the parsed wiki article for that name.

    Args:
        name (str): The name of the wiki article to be parsed.

    Returns:
        str: The parsed wiki article for the given name.
    """
    bird = wikipedia.page(name)
    output = bird.title + "\n" + wikipedia.summary(name, sentences=3)
    output+="\n" + "Learn More at: " + bird.url
    return output



def main():
    print(nameToParsedWikiArticleTest("test"))
    print(nameToParsedWikiArticle("Poecile atricapillus"))


if __name__ == "__main__":
    main()