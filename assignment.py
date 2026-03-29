from abc import ABC, abstractmethod
from multipledispatch import dispatch

class InvalidItemError(Exception):
    """Custom exception for invalid library item attributes"""
    pass

class InvalidBorrowerError(Exception):
    """Custom exception for invalid borrower information"""
    pass

class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str, author: str):
        self._validate_input(item_id, title, author)
        self._item_id = item_id
        self._title = title
        self._author = author
        self._is_borrowed = False
        self._borrower = None
        self._borrow_date = None

    def _validate_input(self, item_id: str, title: str, author: str):
        if not isinstance(item_id, str) or not item_id.strip():
            raise InvalidItemError("Item ID must be a non-empty string")
        if not isinstance(title, str) or not title.strip():
            raise InvalidItemError("Title must be a non-empty string")
        if not isinstance(author, str) or not author.strip():
            raise InvalidItemError("Author must be a non-empty string")

    # Getter and setter methods
    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise InvalidItemError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise InvalidItemError("Author must be a non-empty string")
        self._author = value

    @abstractmethod
    def display_info(self):
        pass

    def _validate_borrower(self, borrower_name: str):
        if not isinstance(borrower_name, str) or not borrower_name.strip():
            raise InvalidBorrowerError("Borrower name must be a non-empty string")

    @dispatch(str)
    def borrow(self, borrower_name: str):
        self._validate_borrower(borrower_name)
        if self._is_borrowed:
            raise InvalidBorrowerError(f"Item {self._item_id} is already borrowed")
        self._is_borrowed = True
        self._borrower = borrower_name
        self._borrow_date = None
        return f"{self._title} has been borrowed by {borrower_name}"

    @dispatch(str, str)
    def borrow(self, borrower_name: str, borrow_date: str):
        self._validate_borrower(borrower_name)
        if self._is_borrowed:
            raise InvalidBorrowerError(f"Item {self._item_id} is already borrowed")
        self._is_borrowed = True
        self._borrower = borrower_name
        self._borrow_date = borrow_date
        return f"{self._title} has been borrowed by {borrower_name} on {borrow_date}"

class Book(LibraryItem):
    def display_info(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        borrower_info = f" by {self._borrower}" if self._is_borrowed else ""
        date_info = f" on {self._borrow_date}" if self._borrow_date else ""
        return (f"Type: Book\n"
                f"ID: {self._item_id}\n"
                f"Title: {self._title}\n"
                f"Author: {self._author}\n"
                f"Status: {status}{borrower_info}{date_info}")

class Magazine(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str, issue_number: str):
        super().__init__(item_id, title, author)
        self._issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        self._issue_number = value

    def display_info(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        borrower_info = f" by {self._borrower}" if self._is_borrowed else ""
        date_info = f" on {self._borrow_date}" if self._borrow_date else ""
        return (f"Type: Magazine\n"
                f"ID: {self._item_id}\n"
                f"Title: {self._title}\n"
                f"Author: {self._author}\n"
                f"Issue Number: {self._issue_number}\n"
                f"Status: {status}{borrower_info}{date_info}")

# Test the implementation
def main():
    try:
        # Create instances
        book = Book("B001", "Python Programming", "John Smith")
        magazine = Magazine("M001", "Tech Weekly", "Editorial Team", "2024-001")

        # 1. Display details
        print("Book Information:")
        print(book.display_info())
        print("\nMagazine Information:")
        print(magazine.display_info())

        # 2. Borrow book with only borrower's name
        print("\nBorrowing book:")
        print(book.borrow("Alice Johnson"))
        print("\nUpdated Book Information:")
        print(book.display_info())

        # 3. Borrow magazine with name and date
        print("\nBorrowing magazine:")
        print(magazine.borrow("Bob Wilson", "2024-03-15"))
        print("\nUpdated Magazine Information:")
        print(magazine.display_info())

        # 4. Try to create an item with empty title
        print("\nTrying to create an invalid book:")
        invalid_book = Book("B002", "", "John Smith")

    except InvalidItemError as e:
        print(f"\nInvalid Item Error: {e}")
    except InvalidBorrowerError as e:
        print(f"\nInvalid Borrower Error: {e}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")

    # 5. Try to borrow with empty borrower name
    try:
        print("\nTrying to borrow with empty name:")
        book.borrow("")
    except InvalidBorrowerError as e:
        print(f"Invalid Borrower Error: {e}")

if __name__ == "__main__":
    main()
