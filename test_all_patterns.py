# Importy z katalogu wzorce
from patterns.adapter import LibraryCatalogAdapter
from patterns.factory import UserFactory
from patterns.facade import LibraryInterface
from patterns.observer import LibraryCatalog, User


def test_adapter():
    print("\nTesting Adapter...")
    json_data = '[{"title": "Book 1", "author": "Author 1"}]'
    csv_data = "Book 3, Author 3\nBook 4, Author 4"

    adapted_json = LibraryCatalogAdapter.adapt(json_data, "json")
    adapted_csv = LibraryCatalogAdapter.adapt(csv_data, "csv")

    print("Adapted JSON:", adapted_json)
    print("Adapted CSV:", adapted_csv)


def test_factory():
    print("\nTesting Factory...")
    student = UserFactory.create_user("Student", "Alice")
    teacher = UserFactory.create_user("Teacher", "Bob")
    librarian = UserFactory.create_user("Librarian", "Charlie")
    guest = UserFactory.create_user("Guest", "Daisy")

    print(f"{student.name}: {student.get_permissions()}")
    print(f"{teacher.name}: {teacher.get_permissions()}")
    print(f"{librarian.name}: {librarian.get_permissions()}")
    print(f"{guest.name}: {guest.get_permissions()}")


def test_facade():
    print("\nTesting Facade...")
    library = LibraryInterface()

    # Adding users
    print(library.add_user("John"))
    print(library.add_user("Doe"))

    # Adding books
    print(library.add_book("Cool Book", "Smith XYZ"))
    print(library.add_book("Fun Story", "Jane ABC"))

    # Listing users
    print("Users:", library.list_users())

    # Listing books
    print("Books:", library.list_books())

    # Borrowing books
    print(library.borrow_book("Cool Book"))
    print(library.borrow_book("Cool Book"))
    print(library.borrow_book("Unknown Book"))


def test_observer():
    print("\nTesting Observer...")
    catalog = LibraryCatalog()

    # Creating users
    kasia = User("Kasia")
    jan = User("Jan")

    # Adding observers
    catalog.add_observer(kasia)
    catalog.add_observer(jan)

    # Adding books
    print(catalog.add_book("Fajna Książka", available=False))
    print(catalog.add_book("Śmieszna Opowieść"))

    # Changing book status
    print(catalog.change_book_status("Śmieszna Opowieść", available=False))
    print(catalog.change_book_status("Fajna Książka", available=True))


if __name__ == "__main__":
    test_adapter()
    test_factory()
    test_facade()
    test_observer()
