
public class LanternFish {
	
	protected int timer;
	
	public LanternFish() {
		timer = 6;
	}
	public LanternFish(int timer) {
		this.timer = timer;
	}
	public void setTimer(int timer) {
		this.timer = timer;
	}
	public void decrement() {
		this.timer -= 1;
	}
	public String toString() {
		return String.valueOf(timer);
	}
}
