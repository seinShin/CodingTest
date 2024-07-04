

import java.util.*;
public class Main {
    static int N;
    static int X;
    static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        X = sc.nextInt();

        for(int i=0; i<N; i++){
            int tmp = sc.nextInt();
            if(tmp < X) list.add(tmp);
        }

        for(int i=0; i<list.size(); i++){
            System.out.print(list.get(i));
            System.out.print(" ");
        }
    }
}

