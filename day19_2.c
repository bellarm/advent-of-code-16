#include <stdio.h>
#include <stdlib.h>

void removeElf(int* pos, int elfToRemove, int elvesInCircle) {
    int i = elfToRemove;
    for (int j = elfToRemove+1; j < elvesInCircle; j++) {
        pos[i++] = pos[j];
    }
}

int main(int argc, char const *argv[]) {
    int num = 3001330;
    int *elves = malloc(sizeof(int)*num);
    printf("hello\n");
    int i;
    for (i = 0; i < num; i++){
        elves[i] = 1;
    }
    int *pos = malloc(sizeof(int)*num);
    int elvesInCircle = num;
    for (i = 0; i < num; i++) {
        pos[i] = i;
    }
    int indexCur = 0;
    int indexNext;
    while (elvesInCircle > 2) {
        indexNext = (indexCur + elvesInCircle/2) % elvesInCircle;
        elves[pos[indexCur]] += elves[pos[indexNext]];
        elves[pos[indexNext]] = 0;
        removeElf(pos, indexNext, elvesInCircle);
        if (indexNext < indexCur) {
            indexCur--;
        }
        elvesInCircle--;
        indexCur = (indexCur + 1) % (elvesInCircle);
    }
    printf("%d\n", pos[0]+1);
    return EXIT_SUCCESS;
}