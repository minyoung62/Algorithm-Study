import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max =-1;
        int idx = -1;
        
        for(int i = 0; i<9; i++) {
            int value = sc.nextInt();
            if (max < value){
                max = value;
                idx = i + 1;
            }
        }
        System.out.println(max);
        System.out.println(idx);

    }




}
