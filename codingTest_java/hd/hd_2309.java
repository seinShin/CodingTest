package codingTest_java.hd;

import java.util.*;
public class hd_2309 {

    static int[] arr = new int[9];
    static int sum=0;
    static int f1 =0, f2=0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for(int i=0; i<9; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }

        Arrays.sort(arr);

        for(int i=0; i<9; i++){
            for(int j=i+1; j<9; j++){
                if(sum-arr[i]-arr[j] == 100){
                    f1=arr[i];
                    f2=arr[j];
                }
            }
        }

        for(int i=0; i<9; i++){
            if(arr[i] != f1 && arr[i] != f2) System.out.println(arr[i]);
        }


    }
}

