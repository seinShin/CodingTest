
import java.util.*;
import java.io.*;
public class Main {


    public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));


    while(true){
        String st = bf.readLine();
        boolean sts = true;
        if(st.equals(".")) break;

        Stack<Character> stack = new Stack<>();
        for(char c : st.toCharArray()){
            if(c=='(' || c=='['){
                stack.push(c);
            }else if((c==')' || c==']') ){
                if(!stack.isEmpty()){
                    if((c==')' && stack.peek() == '(') || (c==']' && stack.peek() == '[')){
                        stack.pop();
                    }else{
                        sts=false;
                    }
                }else{
                    sts=false;
                    break;
                }

            }
        }

        if(stack.isEmpty() && sts) System.out.println("yes");
        else System.out.println("no");

    }

    }
}
