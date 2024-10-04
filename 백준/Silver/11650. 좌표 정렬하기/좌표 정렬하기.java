
import java.io.*;
import java.util.*;
public class Main {

    static int N;
    static int[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(bf.readLine());
        graph = new int[N][2];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[i][0] = a;
            graph[i][1] = b;
        }

        Arrays.sort(graph, (o1,o2)->{
            if(o1[0] == o2[0]){
                return o1[1]-o2[1];
            }else{
                return o1[0]-o2[0];
            }
        });

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<N; i++){
            sb.append(graph[i][0]+ " " + graph[i][1]).append('\n');
        }
        System.out.println(sb);
    }

}
