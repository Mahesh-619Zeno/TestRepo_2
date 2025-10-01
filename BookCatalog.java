import java.util.ArrayList;
import java.util.List;

public class BookCatalog {

    // ⚠️ No encapsulation: public and static
    public static List<String> books = new ArrayList<>();

    public static void main(String[] args) {
        BookCatalog catalog = new BookCatalog();

        catalog.addBook("Clean Code");
        catalog.addBook("The Pragmatic Programmer");
        catalog.addBook("  ");           // ⚠️ Should not allow empty titles
        catalog.addBook(null);           // ⚠️ Should be validated

        catalog.printCatalog();
    }

    public void addBook(String title) {
        books.add(title); // ⚠️ No validation
    }

    public void printCatalog() {
        System.out.println("Book Catalog:");

        if (books.isEmpty()) {
            System.out.println("No books available.");
            return;
        }

        int index = 1;
        for (String title : books) {
            // ⚠️ May print null or blank titles
            System.out.println(index + ". " + title);
            index++;
        }
    }
}
