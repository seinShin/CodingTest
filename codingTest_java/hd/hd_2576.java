package codingTest_java.hd;

import java.util.*;
public class hd_2576 {
    public static int[] arr = new int[7];
    public static int sum = 0;
    public static int min=100;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int i=0 ; i<7; i++){
            int x = sc.nextInt();

            if(x%2 !=0){
                sum+=x;
                if(min>x) min =x;
            }
        }

        if(sum == 0) System.out.println(-1);
        else{
            System.out.println(sum);
            System.out.println(min);
        }
    }

}
