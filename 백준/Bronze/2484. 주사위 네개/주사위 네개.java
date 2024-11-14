import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // 선언
		
		int N = Integer.parseInt(br.readLine()); //참여수
		
		int reward = 0;
		int bestReward = 0;
		
		for(int i = 0; i<N;i++) { 	//참여 수 만큼 반복
			int maxDice = 0;			//최대 중복 주사위
			int secondDice = 0;			//최대 중복 주사위 2(중복건수가 2로 동일할시)
			int count = 0;				//중복 건수
			StringTokenizer st = new StringTokenizer(br.readLine());
			int[] dice = new int[4];	//주사위 배열
			for(int j = 0; j<4;j++) {	//이번 4개의 주사위를 불러온다.
				dice[j] = Integer.parseInt(st.nextToken());
			}
			
			
			for(int num=1; num<=6; num++) {	//1부터 6까지 반복한다.
				int tempCount = 0;
				for(int l=0; l<dice.length; l++) { //현재 저장된 4개 주사위를 가져온다.
					
					if(num==dice[l]) { 			//현재 수와 같은 주사위가 있을시 + 1
						tempCount = tempCount + 1;
					}
				}
				if(count<tempCount&&maxDice<num) { //더 큰 주사위 갯수가 많을시
					count = tempCount;
					maxDice = num;
					secondDice = 0;
				}else if(count==tempCount&&maxDice<num&&count==1) { // 중복이 없을시 가장 큰 주사위
					maxDice = num;
				}
				else if(count==tempCount) { //2개 2쌍
					secondDice = num;
				}
					
			}

			if(count == 4) {  //상금 계산
				reward = 50000+maxDice*5000; 
			}else if(count ==3) {
				reward = 10000+maxDice*1000; 
			}else if(count > 1&&secondDice > 0) {
				reward = 2000+maxDice*500+secondDice*500;
			}else if(count ==2) {
				reward = 1000+maxDice*100; 
			}else if(count == 1) {
				reward = maxDice*100;
			}
			
		/*	if(count > 1&&secondDice > 0) {
				bw.write("많은 주사위 : "+maxDice+"\n세컨 주사위2 : "+secondDice+"\n");
			}else{
				bw.write("많은 주사위"+maxDice+"\n");	
			}
			bw.write("중복 개수 : "+count+"개\n");
			bw.write("현재 상금 : "+reward+"\n");*/
			if(reward>bestReward) bestReward = reward; //최대 상금 갱신
		}
		bw.write(bestReward+"");
	
		bw.close();
		br.close();
	}
}