#include <iostream>
#include <vector>
#include <algorithm>

void printNumber(int number) {
std::cout << number << " ";
}

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};

    std::for_each(numbers.begin(), numbers.end(), printNumber);

    return 0;
}
