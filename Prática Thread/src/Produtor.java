
public class Produtor implements Runnable{
	private Thread t;
	private int cooldown;
	private Deposito dep;
	
	public Produtor(Deposito dep, int cooldown) {
		this.dep = dep;
		this.cooldown = cooldown;
	}
	
	
	public void run() {
		int i = 0;
		boolean sucesso;
		while(i < 100){
		
			sucesso = dep.colocar();

			if (sucesso) {
				i += 1;
			}
			
			try {
				Thread.sleep(this.cooldown);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
	
	   public void start () {
		   if (t == null){
	         t = new Thread(this);
	         t.start ();
		   }
	   }
}
