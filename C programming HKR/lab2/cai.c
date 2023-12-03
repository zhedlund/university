#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int a;
    int b;
    int answer;
    
    srand(time(0));
    a = rand() % 101;
    b = rand() % 101;
    answer = 0;
    while (answer != a + b)
    {
        printf("How much is the sum of %d and %d?: ", a, b);
        scanf("%d", &answer);
            if (answer == a + b)
                printf("Very good!\n");
            else
                printf("No. Please try again.\n");
    }
    return (0);
}