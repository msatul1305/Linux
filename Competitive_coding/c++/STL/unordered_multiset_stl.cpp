#include <iostream>
#include <unordered_set>

int main() {
std::unordered_multiset<int> numbers = {5, 3, 1, 4, 2};

    // Insertion
    numbers.insert(2);
    numbers.insert(3);

    // Iterating over elements
    for (const auto& number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
