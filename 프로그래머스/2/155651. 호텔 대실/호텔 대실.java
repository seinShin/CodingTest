import java.util.*;
class Solution {
    
    public int solution(String[][] book_time) {
        int answer = 0;
        int[][] times = new int[book_time.length][2];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
     
        for(int i=0; i<book_time.length;i++){
            for(int j=0; j<2; j++){
                String[] tmp = book_time[i][j].split(":");
                times[i][j] =  Integer.parseInt(tmp[0]) * 60 + Integer.parseInt(tmp[1]);
            }
        }
        
        Arrays.sort(times, (a,b)-> {
            if(a[0]==b[0]) return Integer.compare(a[1], b[1]);
            else return Integer.compare(a[0], b[0]);
        });
        
        // 첫번째 세팅
        pq.add(times[0][1]+10);
        
        for(int i=1; i<times.length; i++){
            System.out.println("start "+times[i][0]);
            System.out.println(pq.peek());
            if(times[i][0]>=pq.peek()){
                pq.poll();
            }
            
            pq.add(times[i][1]+10);
            
        }
    
        answer = pq.size();
        return answer;
    }
    
}