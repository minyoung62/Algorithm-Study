import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++) {
            int repeatNum = sc.nextInt();
            String string = sc.next();

            for(int j = 0; j < string.length(); j++) {
                for(int z = 0; z < repeatNum; z++) {
                    System.out.print(string.charAt(j));
                }
            }
            System.out.println();
        }

    }

}
