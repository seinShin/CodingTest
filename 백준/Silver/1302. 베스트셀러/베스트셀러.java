
import java.util.*;

public class Main {

    static int cnt=0;
    static int max=0;
    static HashMap<String, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        cnt = sc.nextInt();
        sc.nextLine();

        for(int i=0; i< cnt;i++){
            String s = sc.nextLine();
            if(map.get(s) == null) map.put(s, 1);
            else map.put(s, map.get(s)+1);
        }

        max=Collections.max(map.values());

        List<String> list = new ArrayList<>();
        for(HashMap.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue() == max) list.add(entry.getKey());
        }

        Collections.sort(list);
        System.out.println(list.get(0));

    }
}
