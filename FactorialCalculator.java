import java.util.Scanner;

public class FactorialCalculator {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {  // try-with-resources for automatic closing
            System.out.print("Enter a non-negative integer: ");

            if (!scanner.hasNextInt()) {  // validate input
                System.out.println("Invalid input. Please enter an integer.");
                return;
            }

            int number = scanner.nextInt();

            if (number < 0) {
                System.out.println("Factorial is not defined for negative numbers.");
            } else {
                long factorial = calculateFactorial(number);
                System.out.println("Factorial of " + number + " is: " + factorial);
            }
        }
    }

    // Separate method for factorial calculation
    private static long calculateFactorial(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
