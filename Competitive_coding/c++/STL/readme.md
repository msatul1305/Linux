1. STL:
    - Standard Template Library (STL) 
    - collection of ainer classes, algorithms, and iterators to manipulate and process data efficiently.
      - ainers:
        - ***std::vector***: A dynamic array that can be resized and allows efficient random access. 
        - ***std::list***: A doubly-linked list that allows efficient insertion and deletion at any position. 
        - ***std::deque***: A double-ended queue that allows efficient insertion and deletion at both ends. 
        - ***std::set*** and 
          - ***std::multiset***: ainers that store elements in a sorted order, with unique or duplicate values respectively. 
        - ***std::map*** 
          - and ***std::multimap***: Associative ainers that store key-value pairs, with unique or duplicate keys respectively. 
            - ***std::unordered_set***, 
            - ***std::unordered_multiset***, 
            - ***std::unordered_map***, and 
            - ***std::unordered_multimap***: ainers that provide fast access to elements using hash-based data structures.
            - ***std::stack***: Provides a stack (Last-In-First-Out) behavior on top of a sequence ainer. 
              - ***Uses std::deque*** by default. 
            - ***std::queue***: Provides a queue (First-In-First-Out) behavior on top of a sequence ainer. 
              - Uses ***std::deque*** by default. 
            - ***std::priority_queue***: Provides a priority queue behavior based on a comparator function. 
              - Uses ***std::vector*** by default.
      - Algorithms:
        - ***Sorting***: std::sort, std::stable_sort, std::partial_sort, etc. 
        - ***Searching***: std::find, std::binary_search, std::lower_bound, std::upper_bound, etc. 
        - ***Modifying sequences***: std::copy, std::fill, std::transform, etc. 
        - ***Numeric operations***: std::accumulate, std::inner_product, std::partial_sum, etc. 
      - Iterators:
        - used to traverse the elements of a ainer. 
        - provide a uniform interface to access elements, regardless of the underlying ainer type.
        - Some commonly used iterators include:
          - Input iterators: Used to read values from a ainer sequentially. 
          - Output iterators: Used to write values to a ainer sequentially. 
          - Forward iterators: Supports both reading and writing of values in a forward direction. 
          - Bidirectional iterators: Supports reading and writing in both forward and backward directions. 
          - Random access iterators: Supports all operations of a bidirectional iterator and allows random access to elements using arithmetic operations.

2. ainers with examples:
   - ***std::vector***:
   ```
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
   ```
   - ***std::list***:
   ```
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
   ```
   - ***std::deque***:
   ```
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
   ```
   - ***std::set***:
    ```  
    #include <iostream>
    #include <set>
    int main() {
      std::set<int> numbers = {5, 3, 1, 4, 2};
        
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
    ```

    - ***std::multiset***:
   ```
      #include <iostream>
      #include <set>
    
    int main() {
    std::multiset<int> numbers = {5, 3, 1, 4, 2};
    
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
    ```

    - ***std::map***:
   ```
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
    ```
    - ***std::multimap***:
   ```
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
    ```
    - ***std::unordered_set***:
    ```
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
    ```
    - ***std::unordered_multiset***:
   ```
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
    ```



