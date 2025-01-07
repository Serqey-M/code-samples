package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;

public class OnlineReplenishmentBlock extends Website {
    String url = "https://www.mts.by/";
    By blockName = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/h2");
    By logoVisa = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[2]/ul/li[1]/img");
    By logoVerifiedByVisa = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[2]/ul/li[2]/img");
    By logoMasterCard = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[2]/ul/li[3]/img");
    By logoMasterCardSecureCode = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[2]/ul/li[4]/img");
    By logoBelcart = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[2]/ul/li[5]/img");
    By linkMoreAboutService = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/a");
    By paymentOption = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[1]/div[1]/div[2]/button");
    By communicationServices = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[1]/div[1]/div[2]/ul/li[1]/p");
    By homeInternet = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[1]/div[1]/div[2]/ul/li[2]/p");
    By instalment = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[1]/div[1]/div[2]/ul/li[3]/p");
    By arrears = By.xpath("//*[@id=\"pay-section\"]/div/div/div[2]/section/div/div[1]/div[1]/div[2]/ul/li[4]/p");
    By phoneNumberField = By.xpath("//*[@id=\"connection-phone\"]");
    By subscriberNumberField = By.xpath("//*[@id=\"internet-phone\"]");
    By accountNumberFor44 = By.xpath("//*[@id=\"score-instalment\"]");
    By accountNumberFor2073 = By.xpath("//*[@id=\"score-arrears\"]");
    By amountCommunicationServicesField = By.xpath("//*[@id=\"connection-sum\"]");
    By amountHomeInternetField = By.xpath("//*[@id=\"internet-sum\"]");
    By amountInstalmentField = By.xpath("//*[@id=\"instalment-sum\"]");
    By amountArrearsField = By.xpath("//*[@id=\"arrears-sum\"]");
    By emailCommunicationServicesField = By.xpath("//*[@id=\"connection-email\"]");
    By emailHomeInternetField = By.xpath("//*[@id=\"internet-email\"]");
    By emailInstalmentField = By.xpath("//*[@id=\"instalment-email\"]");
    By emailArrearsField = By.xpath("//*[@id=\"arrears-email\"]");
    By buttonPayConnection = By.xpath("//*[@id=\"pay-connection\"]/button");




    public OnlineReplenishmentBlock(WebDriver driver) {
        super(driver);
        OnlineReplenishmentBlock.openWebsite(url);
        Cookie cookie = new Cookie(driver);
        try {
            cookie.click(cookie.buttonCookie);
        }
        catch (NoSuchElementException ignored){
        }

    }

    public void choosingPaymentOption(By element){
        webElement(paymentOption).click();
        webElement(element).click();
    }
    public PayConnection payConnection (String phoneNumber, String amount){
        return new PayConnection(driver, phoneNumber, amount);
    }
}
