
import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int size;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        int count=0;
        int plus=1;
        int num=10;

        for(int i=1; i<=N; i++){
            if(i%num == 0){
                plus++;
                num*=10;
            }
            count+= plus;
        }

        System.out.println(count);
        bf.close();
    }
}
