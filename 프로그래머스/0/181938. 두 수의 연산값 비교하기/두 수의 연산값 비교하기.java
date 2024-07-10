class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int tmp = Integer.parseInt(""+a+b);
        int tmp2 = 2*a*b;
        
        answer = tmp>tmp2 ? tmp :tmp2;
        return answer;
    }
}