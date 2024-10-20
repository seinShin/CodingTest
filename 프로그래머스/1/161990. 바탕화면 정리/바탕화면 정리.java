import java.util.*;
import java.lang.*;
class Solution {
    public int[] solution(String[] wallpaper) {
        int xMax = wallpaper.length;
        int yMax = wallpaper[0].length();
        int[] answer = {xMax,yMax, 0, 0};
        
        for(int i=0; i<xMax; i++){
            for(int j=0; j<yMax; j++){
                if(wallpaper[i].charAt(j) == '#'){
                    answer[0] = Math.min(answer[0], i);
                    answer[1] = Math.min(answer[1], j);
                    answer[2] = Math.max(answer[2], i+1);
                    answer[3] = Math.max(answer[3], j+1);
                }
            }
        }
        return answer;
    }
}