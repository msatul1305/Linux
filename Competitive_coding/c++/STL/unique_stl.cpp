#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> numbers = {1, 2, 2, 3, 3, 4, 5, 5, 5};

    auto it = std::unique(numbers.begin(), numbers.end());
    numbers.erase(it, numbers.end());

    for (const auto& number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
