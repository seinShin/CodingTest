package codingTest_java.hd;

import java.util.*;
public class hd_10869 {
    static int A;
    static int B;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        if(1<=A && A<=10000 && 1<=B && B<=10000 ){
            System.out.println(A+B);
            System.out.println(A-B);
            System.out.println(A*B);
            System.out.println(A/B);
            System.out.println(A%B);
        }
    }
}
