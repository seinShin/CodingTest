class Solution {
    boolean solution(String s) {
        boolean answer = false;
        int pCnt = 0;
        int yCnt = 0;
        
        for(char c : s.toCharArray()){
            if(c == 'p' || c == 'P') pCnt++;
            else if(c=='y' || c=='Y') yCnt++;
        }
        
        if(pCnt == yCnt) answer = true;

        return answer;
    }
}