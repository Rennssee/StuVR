articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []

    for article in articles_dict:
        title_key = False
        author_key = False

        if letter_case:
            if key in article["title"]:
                title_key = True
            if key in article["author"]:
                author_key = True

        else:
            if key.lower() in article["author"].lower():
                title_key = True
            if key.lower() in article["title"].lower():
                author_key = True

        if title_key or author_key:
            author_LN = article["author"].split()[-1]
            new_article = {
                "title": article["title"],
                "author": article["author"],
                "year": article["year"],
            }
            result.append(new_article)

    return result
