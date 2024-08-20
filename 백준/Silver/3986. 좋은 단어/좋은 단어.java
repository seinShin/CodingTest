
import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int answer=0;


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());


        for(int i=0; i<N; i++) {
            String word = bf.readLine();
            Stack<Character> st = new Stack<>();

            for(int j=0; j<word.length();j++){
                if(!st.isEmpty() && st.peek() == word.charAt(j)){
                    st.pop();
                }else{
                    st.push(word.charAt(j));
                }
            }
            if(st.empty()) answer++;
        }

        System.out.println(answer);

    }
}
