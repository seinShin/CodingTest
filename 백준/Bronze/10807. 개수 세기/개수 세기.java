
import java.util.*;
public class Main {
    static int N;
    static int V;
    static int answer;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i< N; i++){
            arr[i] = sc.nextInt();
        }
        V = sc.nextInt();

        for(int i=0; i< N; i++){
            if(V == arr[i]) answer++;
        }

        System.out.println(answer);

    }
}

