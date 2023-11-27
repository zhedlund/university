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

void	do_test(int operation) 
{
    int i, num1, num2, answer, user_answer, correct = 0;

    for (i = 0; i < 15; i++) 
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

/*
void	do_test(int operation) 
{
    int i, num1, num2, answer, user_answer
    int correct = 0;

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
*/