#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int	generate_random_number(int min, int max) 
{
    return (rand() % (max - min + 1) + min);
}

void	do_practice(int operation) 
{
    int i, num1, num2, answer, user_answer;
	int	correct = 0;

    for (i = 0; i < 10; i++)
	{
        num1 = generate_random_number(0, 100);
        num2 = generate_random_number(0, 100);

        if (operation == 1) 
		{
            printf("%d. %d + %d = ", i + 1, num1, num2);
            answer = num1 + num2;
        }
		else if (operation == 2)
		{
            printf("%d. %d - %d = ", i + 1, num1, num2);
            answer = num1 - num2;
        } 
		else 
		{
            if (rand() % 2 == 0) 
			{
                printf("%d. %d + %d = ", i + 1, num1, num2);
                answer = num1 + num2;
            } 
			else 
			{
                printf("%d. %d - %d = ", i + 1, num1, num2);
                answer = num1 - num2;
            }
		}
        scanf("%d", &user_answer);
        while (user_answer != answer) 
		{
            printf("No. Please try again. Enter your answer: ");
            scanf("%d", &user_answer);
        }
        printf("Very good!\n");
        correct++;
    }
    printf("Practice completed. You got %d out of 10 correct.\n", correct);
}

// Function to conduct a test
void	do_test(int operation) 
{
    int i, num1, num2, answer, user_answer, correct = 0;

    for (i = 0; i < 15; i++) 
	{
        num1 = generate_random_number(0, 100);
        num2 = generate_random_number(0, 100);
        if (operation == 1) 
            answer = num1 + num2;
		else if (operation == 2) 
            answer = num1 - num2;
		else 
		{
            if (rand() % 2 == 0) 
                answer = num1 + num2;
			else 
                answer = num1 - num2;
        }
        printf("%d. ", i + 1);
        if (operation == 1)
            printf("%d + %d = ", num1, num2);
		else if (operation == 2) 
		    printf("%d - %d = ", num1, num2);
		else 
		{
            if (answer == num1 + num2) 
                printf("%d + %d = ", num1, num2);
			else
                printf("%d - %d = ", num1, num2);
        }
        scanf("%d", &user_answer);
        if (user_answer == answer)
		{
            printf("Very good!\n");
            correct++;
        } 
		else
            printf("Wrong answer.\n");
    }
    printf("Test completed. Your score is: %.2f%%\n", (float)(correct * 100) / 15);
}

int main() {
    srand(time(NULL));

    char name[50];
    int choice, operation;

    printf("Enter your name: ");
    scanf("%s", name);
    printf("Welcome, %s!\n", name);
    do 
	{
        printf("You can choose:\n");
        printf("1. do practices\n");
        printf("2. complete a test\n");
        printf("3. quit the program\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) 
		{
            case 1:
                printf("Now, you can choose to do practices on:\n");
                printf("1. addition\n");
                printf("2. subtraction\n");
                printf("3. addition and subtraction\n");
                printf("Enter your choice: ");
                scanf("%d", &operation);

                if (operation < 1 || operation > 3) 
				{
                    printf("Invalid choice.\n");
                    break;
                }
                do_practice(operation);
                break;
            case 2:
                printf("Now, you can choose to do a test on:\n");
                printf("1. addition\n");
                printf("2. subtraction\n");
                printf("3. addition and subtraction\n");
                printf("Enter your choice: ");
                scanf("%d", &operation);

                if (operation < 1 || operation > 3)
				{
                    printf("Invalid choice.\n");
                    break;
                }
                do_test(operation);
                break;
            case 3:
                printf("Exiting the program. Goodbye, %s!\n", name);
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    } 
	while (choice != 3);
    return (0);
}
