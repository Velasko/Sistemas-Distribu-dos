
public class Consumidor implements Runnable{
	private Thread t;
	private int cooldown;
	private Deposito dep;
	
	public Consumidor(Deposito dep, int cooldown) {
		this.dep = dep;
		this.cooldown = cooldown;
	}
	
	
	public void run() {
		int i = 0;	//Iteracoes
		int cd; 	//CoolDown
		boolean sucesso;
		while(i < 20){
			sucesso = dep.retirar();
			if(sucesso) {
				cd = this.cooldown;
				i += 1;				
			}else {
				cd = 200;
			}

			try {
				Thread.sleep(cd);
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
