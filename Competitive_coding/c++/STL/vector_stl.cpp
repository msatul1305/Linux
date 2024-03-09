    #include <iostream>
    #include <vector>

    int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
        // Accessing elements
        std::cout << "First element: " << numbers[0] << std::endl;
        std::cout << "Size: " << numbers.size() << std::endl;
    
        // Modifying elements
        numbers.push_back(6);
        numbers[2] = 10;
    
        // Iterating over elements
        for (const auto& number : numbers) {
            std::cout << number << " ";
        }
        std::cout << std::endl;
    
        return 0;
    }
