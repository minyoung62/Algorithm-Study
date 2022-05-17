import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        String c = s.nextLine().trim();

        System.out.println(countChar(c, ' '));
    }

    private static int countChar(String c, char s) {
        int count = 1;

        for (int i = 0; i < c.length(); i++) {
            if (c.charAt(i) == s) {
                count++;
            }
        }
        if (c.isEmpty()) count = 0;
        return count;
    }
}
