class Solution {
    public int solution(String s) {
        int answer=1;
        char x = s.charAt(0);
        int cnt =1;
        
        for(int i=1; i<s.length(); i++){
            if(cnt == 0){
                answer+=1;
                x=s.charAt(i);
            }
            
            if(x == s.charAt(i)){
                cnt+=1;
            }else{
                cnt-=1;
            }
        }
        
        return answer;
    }
}