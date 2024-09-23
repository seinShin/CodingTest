import java.util.*;
import java.io.*;

class Node{
    int idx;
    int x;

    public Node(int idx, int x){
        this.idx = idx;
        this.x = x;
    }
}

public class Main {
    static int N, E, v1, v2;
    static int[] rst;
    static ArrayList<Node>[] graph;
    static boolean[] visited;
    static final int INF = 200000000;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        rst = new int[N+1];
        visited = new boolean[N+1];

        for(int i=0; i<N+1; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<E; i++){
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a].add(new Node(b,c));
            graph[b].add(new Node(a,c));
        }

        st = new StringTokenizer(bf.readLine());
        v1 = Integer.parseInt(st.nextToken());
        v2 = Integer.parseInt(st.nextToken());


        int res = 0;
        res+=djikstra(1, v1);
        res+=djikstra(v1, v2);
        res+=djikstra(v2, N);

        int res2 = 0;
        res2+=djikstra(1, v2);
        res2+=djikstra(v2, v1);
        res2+=djikstra(v1, N);

        // 경로가 없는 경우
        if(res>= INF && res2>= INF){
            System.out.println(-1);
        }else{
            System.out.println(Math.min(res, res2));
        }
    }

    public static int djikstra(int start, int end){
        Arrays.fill(rst, INF);
        Arrays.fill(visited, false);
        //다익스트라 시작
        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2)-> {
            return o1.x - o2.x;
        });

        rst[start] =0;
        pq.offer(new Node(start,0));

        while(!pq.isEmpty()){
            Node now = pq.poll();

            if(visited[now.idx]) continue;
            visited[now.idx] = true;

            for(Node node : graph[now.idx]){
                int nextCost = now.x+node.x;

                if(rst[node.idx] > nextCost && !visited[node.idx]){
                    rst[node.idx] = nextCost;
                    pq.add(new Node(node.idx, nextCost));
                }
            }
        }
        return rst[end];
    }
}
