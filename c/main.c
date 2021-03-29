#include <stdio.h>
#include <stdlib.h>

int init_board(char board[3][3]);
int draw_board(char board[3][3]);

int main()
{
    char board[3][3];
    init_board(board);
    draw_board(board);
    return EXIT_SUCCESS;
}

int init_board(char board[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = '-';
        }
        
    }
    return EXIT_SUCCESS;
}

int draw_board(char board[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%c", board[i][j]);
        }
        printf("\n");
    }
    return EXIT_SUCCESS;
}
