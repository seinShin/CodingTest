
import java.util.*;
import java.io.*;
public class Main {

    public static class Node{
        int v;
        int w;
        int cost;

        public Node(int v, int w, int cost){
            this.v = v;
            this.w = w;
            this.cost = cost;
        }
    }
    static int N, M;

    static long[] dist;
    static ArrayList<Node> graph;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>();
        dist = new long[N+1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[1]=0;

        // 그래프 세팅
        for(int i=0; i<M; i++){
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.add(new Node(a,b,c));
        }

        // 벨만-포드
        for(int i=1; i<=N; i++){
           for(Node node : graph){
               if(dist[node.v] == Long.MAX_VALUE) continue;

               if(dist[node.w] > dist[node.v]+node.cost){
                   dist[node.w] = dist[node.v]+node.cost;

                   if(i == N){
                       System.out.println(-1);
                       return;
                   }
               }
           }
        }

        for(int i=2; i<=N; i++){
            if(dist[i] != Long.MAX_VALUE) System.out.println(dist[i]);
            else System.out.println(-1);
        }

    }

}


