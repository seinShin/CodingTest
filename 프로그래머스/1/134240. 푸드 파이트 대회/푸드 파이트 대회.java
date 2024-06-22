class Solution {
    public String solution(int[] food) {
        String answer = "";
        
        for(int i=1; i< food.length;i++){
            String num = i+"";
            if(food[i]%2!=0){
                answer+=num.repeat((food[i]-1)/2);
            }else{
                answer+=num.repeat(food[i]/2);
            }
        }
        
        StringBuffer str = new StringBuffer(answer);
        
        return answer+"0"+str.reverse().toString();
    }
}