package org.example;

import org.junit.jupiter.api.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.concurrent.TimeUnit;

public class TestOnlineReplenishmentBlock {
    static WebDriver driver = new ChromeDriver();
    static OnlineReplenishmentBlock onlineReplenishmentBlock = new OnlineReplenishmentBlock(driver);
    static String url = "https://www.mts.by/";

    @BeforeAll
    public static void initDriver(){
        Website.openWebsite(url);
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void blockName(){
        Assertions.assertEquals(onlineReplenishmentBlock.name(onlineReplenishmentBlock.blockName), "Онлайн пополнение\nбез комиссии");
        }

    @Test
    public void logoVisa(){
        Assertions.assertTrue(onlineReplenishmentBlock.iconDisplay(onlineReplenishmentBlock.logoVisa));
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.logoVisa, "alt"), "Visa");
    }

    @Test
    public void logoVerifiedByVisa(){
        Assertions.assertTrue(onlineReplenishmentBlock.iconDisplay(onlineReplenishmentBlock.logoVerifiedByVisa));
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.logoVerifiedByVisa, "alt"), "Verified By Visa");
    }

    @Test
    public void logoMasterCard(){
        Assertions.assertTrue(onlineReplenishmentBlock.iconDisplay(onlineReplenishmentBlock.logoMasterCard));
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.logoMasterCard, "alt"), "MasterCard");
    }

    @Test
    public void logoMasterCardSecureCode(){
        Assertions.assertTrue(onlineReplenishmentBlock.iconDisplay(onlineReplenishmentBlock.logoMasterCardSecureCode));
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.logoMasterCardSecureCode, "alt"), "MasterCard Secure Code");

    }

    @Test
    public void logoBelcart(){
        Assertions.assertTrue(onlineReplenishmentBlock.iconDisplay(onlineReplenishmentBlock.logoBelcart));
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.logoBelcart, "alt"), "Белкарт");
    }

    @Test
    public void linkMoreAboutService() {
        onlineReplenishmentBlock.click(onlineReplenishmentBlock.linkMoreAboutService);
        Assertions.assertEquals(onlineReplenishmentBlock.url(), "https://www.mts.by/help/poryadok-oplaty-i-bezopasnost-internet-platezhey/");
        Website.openWebsite(url);
    }

    @Test
    public void placeholdersCommunicationServices(){
        onlineReplenishmentBlock.choosingPaymentOption(onlineReplenishmentBlock.communicationServices);
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.phoneNumberField, "placeholder"),"Номер телефона");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.amountCommunicationServicesField, "placeholder"),"Сумма");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.emailCommunicationServicesField, "placeholder"),"E-mail для отправки чека");
    }

    @Test
    public void placeholdersHomeInternet(){
        onlineReplenishmentBlock.choosingPaymentOption(onlineReplenishmentBlock.homeInternet);
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.subscriberNumberField, "placeholder"),"Номер абонента");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.amountHomeInternetField, "placeholder"),"Сумма");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.emailHomeInternetField, "placeholder"),"E-mail для отправки чека");
    }

    @Test
    public void placeholdersInstalment(){
        onlineReplenishmentBlock.choosingPaymentOption(onlineReplenishmentBlock.instalment);
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.accountNumberFor44, "placeholder"),"Номер счета на 44");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.amountInstalmentField, "placeholder"),"Сумма");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.emailInstalmentField, "placeholder"),"E-mail для отправки чека");
    }

    @Test
    public void placeholdersArrears(){
        onlineReplenishmentBlock.choosingPaymentOption(onlineReplenishmentBlock.arrears);
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.accountNumberFor2073, "placeholder"),"Номер счета на 2073");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.amountArrearsField, "placeholder"),"Сумма");
        Assertions.assertEquals(onlineReplenishmentBlock.attributeSearch(onlineReplenishmentBlock.emailArrearsField, "placeholder"),"E-mail для отправки чека");
    }

    @Test
    public void switchToPayConnection(){
        Assertions.assertInstanceOf(PayConnection.class, onlineReplenishmentBlock.payConnection("297777777", "10"));
        Website.openWebsite(url);
    }

    @AfterAll
    public static void closeDriver(){
        driver.quit();
    }
}


