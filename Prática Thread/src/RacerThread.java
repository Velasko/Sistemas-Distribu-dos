public class RacerThread extends Thread{
	private int i;

	public RacerThread(int id){
		i = id;
	}
	
	public void correr(){
		System.out.println("Racer " +  i + "- imprimindo");
	}
	
	public void run() {
		while(true){
			this.correr();

			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
