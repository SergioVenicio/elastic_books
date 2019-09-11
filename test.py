from elasticsearch import Elasticsearch

class Book:
    def __init__(self, title, author, year, pages, gender, language):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.gender = gender
        self.language = language

    def __str__(self):
        return (
            'Title: %s.\n'
            'Author: %s.\n'
            'Year: %s.\n'
            'Pages: %s.\n'
            'Gender: %s.\n'
            'Language: %s.\n'
            '\n________________________________\n'
        ) % (
            self.title,
            self.author,
            self.year,
            self.pages,
            self.gender,
            self.language
        )


if __name__ == "__main__":

    es = Elasticsearch() 

    books = [{
        'title': 'IT',
        'author': 'Stephen King',
        'year': 1987,
        'pages': 1116,
        'gender': 'Thriller',
        'language': 'Inglish'
    },{
        'title': 'Alice in Wonderland',
        'author': 'Lewis Carrol',
        'year': 1865,
        'pages': 78,
        'gender': 'Adventure',
        'language': 'Inglish'
    }]

    es.indices.delete(index='book_db')

    for _book in books:
        resp = es.index(
            index='book_db', doc_type='book',
            id=_book['title'], body=_book
        )

    resp = es.search(body={'query': {'match_all': {}}})

    for row in resp['hits']['hits']:
        print(Book(**row['_source']))