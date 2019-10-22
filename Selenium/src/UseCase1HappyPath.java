import java.util.List;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UseCase1HappyPath {


	//@SuppressWarnings("deprecation")
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String workspace = "rajshreegroup";
		String botURL = "https://app.slack.com/client/TPDPYLR63/CPDPYM023";
		String loginEmail = "vnukala2@ncsu.edu";
		String loginPassword = "Mani@1234";
		
		System.setProperty("webdriver.chrome.driver","chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get(botURL);
		
		WebDriverWait wait = new WebDriverWait(driver, 30);
		
		// Wait until page loads workspace field
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("domain")));
		WebElement domain =  driver.findElement(By.id("domain"));
		domain.sendKeys(workspace);
		
		WebElement continuebtn =  driver.findElement(By.id("submit_team_domain"));	
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
		
		//post message to libra bot with csv file
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("undefined")));
		//WebElement postMessage =  driver.findElement(By.id("undefined"));
		//postMessage.sendKeys("Hey bot suggest a machine learning model for this dataset");
		
		WebElement uploadImage = driver.findElement(By.className("p-message_input_file_button"));
		uploadImage.click();
		try {
			Thread.sleep(1200);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		/*
		 * List<WebElement> dropdowns =
		 * driver.findElements(By.className("c-menu_item__button")); WebElement
		 * yourComputer = dropdowns.get(dropdowns.size()-1); yourComputer.click();
		 * yourComputer.sendKeys("C:\\Users\\mouni\\Downloads\\Spectrum.pdf");
		 */
		WebElement createNew = driver.findElement(By.className("c-menu_item__button"));
		createNew.click();
		
		List<WebElement> buttons  = driver.findElements(By.className("c-menu_item__button"));
		WebElement codeSnippet = buttons.get(buttons.size()-2);
		codeSnippet.click();
		
		//waiting for the pop up
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("snippet-editor-filename")));
		
		
		//entering the title
		WebElement title = driver.findElement(By.name("snippet-editor-filename"));
		title.sendKeys("Wine.csv");
		
		//enter the csv data
		WebElement message = driver.findElement(By.id("share-dialog-message-input"));
		message.sendKeys("Hey bot suggest a machine learning model for this dataset");
		//enter Content
		//WebElement content = driver.findElement(By.className("CodeMirror-line"));
		//content.sendKeys("Inside content");
		
		JavascriptExecutor js = (JavascriptExecutor)driver;
		js.executeScript("var messages = document.getElementsByClassName('CodeMirror');messages[messages.length-1].innerText = 'Inside\\n';");
		/*
		 * List<WebElement> codes =
		 * driver.findElements(By.className("CodeMirror-code")); WebElement code =
		 * codes.get(codes.size()-1); code.sendKeys("Inside");
		 */
		
		
		//please refer this tomorrow
				/*
				 * var messages = document.getElementsByClassName('CodeMirror');
				 * messages[3].innerText = "sadfsadfasdf";
				 */
		
		//create Snippet Click
		
		  buttons = driver.findElements(By.className("c-button")); WebElement
		  createSnippet = buttons.get(buttons.size()-1); createSnippet.click();
		 
		
		
		
		
		
	}



}
