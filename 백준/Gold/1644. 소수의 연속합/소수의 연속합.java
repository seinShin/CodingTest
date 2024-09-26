
import java.io.*;
import java.util.*;
public class Main {

    static int N;

    static List<Integer> arr = new ArrayList<>();
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        for(int i=2; i<=N; i++){
            if(isPrime(i)){
                arr.add(i);
            }
        }

        int start=0;
        int end=0;
        int sum=2;
        int cnt=0;

        while(start<arr.size()){
            if(sum == N){
                cnt++;
                sum-=arr.get(start);
                start++;
            }else if(sum>N){
                sum-=arr.get(start);
                start++;
            }else{
                end++;
                if(end>=arr.size()) break;
                sum+=arr.get(end);
            }

            if(start == end && sum == 0) break;
//            System.out.println(sum + " "+start+ " "+ end);
        }

        System.out.println(cnt);
    }

    public static boolean isPrime(int x){
        for(int i=2; i<=(int)Math.sqrt(x);i++){
            if(x%i==0){
                return false;
            }
        }
        return true;
    }

}
