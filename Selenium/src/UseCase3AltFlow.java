

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.junit.Assert;


public class UseCase3AltFlow {
	
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        System.setProperty("webdriver.chrome.driver", "C:\\ProgramData\\chocoportable\\lib\\chromedriver\\tools\\chromedriver.exe");

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

		
		WebElement postMessage2 =  driver.findElement(By.id("undefined"));
		postMessage2.sendKeys("I want know about hululu");
		postMessage2.sendKeys(Keys.RETURN);
		
		/*
		 * try { driver.manage().timeouts().wait(3000); } catch (InterruptedException e)
		 * { // TODO Auto-generated catch block e.printStackTrace(); }
		 */
		
		
		//wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//wait.withTimeout(2, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		//wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("https://numpy.org/")));
		//driver.manage().timeouts().implicitlyWait( 10, TimeUnit.SECONDS );
		
		//driver.manage().timeouts().implicitlyWait( 10, TimeUnit.SECONDS );
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//System.out.println(js.executeScript("return Date()"));
		/*
		 * if(js.executeScript("document.").toString().equals("complete")) {
		 * 
		 * 
		 * }
		 */
		List<WebElement> messages= driver.findElements(By.className("c-message__body"));
		System.out.println(messages.get(messages.size()-1).getText());
		//Assert.assertEquals("I am sorry, we are still working and building our database!");
		try {
		Assert.assertEquals("I am sorry, we are still working and building our database!", messages.get(messages.size()-1).getText());
		System.out.println("Test for alternate path is verified");
		}catch(AssertionError e) {
			System.out.println("Test for alternate path has failed");
		}

}
}
