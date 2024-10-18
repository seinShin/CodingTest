import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        char[] x = X.toCharArray();
        char[] y = Y.toCharArray();
        
        Arrays.sort(x);
        Arrays.sort(y);
        
        StringBuilder answer = new StringBuilder();  
        int idxX = x.length-1;
        int idxY = y.length-1;
        
        while(idxX >=0 && idxY >=0){
            if(x[idxX] == y[idxY]){
                answer.append(x[idxX]);
                idxX--;
                idxY--;
            }
            
            else if(x[idxX] > y[idxY]){
                idxX--;
            }else{
                idxY--;
            }
        }
        
        if(answer.length() == 0) return "-1";
        
        if(answer.toString().matches("0+")) return "0";
        
        return answer.toString();
    }
}