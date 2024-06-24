import java.lang.Math;
class Solution {
    public static int divisor(int n){
        int cnt=0;
        for(int i=1; i<=Math.sqrt(n);i++){
            if(i*i==n) cnt++;
            else if(n%i==0) cnt+=2;
        }
        return cnt;
    }
    
    public int solution(int number, int limit, int power) {
        int answer = 0;

        for(int i=1; i<number+1;i++){
            int attack = divisor(i);
            if(attack>limit) answer+= power;
            else answer+= attack;
        }
        
        return answer;
    }
}