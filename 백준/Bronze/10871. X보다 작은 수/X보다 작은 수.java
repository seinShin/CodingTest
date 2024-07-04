
import java.util.*;
public class Main {
    static int N;
    static int X;
    static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        X = sc.nextInt();
        
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<N; i++){
            int tmp = sc.nextInt();
            if(tmp < X) sb.append(tmp).append(" ");
        }

        System.out.println(sb);
    }
}

