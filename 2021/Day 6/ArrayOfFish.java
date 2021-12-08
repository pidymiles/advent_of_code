import java.util.*;
import java.io.*;


public class ArrayOfFish {

	private static ArrayList<LanternFish> arrayOfFish = new ArrayList<LanternFish>();
	
	//Recursion
	public static void day (int d) {
		if (d <= 0) {
			System.out.print("There are "+ arrayOfFish.size() + " fish surrounding the submarine");
			return;
		}
		else {
			for (LanternFish f : arrayOfFish) {
				f.decrement();
			}
			for (int i = 0; i < arrayOfFish.size(); i++) {
				if (arrayOfFish.get(i).timer == -1) {
					arrayOfFish.add(new BabyLanternFish());	
					arrayOfFish.get(i).setTimer(6);	
				}
			}	
		}
		d--;
		day(d);
	}
	
	public static void main (String[] args) throws IOException {
		//input.txt
		File in = new File("input.txt");
		BufferedReader br = new BufferedReader(new FileReader(in));
		//Parse input to int
		List<String> raw_input = Arrays.asList(br.readLine().split(","));
		List<Integer> expected_input = new ArrayList<Integer>();
		for (String num : raw_input) {
			expected_input.add(Integer.parseInt(num));
		}
		//Create Parent Fish
		for (int i = 0; i < expected_input.size(); i++) {
			arrayOfFish.add(new LanternFish(expected_input.get(i)));
		}
		//Run recursive method
		day(80);
	}
}

