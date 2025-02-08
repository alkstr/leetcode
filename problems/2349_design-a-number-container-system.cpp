// 2349. Design a Number Container System
//
// Design a number container system that can do the following:
// - Insert or Replace a number at the given index in the system.
// - Return the smallest index for the given number in the system.
// Implement the NumberContainers class:
// - NumberContainers() Initializes the number container system.
// - void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
// - int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

#include <unordered_map>
#include <vector>
#include <set>

class NumberContainers
{
public:
  NumberContainers()
  {
    numbers_indexes = std::unordered_map<int, std::set<int>>{};
    indexes_number = std::unordered_map<int, int>{};
  }

  void change(int index, int number)
  {
    if (indexes_number.count(index))
    {
      int prev_number = indexes_number[index];
      if (numbers_indexes[prev_number].size() == 1)
      {
        numbers_indexes.erase(prev_number);
      }
      else
      {
        numbers_indexes[prev_number].erase(index);
      }
    }

    indexes_number[index] = number;
    if (!numbers_indexes.count(number))
    {
      numbers_indexes[number] = std::set<int>();
    }
    numbers_indexes[number].insert(index);
  }

  int find(int number)
  {
    if (numbers_indexes.count(number))
    {
      return *numbers_indexes[number].begin();
    }
    return -1;
  }

private:
  std::unordered_map<int, std::set<int>> numbers_indexes;
  std::unordered_map<int, int> indexes_number;
};