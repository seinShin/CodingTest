
import java.io.*;
import java.util.*;
public class Main {
    static int N;
    static int M;
    static int[] parentSet;

    public static boolean union(int x, int y){
        x = find(x);
        y = find(y);

        if(x == y) return false;

        if(x<y) parentSet[y] = x;
        else parentSet[x] = y;

        return true;
    }
    public static int find(int x){
        if(parentSet[x] != x) parentSet[x] = find(parentSet[x]);
        return parentSet[x];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        parentSet = new int[N+1];

        for(int i=0; i<parentSet.length; i++){
            parentSet[i] = i;
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(bf.readLine());
            int idx = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(idx == 0){
                union(a,b);
            }else{
                if(find(a) == find(b)) System.out.println("yes");
                else System.out.println("no");
            }
        }

    }

}
