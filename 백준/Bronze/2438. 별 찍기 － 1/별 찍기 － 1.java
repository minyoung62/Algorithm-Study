import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++) {
            String tmp = "";
            for(int j = 0; j <= i; j++){
                tmp += "*";
            }
            System.out.println(tmp);
        }

    }




}
