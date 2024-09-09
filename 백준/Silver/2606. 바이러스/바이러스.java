import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int computer;
    static int pair;
    static int[][] graph;
    static boolean[] visited;
    static int answer=0;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        computer = Integer.parseInt(bf.readLine());
        pair = Integer.parseInt(bf.readLine());
        graph = new int[computer+1][computer+1];
        visited = new boolean[computer+1];

        for(int i=0; i<pair; i++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1][v2] = 1;
            graph[v2][v1] = 1;
        }

        dfs(1);

        for(int i=2; i<=computer; i++){
            if(visited[i]) answer++;
        }

        System.out.println(answer);
    }

    static void dfs(int node){
        visited[node]= true;

        for(int i=1; i<=computer; i++){
            if(!visited[i] && graph[node][i] == 1){
                dfs(i);
            }
        }

    }
}

