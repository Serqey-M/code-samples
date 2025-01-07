package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class Cookie extends Website{
    By buttonCookie = By.xpath("/html/body/div[6]/main/div/div[2]/div/div[2]/button[2]");

    public Cookie(WebDriver driver) {
        super(driver);
    }
}