3. Overview of some commonly used algorithms in the STL:
    - Non-modifying sequence operations:
      - ***std::all_of***: Checks if a condition is true for all elements in a range. 
      - ***std::any_of***: Checks if a condition is true for any element in a range. 
      - ***std::none_of***: Checks if a condition is false for all elements in a range. 
      - ***std::count***: Counts the occurrences of a value in a range. 
      - ***std::count_if***: Counts the elements in a range that satisfy a given condition. 
      - ***std::find***: Finds the first occurrence of a value in a range. 
      - ***std::find_if***: Finds the first element in a range that satisfies a given condition. 
      - ***std::find_if_not***: Finds the first element in a range that does not satisfy a given condition. 
      - ***std::equal***: Checks if two ranges are equal. 
      - ***std::search***: Searches for the first occurrence of a sequence within another range. 
    - Modifying sequence operations:
      - ***std::copy***: Copies elements from a source range to a destination range. 
      - ***std::copy_if***: Copies elements from a source range to a destination range based on a given condition. 
      - ***std::transform***: Applies a function to each element in a range and stores the result in another range. 
      - ***std::fill***: Sets all elements in a range to a particular value. 
      - ***std::fill_n***: Sets a specific number of elements in a range to a particular value. 
      - ***std::generate***: Generates values for each element in a range using a generator function. 
      - ***std::replace***: Replaces all occurrences of a value in a range with another value. 
      - ***std::replace_if***: Replaces elements in a range that satisfy a given condition with a specified value. 
      - ***std::remove***: Removes all occurrences of a value from a range. 
      - ***std::remove_if***: Removes elements from a range that satisfy a given condition. 
      - ***std::unique***: Removes consecutive duplicate elements from a range. 
   - Sorting and related operations:
     - ***std::sort***: Sorts elements in a range in ascending order. 
     - ***std::stable_sort***: Sorts elements in a range in ascending order while preserving the relative order of equal elements. 
     - ***std::partial_sort***: Partially sorts elements in a range, placing the smallest elements in a specified subrange. 
     - ***std::is_sorted***: Checks if elements in a range are sorted in ascending order. 
     - ***std::binary_search***: Checks if a value exists in a sorted range using binary search. 
     - ***std::lower_bound***: Finds the lower bound position of a value in a sorted range. 
     - ***std::upper_bound***: Finds the upper bound position of a value in a sorted range. 
     - ***std::merge***: Merges two sorted ranges into a single sorted range. 
     - ***std::inplace_merge***: Merges two consecutive sorted ranges in place. 
   - Numeric algorithms:
     - ***std::accumulate***: Computes the sum of elements in a range. 
     - ***std::inner_product***: Computes the inner product of two ranges. 
     - ***std::partial_sum***: Computes the partial sums of elements in a range. 
     - ***std::iota***: Assigns consecutive values to elements in a range. 
   - Heap operations:
     - ***std::make_heap***: Creates a heap from a range of elements. 
     - ***std::push_heap***: Adds an element to a heap. 
     - ***std::pop_heap***: Removes the largest element from a heap and places it at the end of the range. 
     - ***std::sort_heap***: Converts a heap into a sorted range. 
   - Set operations:
     - ***std::set_union***: Computes the union of two sorted ranges. 
     - ***std::set_intersection***: Computes the intersection of two sorted ranges. 
     - ***std::set_difference***: Computes the difference between two sorted ranges. 
     - ***std::set_symmetric_difference***: Computes the symmetric difference of two sorted ranges. 
   - Min/max operations:
     - ***std::min_element***: Finds the smallest element in a range. 
     - ***std::max_element***: Finds the largest element in a range. 
     - ***std::minmax_element***: Finds both the smallest and largest elements in a range. 
   - Other useful algorithms:
     - ***std::reverse***: Reverses the order of elements in a range. 
     - ***std::rotate***: Rotates the order of elements in a range. 
     - ***std::next_permutation***: Generates the next lexicographically greater permutation of a range. 
     - ***std::prev_permutation***: Generates the next lexicographically smaller permutation of a range. 
     - ***std::random_shuffle***: Randomly shuffles the elements in a range.


Examples of each algorithm:
    - explanation of each algorithm in the STL along with an example of how to use it:

std::for_each:
Description: Applies a function to each element in a range.
```
#include <iostream>
#include <vector>
#include <algorithm>

void printNumber(int number) {
std::cout << number << " ";
}

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};

    std::for_each(numbers.begin(), numbers.end(), printNumber);

    return 0;
}
```
std::find:
Description: Finds the first occurrence of a value in a range.
```
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
```
std::count:
Description: Counts the occurrences of a value in a range.
```
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5, 3};

    int count = std::count(numbers.begin(), numbers.end(), 3);
    std::cout << "Count: " << count << std::endl;

    return 0;
}
```
std::sort:
Description: Sorts the elements in a range.
```
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
std::vector<int> numbers = {5, 3, 1, 4, 2};

    std::sort(numbers.begin(), numbers.end());

    for (const auto& number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
std::transform:
Description: Applies a function to each element in a range and stores the result in another range.
```
#include <iostream>
#include <vector>
#include <algorithm>

int square(int number) {
return number * number;
}

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};
std::vector<int> squaredNumbers(numbers.size());

    std::transform(numbers.begin(), numbers.end(), squaredNumbers.begin(), square);

    for (const auto& number : squaredNumbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
std::accumulate:
Description: Computes the sum of elements in a range.
```
#include <iostream>
#include <vector>
#include <numeric>

int main() {
std::vector<int> numbers = {1, 2, 3, 4, 5};
int sum = std::accumulate(numbers.begin(), numbers.end(), 0);
std::cout << "Sum: " << sum << std::endl;

return 0;
}
```
7. `std::copy`:
- Description: Copies elements from one range to another.
  ```
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
  ```
8. `std::reverse`:
- Description: Reverses the order of elements in a range.
  ```
  #include <iostream>
  #include <vector>
  #include <algorithm>

  int main() {
      std::vector<int> numbers = {1, 2, 3, 4, 5};

      std::reverse(numbers.begin(), numbers.end());

      for (const auto& number : numbers) {
          std::cout << number << " ";
      }
      std::cout << std::endl;

      return 0;
  }
  ```
9. `std::unique`:
- Description: Removes consecutive duplicate elements in a range.
- 
  ```
  #include <iostream>
  #include <vector>
  #include <algorithm>

  int main() {
      std::vector<int> numbers = {1, 2, 2, 3, 3, 4, 5, 5, 5};

      auto it = std::unique(numbers.begin(), numbers.end());
      numbers.erase(it, numbers.end());

      for (const auto& number : numbers) {
          std::cout << number << " ";
      }
      std::cout << std::endl;

      return 0;
  }
  ```
std::binary_search:
Description: Checks if a specific value exists in a sorted range.
```
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
```
