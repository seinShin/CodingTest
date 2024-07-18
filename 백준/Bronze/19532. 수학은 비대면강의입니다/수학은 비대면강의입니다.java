
import java.util.*;

public class Main {
    static int a,b,c,d,e,f;

    static int x,y;
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        a=sc.nextInt();
        b=sc.nextInt();
        c=sc.nextInt();
        d=sc.nextInt();
        e=sc.nextInt();
        f=sc.nextInt();

        for(int i=-999; i<=999; i++){
            for(int j=-999; j<=999; j++){
                if((i*a + b*j == c) && (i*d + e*j == f)){
                    x=i;
                    y=j;
                    break;
                }
            }
        }

        System.out.println(x+" "+y);

    }
}
