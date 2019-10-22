import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class testclass {
	
	public static void main(String[] args) {
		
		
		String fileName = "Wine.csv";
		File file = new File(fileName);
		
		try {
			Scanner inputStream = new Scanner(file);
			StringBuffer sb = new StringBuffer();
			
			while(inputStream.hasNext()) 
			{
				String data = inputStream.nextLine();
				sb.append(data+"\n");
				
			}
			inputStream.close();
			System.out.println(sb);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
