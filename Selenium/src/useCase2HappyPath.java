import java.util.List;
import java.util.concurrent.TimeUnit;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


public class UseCase2HappyPath {
	
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
        WebDriver driver = new ChromeDriver();
     		
        String workspace = System.getenv("SLACK_WORKSPACE");
		String Slack_url= System.getenv("SLACK_URL");
		String loginEmail = System.getenv("SLACK_EMAIL");
		String loginPass = System.getenv("SLACK_PASSWORD");
		driver.get(Slack_url);

		// Wait until page loads and we can see a sign in button.
		
		  WebDriverWait wait = new WebDriverWait(driver, 30);
		/*
		 * wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn"))
		 * );
		 */
		  
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("domain")));
		WebElement domain =  driver.findElement(By.id("domain"));
		domain.sendKeys(workspace);
		
		WebElement continuebtn =  driver.findElement(By.id("submit_team_domain"));	
		continuebtn.click();
		 
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("email")));
		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("password")));
		WebElement password = driver.findElement(By.id("password"));

		// Enter slack email and password
		email.sendKeys(loginEmail);
		password.sendKeys(loginPass);

		// Click
		WebElement signIn = driver.findElement(By.id("signin_btn"));
		signIn.click();

		
		
		//POST A MESSAGE TO ANALYZE THE DATA SET 
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("undefined")));
		WebElement postMessage =  driver.findElement(By.id("undefined"));
		postMessage.sendKeys("I want to analyze my dataset");
		
		//Upload dataset 
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
		  
		//UPLOADING THE FILE 
		  StringSelection stringSelection = new StringSelection("C:\\Users\\nitar\\Downloads\\ordergroups.csv");
		  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(stringSelection, null);
		  
		  robot.setAutoDelay(1000);
		  
		  //Ctrl+v
		  robot.keyPress(KeyEvent.VK_CONTROL);
		  robot.keyPress(KeyEvent.VK_V);
		  
		  robot.keyRelease(KeyEvent.VK_CONTROL);
		  robot.keyRelease(KeyEvent.VK_V);
		  
		  robot.setAutoDelay(1000);
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
			
			List<WebElement> messages= driver.findElements(By.className("c-message__body"));
			
			//System.out.println(messages.get(messages.size()-1).getText());
		
			try {
				Assert.assertEquals("Please provide the target column", messages.get(messages.size()-1).getText());
				System.out.println("Target Column request is verified successfully");
			} catch (AssertionError e) {
			    System.out.println("Target Column request verification is failed");
			}
		  
		  //sending the target column
		  WebElement targetColumn =  driver.findElement(By.id("undefined"));
		  //targetColumn.getAttribute("oncopy");
		  targetColumn.sendKeys("Class");
		  targetColumn.sendKeys(Keys.RETURN);
		  
		//Here , we need to wait for the bot's response
			try {
				Thread.sleep(8000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			
			List<WebElement> messages1= driver.findElements(By.className("c-message__body"));
			//System.out.println(messages1.get(messages1.size()-2).getText());
			//asserting error column message
			try {
				Assert.assertEquals("The information you asked is:", messages1.get(messages1.size()-2).getText());
				System.out.println("Test for happy path verfied successfully");
			} catch (AssertionError e) {
			    System.out.println("Test for happy path verification failed");
			}
		  
			try {
				Assert.assertEquals("Were you satisfied with the analysis?", messages1.get(messages1.size()-1).getText());
				System.out.println("Feedback verfied successfully");
			} catch (AssertionError e) {
			    System.out.println("Feedback verification failed");
			}
		  
			WebElement feedback =  driver.findElement(By.id("undefined"));
			feedback.sendKeys("yes");
			feedback.sendKeys(Keys.RETURN);
			
			//Here , we need to wait for the bot's response
					try {
						Thread.sleep(10000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					
			messages= driver.findElements(By.className("c-message__body"));
			
			//asserting feedback message
			try {
				Assert.assertEquals("Thankyou for the feedback", messages.get(messages.size()-1).getText());
				System.out.println("Feedback message is verified");
			} catch (AssertionError e) {
			    System.out.println("Feedback message verification failed");
			}
		  
		


	}

}
