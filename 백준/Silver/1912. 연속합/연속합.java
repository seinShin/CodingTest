
import java.util.*;
import java.io.*;
public class Main {

    static int N;
    static int max;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bf.readLine());
        int [] arr = new int[N+1];
        int [] dp = new int[N+1];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i=1; i<N+1;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp[1]=arr[1];
        max = dp[1];

        for(int i=2; i<N+1;i++){
            dp[i] = Math.max(arr[i], dp[i-1]+arr[i]);
            max = Math.max(max, dp[i]);
        }

        System.out.println(max);

    }
}


