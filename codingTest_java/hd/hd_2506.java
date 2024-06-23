package codingTest_java.hd;

import java.util.*;
public class hd_2506 {
    static int sum=0;
    static int chk=0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=0; i<N; i++){
            int num = sc.nextInt();
            if(num == 0){
                chk=0;
            }else{
                chk++;
                sum+=chk;
            }
        }

        System.out.println(sum);
    }
}
