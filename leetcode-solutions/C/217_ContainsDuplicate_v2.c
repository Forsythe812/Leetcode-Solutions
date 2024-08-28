#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *data;
    int size;
} HashSet;

HashSet* createSet(int size) {
    HashSet *set = (HashSet*)malloc(sizeof(HashSet));
    set->data = (int*)calloc(size, sizeof(int));
    for(int i = 0; i < size; i++){
        set->data[i] = -100;
    }
    set->size = size;
    return set;
}

void destroySet(HashSet *set) {
    free(set->data);
    free(set);
}

int hash(int key, int size) {
    return (key % size + size) % size;
}

bool add(HashSet *set, int value) {
    int idx = hash(value, set->size);
    while (set->data[idx] != -100) {
        if (set->data[idx] == value) {
            return true; // Duplicate found
        }
        idx = (idx + 1) % set->size;
    }
    set->data[idx] = value;
    return false;
}

bool containsDuplicate(int* nums, int numsSize) {
    HashSet* set_arr = createSet(numsSize*2);
    bool status = false;

    for(int i = 0; i < numsSize; i++){
        if(add(set_arr, nums[i])){
            status = true;
            break;
        }
    }
    destroySet(set_arr);
    return status;

}