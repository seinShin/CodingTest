
import java.io.*;
import java.util.*;
public class Main {

    static int n;
    static int[] arr ;
    static int start, end=0;
    static int x;
    static int answer=0;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(bf.readLine());
        arr = new int[n];

        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        x = Integer.parseInt(bf.readLine());

        Arrays.sort(arr);
        end=n-1;
        //tow pointer
        while (start < end) {
            int sum = arr[start] + arr[end];
            if (sum == x) {
                answer++;
            }

            if(sum<x){
                start++;
            }else end--;

        }
        System.out.println(answer);
    }



}
