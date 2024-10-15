import java.util.*;
class Solution {
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> answer = new Stack<>();
    
    public int solution(int[] order) {
        int con=0;
        int idx=1;
        
        while(con < order.length){
            int target = order[con];
            
            if(idx == target){
                answer.push(idx);
                idx++;
                con++;
                
                while(!s1.isEmpty() && s1.peek() == order[con]){
                    answer.push(s1.pop());
                    con++;
                }
            }else{
                if(!s1.isEmpty() && idx == order.length) break;
                s1.push(idx);
                idx++;
            }
        }
        
    
        
        return answer.size();
    }
}