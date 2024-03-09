#include <iostream>
#include <vector>
#include <algorithm>

int square(int number) {
return number * number;
}

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};
std::vector<int> squaredNumbers(numbers.size());

    std::transform(numbers.begin(), numbers.end(), squaredNumbers.begin(), square);

    for (const auto& number : squaredNumbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
