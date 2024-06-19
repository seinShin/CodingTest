package codingTest_java.hd;

import java.util.*;
public class hd_10797 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();
        int sum =0;

        for(int i=0; i<5; i++){
            int car = sc.nextInt();
            if(day == car) sum++;
        }

        System.out.println(sum);

    }
}
