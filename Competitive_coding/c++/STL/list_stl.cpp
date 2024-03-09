     #include <iostream>
     #include <list>

    int main() {
    std::list<int> numbers = {1, 2, 3, 4, 5};
    
        // Insertion and deletion
        numbers.push_front(0);
        numbers.insert(std::next(numbers.begin(), 3), 6);
        numbers.pop_back();
    
        // Iterating over elements
        for (const auto& number : numbers) {
            std::cout << number << " ";
        }
        std::cout << std::endl;
    
        return 0;
    }
