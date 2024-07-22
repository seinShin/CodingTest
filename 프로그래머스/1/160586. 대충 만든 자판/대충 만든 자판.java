import java.util.*;

class Solution {
    HashMap<Character,Integer> keyhash = new HashMap<>();
    
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        for(int i=0; i<keymap.length;i++){
            for(int j=0; j<keymap[i].length(); j++){
                char c = keymap[i].charAt(j);
                if(keyhash.containsKey(c)){
                    int tmpIdx = keyhash.get(c);
                    keyhash.put(c, Math.min(tmpIdx, j+1));
                }else{
                    keyhash.put(c,j+1);
                }
            }
        }
        
        for(int i=0; i<targets.length;i++){
            int cnt=0;
            boolean sts=true;
            for(int j=0; j<targets[i].length(); j++){
                char c = targets[i].charAt(j);
                if(!keyhash.containsKey(c)){
                    sts = false;
                    break;
                }
                cnt += keyhash.get(c);
            }
            
            if(!sts) answer[i] = -1;
            else answer[i] = cnt;
        }
        
        return answer;
    }
}