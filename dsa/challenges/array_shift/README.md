## __Shift an Array__
### [Table of Contents](../../../README.md)
See [solution](array_shift.py)



  * Challenge
  Write a function called __insertShiftArray__ which takes in an array and the value to be added. _Without utilizing any of the built-in methods_ available to your language, __return an array__ with the new value added at the __middle index__.

    Write a second function __removeAndShiftArray__ that removes an element from the middle index and shifts other elements in the array to fill the new gap.

     __Approach & Efficiency__
* I approached it by using a for loop to take each element of the array and then place it into a new array until the mid point is reached.  Then using one built in function .append i appended the inserted argument into the new list, and then continued through the loop until the end of the array
* The method using the built in method .insert as comparison is faster and efficient withot requiring a loop or new list being created.

* For the removeAndShiftArray function, I used the for loop again to iterate through the array, and append each element to a second array. When the loop reaches the midpoint, then it passes over the element at that index, and the continues appending the remaining elements. The new list is returned.

* Using the built-in method of .pop() at the mid index point, the middle index number is removed.

 * The first method for the insertShiftArray function is inefficient due to selecting the for loop, which affects __time__ in linear manner, and the __efficiency__ is affected in a exponential manner. This also uses up much __memory__.

    Similarly for the removeAndShiftArray function, it also uses the loop ineffeciently.

  * Specificiations used :     gitignore, editorconfig

  * Solution
![whiteboard](../../assets/array-shift.jpg)
