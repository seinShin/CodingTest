package codingTest_java.string;
import java.util.Scanner;
public class str_1157 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next().toLowerCase();

        int[] countArr = new int[26];

        for(int i=0; i<str.length();i++){
            char c = str.charAt(i);
            countArr[c-'a']++;
        }

        int maxCount=-1;
        char maxAlpha = '?';

        for(int i=0; i< 26; i++){
            if(countArr[i]>maxCount){
                maxCount = countArr[i];
                maxAlpha = (char)('A' + i);
            }
            else if(countArr[i] == maxCount){
                maxAlpha = '?';
            }
        }

        System.out.println(maxAlpha);
    }
}
