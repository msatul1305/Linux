#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> source = {1, 2, 3, 4, 5};
    std::vector<int> destination(source.size());

    std::copy(source.begin(), source.end(), destination.begin());

    for (const auto& number : destination) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
