package codingTest_java.hd;

import java.util.Scanner;
public class hd_31090 {
    public static int T;
    public static int N;
    public static int M;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        T = Integer.parseInt(sc.next());

        for(int i=0 ; i<T; i++){
            N = Integer.parseInt(sc.next());
            M = N+1;
            int k = Integer.parseInt(String.valueOf(N).substring(2,4));
            if(k!=0){
                if(M%k == 0){
                    System.out.println("Good");
                }else{
                    System.out.println("Bye");
                }
            }else{
                System.out.println("Bye");
            }




        }
    }
}
