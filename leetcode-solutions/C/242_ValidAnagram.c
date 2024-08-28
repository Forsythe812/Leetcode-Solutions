#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

bool isAnagram(const char* s, const char* t) {
    int countS[26] = {0};
    int countT[26] = {0};

    for (int i = 0; s[i] != '\0'; i++){
        if (isalpha(s[i])){
            char lowerChar = tolower(s[i]);
            countS[lowerChar - 'a']++;
        }
    }

    for (int i = 0; t[i] != '\0'; i++){
        if (isalpha(t[i])){
            char lowerChar = tolower(t[i]);
            countT[lowerChar - 'a']++;
        }
    }

    // printf("Letter -> Occurrence\n");
    // printf("String S\n");
    // for (int i = 0; i < 26; i++) {
    //     if (countT[i] > 0) {
    //         printf("%c -> %d\n", 'a' + i, countT[i]);
    //     }
    // }
    // printf("\nString T\n");
    // for (int i = 0; i < 26; i++) {
    //     if (countS[i] > 0) {
    //         printf("%c -> %d\n", 'a' + i, countS[i]);
    //     }
    // }

    for (int i = 0; i < 26; i++){
        if (countS[i] != countT[i]){
            return false;
        }
    }

    return true;
}

int main() {
    const char *s = "Anagram";
    const char *t = "gramAnaaa";
    if (isAnagram(s,t)){
        printf("String S and T is an anagram\n");
    } else {
        printf("String S and T is NOT an anagram\n");
    }
    return 0;
}