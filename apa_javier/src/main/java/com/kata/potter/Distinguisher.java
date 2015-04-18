package com.kata.potter;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Distinguisher<T> {

    public int getNumberOfUniqueValues(T[] items) {
        List<T> listOfItems = Arrays.asList(items);
        Set<T> uniqueItems = new HashSet<>(listOfItems);
        return uniqueItems.size();
    }
}
