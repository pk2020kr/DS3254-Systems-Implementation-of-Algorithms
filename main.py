# for Mac system information
!system_profiler SPHardwareDataType;
'''
Hardware:

    Hardware Overview:

      Model Name: MacBook Air
      Model Identifier: Mac14,2
      Model Number: MLXW3HN/A
      Chip: Apple M2
      Total Number of Cores: 8 (4 performance and 4 efficiency)
      Memory: 8 GB
      System Firmware Version: 11881.61.3
      OS Loader Version: 11881.61.3
      Serial Number (system): D4QJ14DNJF
      Hardware UUID: FB39C139-85B4-51E1-9B4D-57867ED5A68A
      Provisioning UDID: 00008112-000838E02EA3401E
      Activation Lock Status: Disabled
'''

'''
Choosing the Right Laptop or PC: A Detailed Guide
Determine Your Primary Use Case:
    
Gaming
  Graphics Card: High-performance dedicated GPU (e.g., NVIDIA GeForce RTX or AMD Radeon RX)
  Processor: Fast multi-core CPU (e.g., Intel i7/i9 or AMD Ryzen 7/9)
  RAM: Minimum 16 GB
  Storage: SSD with at least 512 GB capacity and additional HDD for extra storage
  Display: High refresh rate display (120 Hz or higher) with Full HD or 4K resolution

Graphic Design
  Graphics Card: Dedicated GPU (e.g., NVIDIA GTX or AMD Radeon RX) 
  Processor: Multi-core CPU (e.g., Intel i5/i7 or AMD Ryzen 5/7)
  RAM: Minimum 16 GB
  Storage: SSD with at least 512 GB capacity
  Display: High-resolution display with accurate color reproduction (e.g., 4K display and high Adobe RGB coverage)

Video Editing
  Graphics Card: Powerful dedicated GPU (e.g., NVIDIA GeForce RTX or AMD Radeon Pro)
  Processor: High-speed, multi-core CPU (e.g., Intel i7/i9 or AMD Ryzen 7/9)
  RAM: Minimum 32 GB
  Storage: Fast SSD with at least 1 TB capacity
  Display: High-resolution monitor with good color accuracy (4K display preferred)

Physics Simulation
  Graphics Card: High-performance GPU (e.g., NVIDIA Quadro or AMD Radeon Pro)
  Processor: High-end multi-core CPU (e.g., Intel Xeon or AMD Ryzen Threadripper)
  RAM: Minimum 32 GB
  Storage: SSD with at least 1 TB capacity
  Additional: Consider specialized hardware for specific simulation needs (e.g., tensor cores)
'''


def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.
    Args:
        arr: The array to be sorted.
    Returns:
        None. The array is modified in-place.
    """
    for j in range(1, len(arr)):
        key = arr[j]  # Element to be inserted

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = key  # Insert the key into its correct position

# Example usage
my_array = [5, 2, 9, 1, 5, 6]
insertion_sort(my_array)
print(my_array)  # Output: [1, 2, 5, 5, 6, 9]
