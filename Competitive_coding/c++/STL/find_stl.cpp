#include <iostream>
#include <vector>
#include <algorithm>

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};

    auto it = std::find(numbers.begin(), numbers.end(), 3);
    if (it != numbers.end()) {
        std::cout << "Found at index: " << std::distance(numbers.begin(), it) << std::endl;
    } else {
        std::cout << "Not found" << std::endl;
    }

    return 0;
}
