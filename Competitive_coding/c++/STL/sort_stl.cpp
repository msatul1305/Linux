#include <iostream>
#include <vector>
#include <algorithm>

int main() {
std::vector<int> numbers = {5, 3, 1, 4, 2};

    std::sort(numbers.begin(), numbers.end());

    for (const auto& number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
