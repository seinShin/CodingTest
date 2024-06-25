import java.util.*;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Integer[] tmp = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(tmp, Collections.reverseOrder());
        
        int len = score.length/m;
       
        for(int i=0; i<len*m-1; i+=m) {
            answer+= tmp[i+m-1]*m;
        }
        return answer;
    }
}