# Python String Interpolation
String interpolation in Python is a method of embedding variables or expressions within string literals to create dynamic and formatted strings. It allows for the seamless integration of variable values and expressions into a string, enhancing readability and efficiency in code.

### 4 Methods for String Interpolation in Python

1. .format()
2. modulo %
3. f-string
4. Template class

## Using String Format Indicators
String formatting with the modulo operator includes the % character and a format indicator for each of the entries in the string template. A format indicator converts a provided value into the type indicated by the format indicator. The conversion is done before the value is inserted into the string. Python provides the following format indicators:

- %s: String (performed using the str() function)
- %d: Integer
- %f: Floating point
- %e: Lowercase exponent
- %E: Uppercase exponent
- %x: Lowercase hexadecimal
- %X: Uppercase hexadecimal
- %o: Octal
- %r: Raw (performed using the repr() function)
- %g: Floating point for smaller numbers, lowercase exponent for larger numbers
- %G: Floating point for smaller numbers, uppercase exponent for larger numbers
- %a: ASCII (performed using the ascii() function)
- %c: Converts an int or a char to a character, such as 65 to the letter A<br/>

**Example 1**
``` python
x = 'looked'
print("Misha %s and %s around"%('walked',x))
```
**Output**
> Misha walked and looked around
 
 **Example 2**
 ```python
 print('The value of pi is: %5.4f' %(3.141592))
 ```
**Output**
>The value of pi is: 3.1416


### Conclusion
 String interpolation in Python is a powerful method for creating dynamic and formatted strings by embedding variables or expressions within string literals. It significantly enhances code readability and efficiency. Using the modulo operator for string formatting involves the % character along with specific format indicators, which convert and insert values into the string according to their types. This method offers various format indicators such as %s for strings, %d for integers, %f for floating-point numbers, and many others for different data types and representations. Understanding and utilizing these format indicators allows for precise control over string formatting, making the code more flexible and expressive.