class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int product=1;
        int sum=0;
        
        for(int i : num_list){
            sum+=i;
            product*=i;
        }
        
        if(sum*sum > product) answer=1;
        else answer=0;
        
        return answer;
    }
}