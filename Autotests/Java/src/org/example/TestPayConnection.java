package org.example;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;
import java.util.concurrent.TimeUnit;

public class TestPayConnection {
    static String phoneNumber = "297777777";
    static String amount = "10";
    static WebDriver driver = new ChromeDriver();
    static PayConnection payConnection = new PayConnection(driver, phoneNumber, amount);
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));


    @BeforeAll
    public static void initDriver() {
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void switchTo(){
        Assertions.assertInstanceOf(PayConnection.class, payConnection);
    }

    @Test
    public void headingAmount(){
        Assertions.assertEquals(payConnection.name(payConnection.headingAmount), String.format("%.2f", Float.parseFloat(amount)).replace(",",".") + " BYN");
    }

    @Test
    public void nameButton(){
        Assertions.assertEquals(payConnection.name(payConnection.button), "Оплатить " + String.format("%.2f", Float.parseFloat(amount)).replace(",",".") + " BYN");
    }

    @Test
    public void headingPhoneNumber(){
        Assertions.assertEquals(payConnection.name(payConnection.headingPhoneNumber), "Оплата: Услуги связи Номер:375" + phoneNumber);
    }

    @Test
    public void labelCardNumber(){
        Assertions.assertEquals(payConnection.name(payConnection.labelCardNumber), "Номер карты");
    }

    @Test
    public void labelValidityPeriod(){
        Assertions.assertEquals(payConnection.name(payConnection.labelValidityPeriod), "Срок действия");
    }

    @Test
    public void labelCVC(){
        Assertions.assertEquals(payConnection.name(payConnection.labelCVC), "CVC");
    }

    @Test
    public void labelNameHolder(){
        Assertions.assertEquals(payConnection.name(payConnection.labelNameHolder), "Имя держателя (как на карте)");
    }

    @Test
    public void logoVisa(){
        Assertions.assertTrue(payConnection.iconDisplay(payConnection.logoVisa));
    }

    @Test
    public void logoMasterCard(){
        Assertions.assertTrue(payConnection.iconDisplay(payConnection.logoMasterCard));
    }

    @Test
    public void logoBelcart(){
        Assertions.assertTrue(payConnection.iconDisplay(payConnection.logoBelcart));
    }

    @Test
    public void logo() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(payConnection.logoMaestro));
        Assertions.assertTrue(payConnection.iconDisplay(payConnection.logoMaestro));
    }

    @Test
    public void logoMir(){
        wait.until(ExpectedConditions.visibilityOfElementLocated(payConnection.logoMir));
        Assertions.assertTrue(payConnection.iconDisplay(payConnection.logoMir));
    }

    @AfterAll
    public static void closeDriver(){
        driver.quit();
    }
}