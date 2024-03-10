'''Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:

Input:
s1 = "0033"
s2 = "2"
Output:
66

Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253

'''



//User function Template for javascript

/**
 * @param {string} s1
 * @param {string} s2
 * @returns {string}
 */

class Solution {
    multiplyStrings(s1,s2){ 
      s1= BigInt(s1);
      s2=BigInt(s2);
      let str = s1*s2;
      str = str.toString();
      return str;
      
    }
}