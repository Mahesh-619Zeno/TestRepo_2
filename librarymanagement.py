import sys

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.title} by {self.author} [{status}]"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def __str__(self):
        return f"{self.name}, Borrowed: {', '.join(self.borrowed) or 'None'}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.next_book_id = 1

    def add_book(self, title, author):
        self.books[self.next_book_id] = Book(title, author)
        print(f"Added book [{self.next_book_id}].")
        self.next_book_id += 1

    def register_member(self, name):
        self.members[name] = Member(name)
        print(f"Member '{name}' registered.")

    def list_books(self):
        if not self.books:
            print("No books in library.")
            return
        for id_, book in self.books.items():
            print(f"[{id_}] {book}")

    def list_members(self):
        if not self.members:
            print("No members registered.")
            return
        for m in self.members.values():
            print(m)

    def issue_book(self, member_name, book_id):
        member = self.members.get(member_name)
        book = self.books.get(book_id)
        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if book.is_issued:
            print("Book already issued.")
            return
        book.is_issued = True
        member.borrowed.append(book.title)
        print(f"Issued '{book.title}' to '{member_name}'.")

    def return_book(self, member_name, book_id):
        member = self.members.get(member_name)
        book = self.books.get(book_id)
        if not member or not book:
            print("Invalid return request.")
            return
        if book.title in member.borrowed:
            book.is_issued = False
            member.borrowed.remove(book.title)
            print(f"Returned '{book.title}' from '{member_name}'.")
        else:
            print(f"'{member_name}' did not borrow this book.")

def main():
    lib = Library()
    while True:
        print("\n1:Add Book 2:Register Member 3:List Books 4:List Members")
        print("5:Issue 6:Return 7:Exit")
        choice = input("> ").strip()
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(title, author)
        elif choice == "2":
            name = input("Member Name: ")
            lib.register_member(name)
        elif choice == "3":
            lib.list_books()
        elif choice == "4":
            lib.list_members()
        elif choice == "5":
            name = input("Member Name: ")
            bid = int(input("Book ID: "))
            lib.issue_book(name, bid)
        elif choice == "6":
            name = input("Member Name: ")
            bid = int(input("Book ID: "))
            lib.return_book(name, bid)
        elif choice == "7":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
