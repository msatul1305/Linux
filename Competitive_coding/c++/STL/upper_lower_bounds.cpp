// Suppose we have a sorted array arr = {10, 20, 30, 30, 40, 50, 60}.

// If we search for 25:

// std::upper_bound will return an iterator to 30 (the first element greater than 25).
// std::lower_bound will return an iterator to 30 (the first element not less than 25).
// If we search for 30:

// std::upper_bound will return an iterator to 40 (the first element greater than 30).
// std::lower_bound will return an iterator to the first 30.
// If we search for 70:

// Both std::upper_bound and std::lower_bound will return an iterator to end() (as there is no element greater than or not less than 70).
// If we search for 5:

// Both std::upper_bound and std::lower_bound will return an iterator to the first 10 (the first element not less than 5).

// Definition:
// std::upper_bound: 
// This function returns an iterator pointing to the first element 
// in the range [first, last) that is greater than value, 
// or last if no such element is found. 
// Formally, it returns an iterator it such that !(*it < value) 
// for every iterator it in the range [first, last).

// std::lower_bound: This function returns an iterator pointing 
// to the first element in the range [first, last) that is 
// not less than (i.e., greater or equal to) value, or last if 
// no such element is found. 
// Formally, it returns an iterator it such that value <= *it 
// for every iterator it in the range [first, last).

#include <iostream>
#include <algorithm>

int main() {
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80};

    // Using upper_bound
    int* upper = std::upper_bound(arr, arr + 8, 35);
    if (upper != arr + 8) {
        std::cout << "Upper bound of 35 is at index: " << (upper - arr) << std::endl;
    } else {
        std::cout << "Upper bound of 35 is not found" << std::endl;
    }

    // Using lower_bound
    int* lower = std::lower_bound(arr, arr + 8, 35);
    if (lower != arr + 8) {
        std::cout << "Lower bound of 35 is at index: " << (lower - arr) << std::endl;
    } else {
        std::cout << "Lower bound of 35 is not found" << std::endl;
    }

    return 0;
}
