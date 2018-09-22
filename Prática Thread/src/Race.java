
public class Race {
	public static void main(String[] args) {
		int y = 0;
		Racer[] threads = new Racer[10];
		while(y < 10){
			threads[y] = new Racer(y);
			y += 1;
		}
		
		y = 0;
		while(y < 10){
			threads[y].start();
			y += 2;
		}
		
		y = 0;
		while(y < 10){
			threads[y].join();
			y += 2;
		}
		
		y = 1;
		while(y < 10){
			threads[y].start();
			y += 2;
		}
	}
}