import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().toUpperCase();

        System.out.println(findManyAlpha(s));

    }

    private static char findManyAlpha(String s) {
        char ans = '?';
        int max = -1;

        int[] alpha = new int[26];

        for(int i = 0; i < s.length(); i++) {
            alpha[s.charAt(i) - 'A']++;
        }


        for(int i = 0; i < alpha.length; i++) {
            if (max < alpha[i]) {
                max = alpha[i];
                ans = (char) (i+'A');
            } else if (max == alpha[i]) {
                ans = '?';
            }
        }




        return ans;
    }


}
