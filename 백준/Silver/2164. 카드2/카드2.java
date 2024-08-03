
import java.util.*;

public class Main {

    static int N;
    static Deque<Integer> cards = new LinkedList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for(int i=1; i<=N; i++){
            cards.add(i);
        }

        while(cards.size() > 1){
            cards.poll();
            cards.add(cards.poll());
            if(cards.size() == 1) break;
        }

        System.out.println(cards.poll());
    }
}
