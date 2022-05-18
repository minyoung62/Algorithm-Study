import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int value = 1;
        for(int i = 0; i < 3; i++) {
            value *= sc.nextInt();
        }
        int[] arr = new int[10];
        for(int i = 0; i < 10; i++){
            arr[i] = 0;
        }
        String s = Integer.toString(value);

        for(int i = 0 ; i < s.length(); i++) {
            arr[s.charAt(i)-'0'] += 1;
        }
        for(int i= 0; i<10; i++){
            System.out.println(arr[i]);
        }
    }

}
