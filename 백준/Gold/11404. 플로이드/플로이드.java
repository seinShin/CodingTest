
import java.io.*;
import java.util.*;
public class Main {

    static int n, m;
    static int[][] graph;

    static final int INF = 10000000;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        m = Integer.parseInt(bf.readLine());
        graph = new int[n+1][n+1];

        for(int i=1; i<graph.length; i++){
            for(int j=1; j<graph.length; j++){
                if(i!=j) graph[i][j] = INF;
                else graph[i][j] = 0;
            }
        }

        StringTokenizer st;
        for(int i=0; i<m; i++){
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a][b] = Math.min(graph[a][b], c);
        }

        floyd(graph, n);

    }

    public static void floyd(int[][] graph, int n){
        for(int k=1; k<=n; k++){
            for(int i=1; i<=n; i++){
                for(int j=1; j<=n; j++){
                    graph[i][j] = Math.min(graph[i][j], graph[i][k]+graph[k][j]);
                }
            }
        }

        for(int i=1; i<=n;i++){
            for(int j=1; j<=n; j++){
                if(graph[i][j] == INF) System.out.print(0+" ");
                else System.out.print(graph[i][j]+" ");
            }
            System.out.println();
        }
    }

}
