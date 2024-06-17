package codingTest_java.hd;

import java.util.*;
import java.io.*;
public class hd_1952 {
    static int N, M;
    static int[][] map;

    static int[] dx ={0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static boolean[][] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        M = sc.nextInt();
        N = sc.nextInt();

        visited = new boolean[M][N];

        int cnt = 0;
        int sum = 1;

        int idx = 0;
        int nowX=0;
        int nowY=0;

        visited[nowX][nowY] = true;


        while(idx < 4){
            int nx= nowX+dx[idx];
            int ny = nowY+dy[idx];

            if(sum == N*M){
                System.out.println(cnt);
                return;
            }
            if(nx >= 0 && ny >= 0 && nx < M && ny < N && !visited[nx][ny]) {
                sum++; // 지나온 칸 수 + 1
                visited[nx][ny] = true; // 방문 처리
                nowX = nx; // 다음 탐색을 위해 갱신
                nowY = ny;
            }else{
                idx++;
                cnt++;
            }

            if(idx>=4){
                idx=0;
            }

        }
    }
}
