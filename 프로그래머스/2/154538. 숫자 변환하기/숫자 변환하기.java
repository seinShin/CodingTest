import java.util.*;
class Solution {
    static int max = 1000000;
    static int[] nums = new int[max+1];
    static boolean[] visited = new boolean[max+1];
    
    public int solution(int x, int y, int n) {
        
        Arrays.fill(nums, -1);
        Arrays.fill(visited, false);
        
        // PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        Queue<Integer> q = new LinkedList<>();
        q.offer(x);
        nums[x] = 0;
        
        while(!q.isEmpty()){
            int cur = q.poll();
            visited[cur] = true;
            
            if(cur == y) break;
            
            if(cur*3 >=1 && cur*3 <=max&& !visited[cur*3]){
                q.offer(cur*3);
                nums[cur*3] = nums[cur]+1;
                visited[cur*3]=true;
            }
            if(cur*2 >=1 && cur*2 <= max&& !visited[cur*2]){
                q.offer(cur*2);
                nums[cur*2] = nums[cur]+1;
                visited[cur*2]=true;
            }
            if(cur+n >=1 && cur+n <= max && !visited[cur+n]){
                q.offer(cur+n);
                nums[cur+n] = nums[cur]+1;
                visited[cur+n]=true;
            }
            
        }
        
    
        return nums[y];
    }
}