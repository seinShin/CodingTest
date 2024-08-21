
import java.io.*;
import java.util.*;

public class Main {

    static int T;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(bf.readLine());

        for(int i=0; i<T; i++){
            String[] vps = bf.readLine().split("");
            Stack<String> st = new Stack<>();

            for (String vp : vps) {
                if (!st.isEmpty() && vp.equals(")") && st.peek().equals("(")) {
                    st.pop();
                } else {
                    st.push(vp);
                }
            }

            if(st.isEmpty()) System.out.println("YES");
            else System.out.println("NO");

        }

    }
}
