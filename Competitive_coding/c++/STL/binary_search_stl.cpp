#include <iostream>
#include <vector>
#include <algorithm>

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};

    bool found = std::binary_search(numbers.begin(), numbers.end(), 3);

    if (found) {
        std::cout << "Value found" << std::endl;
    } else {
        std::cout << "Value not found" << std::endl;
    }

    return 0;
}
