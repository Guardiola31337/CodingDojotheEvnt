package com.kata.potter;

import org.junit.Assert;
import org.junit.Test;

public class DistinguisherTest {

    private Distinguisher<String> distinguisher = new Distinguisher<>();

    @Test
    public void calculateDifferentsItemsWithTwoDifferent() {
        String[] items = new String[] { "book_1", "book_2" };

        int result = distinguisher.getNumberOfUniqueValues(items);
        Assert.assertEquals(result, 2);
    }

    @Test
    public void calculateDifferentsItemsWithTwoThatAreTheSame() {
        String[] items = new String[] { "book_1", "book_1" };

        int result = distinguisher.getNumberOfUniqueValues(items);
        Assert.assertEquals(result, 1);
    }
}
