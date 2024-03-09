#include <iostream>
#include <map>

int main() {
std::multimap<std::string, int> ages;
ages.insert(std::make_pair("Alice", 25));
ages.insert(std::make_pair("Bob", 30));
ages.insert(std::make_pair("Alice", 35));

    // Accessing elements
    std::cout << "Alice's ages: ";
    auto range = ages.equal_range("Alice");
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->second << " ";
    }
    std::cout << std::endl;

    // Iterating over elements
    for (const auto& entry : ages) {
        std::cout << entry.first << ": " << entry.second << std::endl;
    }

    return 0;
}
