import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double arr[] = new double[sc.nextInt()];

        for(int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextDouble();
        }
        double sum = 0;
        double max = Arrays.stream(arr).max().getAsDouble();

        for(int i = 0; i< arr.length; i++) {
            sum += ((arr[i] / max)*100);
        }
        System.out.print(sum/arr.length);

    }




}
