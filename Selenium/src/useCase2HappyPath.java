

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


public class useCase2HappyPath {
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
		
		//wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("undefined")));
		//WebElement postMessage =  driver.findElement(By.id("undefined"));
		//postMessage.sendKeys("I want to analyze my dataset");
		//postMessage.sendKeys(Keys.RETURN);
		//Upload dataset 
		WebElement uploadImage = driver.findElement(By.className("p-message_input_file_button"));
		uploadImage.click();
		try {
			Thread.sleep(1200);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		List<WebElement> dropdowns = driver.findElements(By.className("c-menu_item__button"));
		WebElement createNew = dropdowns.get(dropdowns.size()-2);
		createNew.click();
		
		List<WebElement> dropdowns1 = driver.findElements(By.className("c-menu_item__button"));
		//System.out.println(dropdowns1.get(dropdowns1.size()-1).getText());
		//System.out.println(dropdowns1.get(dropdowns1.size()-2).getText());
		//System.out.println(dropdowns1.get(dropdowns1.size()-3).getText());
		//System.out.println(dropdowns1.get(dropdowns1.size()-4).getText());
		//System.out.println(dropdowns1.get(dropdowns1.size()-5).getText());
		WebElement codeOrTextSnippet = dropdowns1.get(dropdowns1.size()-2);
		codeOrTextSnippet.click();
		
		//wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("CodeMirror-scroll")));
		
		//POST DUMMY MESSAGE IN TITLE BOX(WHERE THE NAME OF THE FILE SHOULD ACTUALLY BE) 
		WebElement postMessage1 = driver.findElement(By.id("snippet-name11"));
		//WebElement postMessages = postMessage1.get(postMessage1.size()-1);
		postMessage1.sendKeys("ordergroups");
		
		
		
		//postMessage1.sendKeys(Keys.RETURN);
		//WebElement uploadButton = driver.findElement(By.className("c-menu_item__icon"));
		//System.out.println(uploadButton.getText());
		//uploadButton.sendKeys("C:\\Users\\nitar\\Downloads\\ordergroups.csv");
		//uploadImage.click();
		
		
		//POST MESSAGE IN CONTENT BOX 
		//WebElement postMessage2 = driver.findElement(By.xpath("//pre[contains(@class,'CodeMirror-line')]"));
		//WebElement postMessages = postMessage1.get(postMessage1.size()-1);
		//System.out.println(postMessage2.get(postMessage2.size()-1).getText());
		//System.out.println(postMessage2.get(postMessage2.size()-2).getText());
		//System.out.println(postMessage2.get(postMessage2.size()-3).getText());
		//System.out.println(postMessage2.get(postMessage2.size()-4).getText());
		//System.out.println(postMessage2.get(postMessage2.size()-5).getText());
		//System.out.println(postMessage2.get(postMessage2.size()-6).getText());
		//WebElement pm = postMessage2.get(postMessage2.size()-1);
		//postMessage2.sendKeys("ordergroups");
		//postMessage2.sendKeys(Keys.RETURN);
		
		By preTagXpath = By.xpath("//pre[contains(@class,'CodeMirror-line')]");
        	JavascriptExecutor js = (JavascriptExecutor) driver;
        	String preValue = "This should be the new value";
        	js.executeScript("document.getElementsByTagName('pre')[1].innerText='" + preValue + "';");
        	System.out.println(driver.findElement(preTagXpath).getText());
		
		
		
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
