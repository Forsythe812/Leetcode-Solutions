#include <stdlib.h>
#include <stdbool.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

bool is_anagram (const char *str1, const char *str2) {
    if (strlen(str1) != strlen(str2)){
        return false;
    }

    int alphabet[26] = {0};

    for (int i = 0; str1[i] != '\0'; i++) {
        alphabet[str1[i] - 'a']++;
        alphabet[str2[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++) {
        if (alphabet[i] != 0) {
            return false;
        }
    }

    return true;

}

char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    if (strs == NULL) {
        *returnSize = 0;
        return NULL;
    }

    

}