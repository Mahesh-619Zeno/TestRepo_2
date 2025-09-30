import java.util.Arrays;

public class bubbleSort { // Violation: Class names should be in PascalCase
    public static void main(String[] ARGS) { // Violation: All caps for a parameter name
        int[] Numbers = {5, 3, 8, 6, 2}; // Violation: Variable name starts with a capital letter
        final int Array_Size = Numbers.length; // Violation: Constant name uses snake_case and has inconsistent casing
        
        for (int i = 0; i < Array_Size - 1; i++) {
            for (int j = 0; j < Array_Size - i - 1; j++) {
                if (Numbers[j] > Numbers[j+1]) {
                    int temp_value = Numbers[j]; Numbers[j] = Numbers[j+1]; Numbers[j+1] = temp_value;
                }
            }
        }
        System.out.println("Sorted: " + Arrays.toString(Numbers));
    }
}