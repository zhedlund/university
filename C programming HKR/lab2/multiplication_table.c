#include <stdio.h>

int main(void)
{
    int n;
    int i;
    int j;

    i = 0;
    j = 0;
    printf("Enter the size of the multiplication table (1 to 11): ");
    scanf("%d", &n);
    if (n <= 0 || n > 11)
    {
        printf("Invalid input. Please enter a value between 1 and 11.\n");
        return (1);
    }
    printf("   x |");
    for (i = 1; i <= n; i++)
        printf("%4d", i);
    printf("\n");
    printf("------");
    for (i = 1; i <= n; i++) {
        printf("----");
    }
    printf("\n");
    for (i = 1; i <= n; i++)
    {
        printf("%4d |", i);
        for (j = 1; j <= n; j++)
            printf("%4d", i * j);
        printf("\n");
    }
    return (0);
}