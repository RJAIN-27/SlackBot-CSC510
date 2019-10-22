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
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.junit.Assert;


public class UseCase3HappyPath {

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
		email.sendKeys(loginEmail);
		password.sendKeys(loginPassword);

		// Click to go into library bot channel
		WebElement signIn = driver.findElement(By.id("signin_btn"));
		signIn.click();
		
		//post message to libra bot
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("undefined")));
		WebElement postMessage =  driver.findElement(By.id("undefined"));
		postMessage.sendKeys("I want know about numpy");
		postMessage.sendKeys(Keys.RETURN);
		
		//Here , we need to wait for the bot's response
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		List<WebElement> messages= driver.findElements(By.className("c-message__body"));
		//System.out.println(messages.get(messages.size()-2).getText());
		//library info verification
		try {
			Assert.assertEquals("NumPy is a very popular python library for large multi-dimensional array and matrix processing, with the help of a large collection of high-level mathematical functions. It is very useful for fundamental scientific computations in Machine Learning. It is particularly useful for linear algebra, Fourier transform, and random number capabilities. High-end libraries like TensorFlow uses NumPy internally for manipulation of Tensors. https://numpy.org/ https://docs.scipy.org/doc/numpy/reference/ http://cs231n.github.io/python-numpy-tutorial/", messages.get(messages.size()-2).getText());
			System.out.println("Library information is verified successfully");
		} catch (AssertionError e) {
		    System.out.println("Library information verification is failed");
		}
		
		try {
			Assert.assertEquals("Were you satisfied with the details?", messages.get(messages.size()-1).getText());
			System.out.println("Bot Question is verified successfully");
		} catch (AssertionError e) {
			System.out.println("Bot Question verification is failed");
		}
		
		WebElement feedback =  driver.findElement(By.id("undefined"));
		feedback.sendKeys("yes");
		feedback.sendKeys(Keys.RETURN);
		
		//Here , we need to wait for the bot's response
				try {
					Thread.sleep(5000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
		messages= driver.findElements(By.className("c-message__body"));
		
		//asserting feedback message
		try {
			Assert.assertEquals("Thankyou for the feedback", messages.get(messages.size()-1).getText());
			System.out.println("Feedback message is verified");
		} catch (AssertionError e) {
		    System.out.println("Feedback message is verification failed");
		}
		
		
		
		
		


	}

}
