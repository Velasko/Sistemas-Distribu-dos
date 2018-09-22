	public class Racer implements Runnable {
		private Thread t;
		private int i;

		public Racer(int id){
			i = id;
		}
		
		public void run() {
			int v = 0;
			while(v < 1000){
				System.out.println("Racer " +  i + "- imprimindo");
				v += 1;
			}
		}
		
	   public void start () {
		   if (t == null){
	         t = new Thread(this);
	         t.start ();
		   }
	   }
	   
	   public void join() {
		   if (t != null) {
			   try {
				t.join();
			   } catch (InterruptedException e) {
				e.printStackTrace();
			   }
		   }
	   }
	}

