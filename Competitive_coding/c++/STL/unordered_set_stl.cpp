#include <iostream>
#include <unordered_set>

int main() {
std::unordered_set<int> numbers = {5, 3, 1, 4, 2};

    // Insertion
    numbers.insert(6);
    numbers.insert(0);

    // Iterating over elements
    for (const auto& number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
