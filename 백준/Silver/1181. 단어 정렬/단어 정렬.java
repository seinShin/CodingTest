
import java.io.*;
import java.util.*;
public class Main {

    static int N;
    static String[] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        graph = new String[N];

        for(int i=0; i<N; i++){
            graph[i] = bf.readLine();
        }



        Arrays.sort(graph, (s1,s2)->{
           if(s1.length() == s2.length()){
               return s1.compareTo(s2);
           }else{
               return s1.length()-s2.length();
           }
        });

        System.out.println(graph[0]);
        for(int i=1; i<N; i++){
            if(!graph[i].equals(graph[i-1]))
                System.out.println(graph[i]);
        }
    }

}
