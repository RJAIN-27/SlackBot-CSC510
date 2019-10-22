import java.util.List;
import java.util.concurrent.TimeUnit;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


public class UseCase1AltFlow {
	
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        System.setProperty("webdriver.chrome.driver", "C:\\ProgramData\\chocoportable\\lib\\chromedriver\\tools\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
     		
		String workspace = "rajshreegroup";
		driver.get("https://app.slack.com/client/TPDPYLR63/CPDPYM023");

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
		email.sendKeys("nradhak2@ncsu.edu");
		password.sendKeys("Angelsanddemons5@");

		// Click
		WebElement signIn = driver.findElement(By.id("signin_btn"));
		signIn.click();
		
		
		//POST A MESSAGE TO ANALYZE THE DATA SET 
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("undefined")));
		WebElement postMessage =  driver.findElement(By.id("undefined"));
		postMessage.sendKeys("I want model suggestion for my dataset");
		
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
			
			System.out.println(messages.get(messages.size()-1).getText());
		
		
		/*
		 * try { driver.manage().timeouts().wait(3000); } catch (InterruptedException e)
		 * { // TODO Auto-generated catch block e.printStackTrace(); }
		 */
		
		
		//wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//wait.withTimeout(2, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("https://numpy.org/")));
		//driver.manage().timeouts().implicitlyWait( 10, TimeUnit.SECONDS );
		
		//driver.manage().timeouts().implicitlyWait( 10, TimeUnit.SECONDS );
		
		
		//assertequals here for bot asking for user dataset 
		

		
		//Fetch the messages from the bot for the return dataset 

		
		//System.out.println(js.executeScript("return Date()"));
		/*
		 * if(js.executeScript("document.").toString().equals("complete")) {
		 * 
		 * 
		 * }
		 */
		//List<WebElement> messages1= driver.findElements(By.className("c-message__body"));

		
		
		//assertequals for the response from the bot 
		


	}

}



