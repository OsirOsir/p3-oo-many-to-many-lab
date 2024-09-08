# many_to_many.py

class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
    
    def __repr__(self):
        return f"Book(title={self.title})"


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)
    
    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        contract = Contract(author=self, book=book, date=date, royalties=royalties)
        self._contracts.append(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
    
    def __repr__(self):
        return f"Author(name={self.name})"


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
    
    def __repr__(self):
        return f"Contract(author={self.author}, book={self.book}, date={self.date}, royalties={self.royalties})"
