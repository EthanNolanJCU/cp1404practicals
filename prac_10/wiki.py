import wikipedia

search_term = input('Enter Wiki Page: ')
while search_term != '':
    title = wikipedia.search(search_term, results=1)
    try:
        page = wikipedia.page(title)
        print(page.title)
        print(page.url)
        print(wikipedia.summary(page))
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)
    search_term = input('Enter Wiki Page: ')
