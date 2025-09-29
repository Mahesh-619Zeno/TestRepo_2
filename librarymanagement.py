import sys
from typing import Dict, List

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.title} by {self.author} [{status}]"

class Member:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: List[int] = []

    def __str__(self):
        borrowed = ', '.join(str(book_id) for book_id in self.borrowed_books) or 'None'
        return f"{self.name}, Borrowed Book IDs: {borrowed}"

class Library:
    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.members: Dict[str, Member] = {}
        self.next_book_id = 1

    def add_book(self, title: str, author: str):
        self.books[self.next_book_id] = Book(title, author)
        print(f"✅ Added book: [{self.next_book_id}] {title} by {author}")
        self.next_book_id += 1

    def register_member(self, name: str):
        if name in self.members:
            print(f"⚠️ Member '{name}' is already registered.")
            return
        self.members[name] = Member(name)
        print(f"✅ Member '{name}' registered.")

    def list_books(self):
        if not self.books:
            print("📚 No books in the library.")
            return
        for book_id, book in self.books.items():
            print(f"[{book_id}] {book}")

    def list_members(self):
        if not self.members:
            print("🙋 No members registered.")
            return
        for member in self.members.values():
            print(member)

    def issue_book(self, member_name: str, book_id: int):
        member = self.members.get(member_name)
        book = self.books.get(book_id)

        if not member:
            print("❌ Member not found.")
            return
        if not book:
            print("❌ Book not found.")
            return
        if book.is_issued:
            print(f"❌ Book [{book_id}] '{book.title}' is already issued.")
            return

        book.is_issued = True
        member.borrowed_books.append(book_id)
        print(f"✅ Issued '{book.title}' to '{member_name}'.")

    def return_book(self, member_name: str, book_id: int):
        member = self.members.get(member_name)
        book = self.books.get(book_id)

        if not member:
            print("❌ Member not found.")
            return
        if not book:
            print("❌ Book not found.")
            return
        if book_id not in member.borrowed_books:
            print(f"❌ '{member_name}' did not borrow book ID [{book_id}].")
            return

        book.is_issued = False
        member.borrowed_books.remove(book_id)
        print(f"✅ Returned '{book.title}' from '{member_name}'.")

def main():
    library = Library()
    menu = """
==== Library Menu ====
1. Add Book
2. Register Member
3. List Books
4. List Members
5. Issue Book
6. Return Book
7. Exit
=======================
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            title = input("📘 Enter book title: ").strip()
            author = input("✍️  Enter author name: ").strip()
            library.add_book(title, author)

        elif choice == "2":
            name = input("🙋 Enter member name: ").strip()
            library.register_member(name)

        elif choice == "3":
            print("\n📚 Book List:")
            library.list_books()

        elif choice == "4":
            print("\n👥 Member List:")
            library.list_members()

        elif choice == "5":
            name = input("🙋 Member name: ").strip()
            try:
                book_id = int(input("📘 Book ID to issue: ").strip())
                library.issue_book(name, book_id)
            except ValueError:
                print("❌ Invalid Book ID.")

        elif choice == "6":
            name = input("🙋 Member name: ").strip()
            try:
                book_id = int(input("📘 Book ID to return: ").strip())
                library.return_book(name, book_id)
            except ValueError:
                print("❌ Invalid Book ID.")

        elif choice == "7":
            print("👋 Goodbye!")
            sys.exit()

        else:
            print("❌ Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
