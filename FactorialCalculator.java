import java.util.Scanner;

public class FactorialCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a non-negative integer: ");
        int number = scanner.nextInt();
        
        if (number < 0) {
            System.out.println("Factorial is not defined for negative numbers.");
        } else {
            long factorial = 1;
            for (int j = 1; j <= number; j++) {
                factorial *= j;
            }
            System.out.println("Factorial of " + number + " is: " + factorial);
        }
        
        scanner.close();
    }
}
