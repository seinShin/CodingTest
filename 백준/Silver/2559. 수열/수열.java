
import java.util.*;
import java.io.*;
public class Main {

    static int N;
    static int K;
//    static int[] maxArr;
    static boolean flag = true;
    static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader bf  = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int[] days = new int[N];
//        maxArr = new int[N];

        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<N; i++){
            days[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<N; i++){
            int tmp = 0;
            for(int j=i; j<=i+K-1; j+=1){
                tmp+= days[j];
                if(j == N-1){
                    flag = false;
                }
            }
            max = Math.max(max, tmp);
            if(!flag) break;
        }

        System.out.println(max);
    }

}


