import java.util.*;

class Solution {
    static List<String> list = new ArrayList<>();
    static String[] words = {"A", "E", "I", "O", "U"};
    public int solution(String word) {
        int answer = 0;
        
        dfs("", 0);
        int size = list.size();
        
        for(int i=0; i<size; i++){
            if(list.get(i).equals(word)){
                answer=i;
                break;
            }
        }
        
        return answer;
    
    }
    
    public void dfs(String str, int depth){
        list.add(str);
        if(depth == 5) return;
        
        for(int i=0 ;i<5; i++){
            dfs(str+words[i], depth+1);
        }
    }
}