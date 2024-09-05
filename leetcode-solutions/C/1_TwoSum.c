/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <stdbool.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    if (nums == NULL) {
        return NULL;
    }

    if(numsSize<2 || numsSize>10000) return NULL;
    if(target<-1000000000 || target>1000000000) return NULL;

    for (int i = 0; i < (numsSize-1) ; i++) {

        if(nums[i]<-1000000000 || nums[i]>1000000000) return NULL;

        for (int j = i+1; j < numsSize; j++){
            if (target - nums[i] == nums[j]){
                int *result = (int*) malloc(2*sizeof(int));
                result[0] = i;
                result[1] = j;

                *returnSize = 2;

                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}