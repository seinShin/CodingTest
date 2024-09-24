
import java.util.*;
import java.io.*;

public class Main {
    public static class move {
        int x; //위치
        int cnt; // 시간(초)

        public move(int x, int cnt){
            this.x = x;
            this.cnt = cnt;
        }
    }
    static int N, K;
    static final int INF = 1000000;

    static int[] rst = new int[INF+1];
    static boolean[] visited = new boolean[INF+1];

    static int[] dx = {1,-1};

    static int answer=0;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        Arrays.fill(visited, false);
        Arrays.fill(rst, INF);
        rst[N]=0;

        PriorityQueue<move> pq = new PriorityQueue<>((o1,o2)->{
            return o1.cnt-o2.cnt;
        });
        pq.offer(new move(N, 0));

        while(!pq.isEmpty()){
            move now = pq.poll();
            int x = now.x;
            int cnt = now.cnt;
            visited[x] = true;
            if(x == K){
                answer = cnt;
                break;
            }

            if(x*2 <= INF && !visited[x*2]){

                pq.offer(new move(x * 2, cnt));
            }
            if(x+1 <= INF && !visited[x+1]){

                pq.offer(new move(x + 1, cnt + 1));
            }
            if(x-1>=0 && !visited[x-1]){

                pq.offer(new move(x - 1, cnt + 1));
            }


        }

        System.out.println(answer);
    }


}
