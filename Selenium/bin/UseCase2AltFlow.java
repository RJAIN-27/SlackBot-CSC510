import java.awt.AWTException;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;
import java.util.List;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UseCase2AltFlow {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String workspace = System.getenv("LIBRA_WORKSPACE");//"rajshreegroup";
		String botURL = System.getenv("LIBRA_URL");//"https://app.slack.com/client/TPDPYLR63/CPDPYM023";
		String loginEmail = System.getenv("SLACK_EMAIL");
		String loginPassword = System.getenv("SLACK_PASSWORD");

		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get(botURL);

		WebDriverWait wait = new WebDriverWait(driver, 30);

		// Wait until page loads workspace field
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("domain")));
		WebElement domain = driver.findElement(By.id("domain"));
		domain.sendKeys(workspace);

		WebElement continuebtn = driver.findElement(By.id("submit_team_domain"));
		continuebtn.click();

		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		WebElement password = driver.findElement(By.id("password"));

		// Enter slack email and password
		email.click();
		email.sendKeys(loginEmail);
		password.click();
		password.sendKeys(loginPassword);

		// Click to go into library bot channel
		WebElement signIn = driver.findElement(By.id("signin_btn"));
		signIn.click();

		// post message to libra bot with csv file
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("undefined")));
		WebElement postMessage = driver.findElement(By.id("undefined"));
		postMessage.sendKeys("Hey, Libra please analyze this dataset");

		WebElement uploadImage = driver.findElement(By.className("p-message_input_file_button"));
		uploadImage.click();
		try {
			Thread.sleep(1200);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		  List<WebElement> dropdowns = driver.findElements(By.className("c-menu_item__button")); 
		  WebElement yourComputer = dropdowns.get(dropdowns.size()-1);
		  yourComputer.click();
		  Robot robot = null;
		  try {
			robot = new Robot();
		} catch (AWTException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		  robot.setAutoDelay(2000);
		  
		  //uploading file
		  //Ctrl+c
		  StringSelection stringSelection = new StringSelection("C:\\Users\\mouni\\eclipse-workspace\\Selenium\\Wine.csv");
		  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(stringSelection, null);
		  
		  robot.setAutoDelay(1000);
		  
		  //Ctrl+v
		  robot.keyPress(KeyEvent.VK_CONTROL);
		  robot.keyPress(KeyEvent.VK_V);
		  
		  robot.keyRelease(KeyEvent.VK_CONTROL);
		  robot.keyRelease(KeyEvent.VK_V);
		  
		  robot.setAutoDelay(500);
		  robot.keyPress(KeyEvent.VK_ENTER);
		  robot.keyRelease(KeyEvent.VK_ENTER);
		  
		  List<WebElement> buttons = driver.findElements(By.className("c-button")); 
		  WebElement uploadButton = buttons.get(buttons.size()-1);
		  uploadButton.click();
		  
		  
		//Here , we need to wait for the bot's response
			try {
				Thread.sleep(3000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		  
		  System.out.println("UseCase2AltFlowVerification:");
		  //receive bot's response
		  List<WebElement> messages= driver.findElements(By.className("c-message__body"));
		  
		  try {
				Assert.assertEquals("Please provide the target column", messages.get(messages.size()-1).getText());
				System.out.println("bot requests target column is verified successfully");
			} catch (AssertionError e) {
			    System.out.println("bot requests target column verification is failed");
			}
		  
		  //sending the target column
		  WebElement targetColumn =  driver.findElement(By.id("undefined"));
		  targetColumn.sendKeys("Cless");
		  targetColumn.sendKeys(Keys.RETURN);
		  
		  //Here , we need to wait for the bot's response
			try {
				Thread.sleep(8000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			messages= driver.findElements(By.className("c-message__body"));
			//System.out.println(messages.get(messages.size()-1).getText());
			
			//asserting error column message
			try {
				Assert.assertEquals("The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive.", messages.get(messages.size()-1).getText());
				System.out.println("Target column not found error message is verfied successfully");
			} catch (AssertionError e) {
			    System.out.println("Target column not found error message verification failed");
			}
	}

}
