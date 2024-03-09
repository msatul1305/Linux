    #include <iostream>
    #include <deque>

    int main() {
    std::deque<int> numbers = {1, 2, 3, 4, 5};
    
        // Insertion and deletion
        numbers.push_front(0);
        numbers.push_back(6);
        numbers.pop_front();
        numbers.pop_back();
    
        // Iterating over elements
        for (const auto& number : numbers) {
            std::cout << number << " ";
        }
        std::cout << std::endl;
    
        return 0;
    }
