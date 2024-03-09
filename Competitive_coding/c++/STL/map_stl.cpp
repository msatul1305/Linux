#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> ages;
    ages["Alice"] = 25;
    ages["Bob"] = 30;
    ages["Charlie"] = 35;

    // Insertion
    ages.insert(std::make_pair("Dave", 40));

    // Accessing elements
    std::cout << "Bob's age: " << ages["Bob"] << std::endl;

    // Iterating over elements
    for (const auto& entry : ages) {
        std::cout << entry.first << ": " << entry.second << std::endl;
    }

    return 0;
}
