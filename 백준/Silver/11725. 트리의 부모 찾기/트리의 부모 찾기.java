
import java.io.*;
import java.util.*;
public class Main {

    static int N;
    static boolean[] visited;
    static int[] parent;
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(bf.readLine());
        visited = new boolean[N+1];
        parent = new int[N+1];

        ArrayList<ArrayList<Integer>> tree = new ArrayList<>();
        for(int i=0; i<N+1; i++){
            tree.add(new ArrayList<>());
        }

        for(int i=0; i<N-1; i++){
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tree.get(a).add(b);
            tree.get(b).add(a);
        }

        //bfs로 루트 찾기
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = true;

        while(!q.isEmpty()){
            int v = q.poll();
            for(int node : tree.get(v)){
                if(!visited[node]){
                    visited[node] = true;
                    q.add(node);
                    parent[node] = v;
                }
            }
        }

        for(int i=2; i<N+1; i++){
            System.out.println(parent[i]);
        };

    }

}
