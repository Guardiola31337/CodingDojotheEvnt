package com.kata.potter;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/**
 * FIRST: Fast, Independent, Repeatable, Self-Validating, Timely AAA: Arrange (Crea instances), Act (Method under test),
 * Assert (Verification) Test doubles: Dummy: Return nothing (used when a parameter is needed for the tested method but
 * without actually needing to use the parameter) Stub: Return default value (used for providing the tested code with
 * "indirect input") Spy: Validate call to certain method (used for verifying "indirect output" of the tested code, by
 * asserting the expectations afterwards, without having defined the expectations before the tested code is executed)
 * Mock: Fake the instance (used for verifying "indirect output" of the tested code, by first defining the expectations
 * before the tested code is executed) Fake: (in-memory database in the tests instead of doing real database access)
 * SOLID Single Responsibility Open/Closed Liskov substitution Interface Segregation Dependency inversion
 */
public class BookPriceCalculatorTest {

    private BookPriceCalculator bookPriceCalculator;
    private Distinguisher<String> distinguisher;

    @Before
    public void setUp() {
        distinguisher = new Distinguisher<>();
        bookPriceCalculator = new BookPriceCalculator(distinguisher);
    }

    @Test
    public void twoDifferentsBooksHas5PerrcentOfDiscount() {
        String[] bookTitles = new String[] { "book_1", "book_2" };

        Double result = bookPriceCalculator.getTotalPrice(bookTitles);

        Double expectedDiscount = 16.0 - 16 * 0.05;
        Assert.assertEquals(expectedDiscount, result);
    }

    @Test
    public void twoEqualBooksPriceIs16() {
        String[] bookTitles = new String[] { "book_1", "book_1" };

        Double result = bookPriceCalculator.getTotalPrice(bookTitles);

        Double expectedResult = 16.0;
        Assert.assertEquals(expectedResult, result);
    }

}
