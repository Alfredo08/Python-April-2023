/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

const str2 = "hello";
const expected2 = "hello";

const str3 = "   This  is a   test  ";
const expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrderSplit(wordsStr = "") {
    // if all spaces
    if (wordsStr == false) {
      return wordsStr;
    }
  
    const words = wordsStr.split(" ");
    let reversedWordOrder = "";
  
    // loop backwards
    for (let i = words.length - 1; i >= 0; --i) {
      // Skip empty strings resulting from .split encountering multiple spaces.
      if (words[i] === "") {
        continue;
      }
  
      if (reversedWordOrder.length > 0) {
        reversedWordOrder += " ";
      }
  
      reversedWordOrder += words[i];
    }
    return reversedWordOrder;
  }