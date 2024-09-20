
import java.util.*;
import java.io.*;
public class Main {

    static int N;
    static PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        for(int i=0; i<N; i++){
            int tmp = Integer.parseInt(bf.readLine());

            if(tmp==0){
                if(pq.isEmpty()){
                    System.out.println("0");
                }else{
                    int x = pq.poll();
                    System.out.println(x);
                }
            }else{
                pq.offer(tmp);
            }
        }
    }

}


