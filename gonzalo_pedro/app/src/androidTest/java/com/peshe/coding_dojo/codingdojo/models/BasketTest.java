package com.peshe.coding_dojo.codingdojo.models;

import android.test.InstrumentationTestCase;

/**
 * Created by pedroduran on 18/4/15.
 */
public class BasketTest extends InstrumentationTestCase {

    public static final double BOOK_PRICE = 8;

    public static double getPrice(int bookNumber) {
        double discount = 0;
        switch (bookNumber) {
            case 2:
                discount = 0.05;
                break;
            case 7:
                discount = 0.45;
                break;
            default:
                break;
        }
        return bookNumber * BOOK_PRICE * (1 - discount);
    }

    public static double getPrice(int bookNumber, int collectionNumber) {
        return getPrice(bookNumber) * collectionNumber;
    }

    public void test1BookIs8Eur() throws Exception {
        assertEquals(getPrice(1), BOOK_PRICE);
    }

    public void test1BookType1and1BookType2HasDiscount() throws Exception {
        double precioType1 = BOOK_PRICE;
        double precioType2 = BOOK_PRICE;
        double precioTotalWithDiscount = (precioType1 + precioType2) * 0.95;

        assertEquals(getPrice(2), precioTotalWithDiscount);
    }

    public void testAllCollectionHas45PercentDiscount(){
        int numberOfBooks = 7;
        double totalPriceWithDiscount = (7 * BOOK_PRICE) * 0.55;
        assertEquals(getPrice(7), totalPriceWithDiscount);
    }

    public void test5Collections() throws Exception {
        int numberOfBooks = 7;
        double totalPriceWithDiscount = ((7 * BOOK_PRICE) * 0.55) * 5;
        assertEquals(getPrice(numberOfBooks, 5), totalPriceWithDiscount);
    }
}
