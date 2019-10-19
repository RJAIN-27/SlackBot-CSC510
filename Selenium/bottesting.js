const puppeteer = require('puppeteer')

const loginEmail = 'vnukala2@ncsu.edu';
const loginPassword = 'Mani@1234';
const workspace = 'rajshreegroup';
const slackURL = 'https://slack.com';
const userMessage = 'I want to know numpy';

async function login(browser, slackURL) {
    const page = await browser.newPage();
  
    await page.goto(slackURL, {waitUntil: 'networkidle0'});
    await page.type('input[id=domain]', workspace);
    await page.click('button[id=submit_team_domain]');
    await page.waitForSelector('#email');//waiting for the page to load
  
    // Login
    await page.type('input[id=email]', loginEmail);
    await page.type('input[id=password]', loginPassword);
    await page.click('button[id=signin_btn]');
  
    // Wait for redirect
    await page.waitForNavigation();
    return page;
  }
  async function libraryInfo(message) {
    
  }

  (async () => {

    const browser = await puppeteer.launch({headless: false, args: ["--no-sandbox", "--disable-web-security"]});
    let page = await login( browser, `${slackURL}/signin` );
    //await postMessage(page, "Hello world from browser automation" );
  
    // const html = await page.content(); // serialized HTML of page DOM.
    // browser.close();
  })()