import requests

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

    #get article from wikipedia
    #name
    #scientific name
    #endangered species
    #image

    #parse article for relevant information
    #return parsed article
    pass



def main():
    print(nameToParsedWikiArticleTest("test"))


if __name__ == "__main__":
    main()