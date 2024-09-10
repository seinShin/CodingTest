
import java.io.*;
import java.util.*;

public class Main {
    static int N, count;
    static int[][] homes;

    static int[] dx = new int [] {-1,0,1,0};
    static int[] dy = new int [] {0,1,0,-1};
    static List<Integer> answer = new ArrayList<>();


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        homes = new int[N][N];

        for(int i=0; i<N; i++){
            String str = bf.readLine();
            for(int j=0; j<N; j++){
                homes[i][j] = str.charAt(j)-'0';
            }
        }

        int homeCnt=0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                count=0;
                if(homes[i][j] == 1){
                    bfs(i,j);
                    answer.add(count);
                    homeCnt++;

                }
            }
        }

        System.out.println(homeCnt);
        Collections.sort(answer);
        for(int i: answer){
            System.out.println(i);
        }
    }

    static void bfs(int v1 , int v2){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{v1,v2});
        homes[v1][v2] = 0;

        while(!q.isEmpty()){
            int[] now = q.poll();
            count+=1;

            for(int i=0; i<4; i++){
                int nx = now[0]+dx[i];
                int ny = now[1]+dy[i];

                if(nx>=0 && nx<N && ny>=0 && ny<N && homes[nx][ny] ==1){
                    homes[nx][ny] = 0;
                    q.offer(new int[] {nx, ny});
                }
            }
        }


    }

}

