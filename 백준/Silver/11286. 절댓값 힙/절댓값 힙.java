
import java.io.*;
import java.util.*;

public class Main {

    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {
            int A = Math.abs(a);
            int B = Math.abs(b);

            if(A>B) return A-B;
            else if(A==B){
                if(a>b) return 1;
                else return -1;
            }

            else
                return -1;
        });

        for(int i=0; i<N; i++){
            int tmp = Integer.parseInt(bf.readLine());
            if(tmp != 0){
                pq.offer(tmp);
            }else{
                if(pq.isEmpty()){
                    System.out.println(0);
                }else{
                    int min = pq.poll();
                    System.out.println(min);
                }
            }
        }
    }

}

