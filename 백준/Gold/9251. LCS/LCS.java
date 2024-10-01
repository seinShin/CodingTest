
import java.io.*;
import java.util.*;
public class Main {

    static String a,b;
    static int[][] lcs;

    static String answer="";
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        a = bf.readLine();
        b = bf.readLine();

        lcs = new int[a.length()+1][b.length()+1];

        for(int i=0; i<a.length(); i++){
            for(int j=0; j<b.length(); j++){
                lcs[i][j] = 0;
            }
        }

        for(int i=1; i<a.length()+1; i++){
            for(int j=1; j<b.length()+1; j++){

                if(a.charAt(i-1) == b.charAt(j-1)){
                    lcs[i][j] = lcs[i-1][j-1]+1;
                }else{
                    lcs[i][j] = Math.max(lcs[i][j-1], lcs[i-1][j]);
                }
//                System.out.print(lcs[i][j]);
            }
//            System.out.println();
        }

        System.out.println(lcs[a.length()][b.length()]);

    }

}
