package com.kata.potter;

public class BookPriceCalculator {

    private static final double STANDARD_BOOK_PRICE = 8.0;
    private static final double ZERO_PERCENT_OF_DISCOUNT = 0.0;
    private static final double FIVE_PERCENT_OF_DISCOUNT = 0.05;

    private Distinguisher<String> distinguisher;

    public BookPriceCalculator(Distinguisher<String> distinguisher) {
        this.distinguisher = distinguisher;
    }

    public Double getTotalPrice(String[] items) {
        Double price = STANDARD_BOOK_PRICE * items.length;
        Double discount = getDiscount(items);
        return price - discount;
    }

    public Double getDiscount(String[] items) {
        int numberOfDifferentBooks = distinguisher.getNumberOfUniqueValues(items);
        Double percent_of_discount = ZERO_PERCENT_OF_DISCOUNT;
        if (numberOfDifferentBooks == 2) {
            percent_of_discount = FIVE_PERCENT_OF_DISCOUNT;
        }
        return STANDARD_BOOK_PRICE * numberOfDifferentBooks * percent_of_discount;
    }
}
