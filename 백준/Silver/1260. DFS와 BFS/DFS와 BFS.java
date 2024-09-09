
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

    static int n, m, v;
    static int[][] graph;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        graph = new int[n+1][n+1];
        visited = new boolean[n+1];

        for(int i=0 ; i<m; i++){
            st = new StringTokenizer(bf.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1][v2] = 1;
            graph[v2][v1] = 1;
        }

        dfs(v);
        System.out.println();
        visited = new boolean[n+1];
        bfs(v);

    }

    static void dfs(int node){
        visited[node] = true;
        System.out.print(node+ " ");
        for(int i=1; i<=n; i++){
            if(graph[node][i]==1 && !visited[i]){
                dfs(i);
            }
        }
    }

    static Queue<Integer> q;
    static void bfs(int node){
        q =  new LinkedList<>();
        q.add(node);
        visited[node] = true;

        while(!q.isEmpty()){
            int tmp = q.poll();
            System.out.print(tmp + " ");
            for(int i=1; i<=n; i++){
                if(graph[tmp][i]==1 && !visited[i]){
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
    }
}

