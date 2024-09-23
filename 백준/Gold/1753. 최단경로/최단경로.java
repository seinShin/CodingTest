
import java.io.*;
import java.util.*;

class Node{
    int n;
    int cost;

    public Node(int n, int cost){
        this.n = n;
        this.cost = cost;
    }
}
public class Main {

    static int V, E, K;
    static boolean[] visited;

    static ArrayList<Node>[] graph;
    static int[] result;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(bf.readLine());

        visited = new boolean[V+1];
        result = new int[V+1];
        Arrays.fill(result, Integer.MAX_VALUE);
        graph = new ArrayList[V+1];

        // 다익스트라 초기 세팅
        for(int i=1; i<=V; i++){
            graph[i] = new ArrayList<>();
            result[i] = Integer.MAX_VALUE;
        }

        // graph 세팅
        for(int i=0; i<E; i++){
            st = new StringTokenizer(bf.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[u].add(new Node(v,w));
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2)->{
            return o1.cost-o2.cost;
        });
        result[K] = 0;
        pq.add(new Node(K,0));

        while(!pq.isEmpty()){
            Node cur = pq.poll();
            if(visited[cur.n]) continue;
            visited[cur.n] = true;

            for(Node node: graph[cur.n]){
                if(visited[node.n]) continue;
                int newWeight = cur.cost+node.cost;
                if(result[node.n]>newWeight){
                    result[node.n] = newWeight;
                    pq.add(new Node(node.n, newWeight));
                }
            }
        }

        for(int i=1; i<V+1; i++){
            if(result[i] == Integer.MAX_VALUE) System.out.println("INF");
            else System.out.println(result[i]);
        }
    }

}

