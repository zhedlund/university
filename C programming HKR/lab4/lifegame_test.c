#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include "lifegame.h"

/* hard-coded world size */
#define WORLDWIDTH 39
#define WORLDHEIGHT 20

/* character representations of cell states */
#define CHAR_ALIVE '*'
#define CHAR_DEAD ' '

#define WORLDWIDTH 39
#define WORLDHEIGHT 20

/* number of generations to evolve the world */
#define NUM_GENERATIONS 50

/* current cell states of the world */
static int world[WORLDWIDTH][WORLDHEIGHT];

/* next generation cell states */
static int nextstates[WORLDWIDTH][WORLDHEIGHT];

/* functions to write for Task 2 of lab */
void initialize_world_from_file(const char * filename) {
	/* TODO: read the state of the world from a file with
	   name "filename".  the live cells are given by pairs of rows and columns.
	 */
}

void save_world_to_file(const char * filename) {
	/* TODO: write the state of the world into a file with
	   name "filename".
	   only the live cells are saved in the file (in the form of rows and columns).

	   This file should be readable using the function
	   initialize_world_from_file(filename) above
	 */
}

/* functions to implement */

/* this function should set the state of all
   the cells in the next generation and call
   finalize_evolution() to update the current
   state of the world to the next generation */
void next_generation(void);

/* this function should return the state of the cell
   at (x,y) in the next generation, according to the
   rules of Conway's Game of Life (see handout) */
/* Rules of the Game of Life */
int get_next_state(int x, int y);

/* this function should calculate the number of alive
   neighbors of the cell at (x,y) */
int num_neighbors(int x, int y);


void next_generation(void) 
{
	/* for every cell, set the state in the next
	   generation according to the Game of Life rules

	   Hint: use get_next_state(x,y) */
    int i, j;

    for (i = 0; i < WORLDWIDTH; i++) {
        for (j = 0; j < WORLDHEIGHT; j++) {
            int next_state = get_next_state(i, j);
            set_cell_state(i, j, next_state);
        }
    }
	finalize_evolution(); /* called at end to finalize */
}

int get_next_state(int x, int y)
{
    int alive_neighbors = num_neighbors(x, y);

    if (world[x][y] == ALIVE) {
        if (alive_neighbors < 2 || alive_neighbors > 3)
            return DEAD; // Any live cell with fewer than two live neighbors dies, as if by underpopulation. Or, any live cell with more than three live neighbors dies, as if by overpopulation.
        else
            return ALIVE; // Any live cell with two or three live neighbors lives on to the next generation.
    } else {
        if (alive_neighbors == 3)
            return ALIVE; // Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        else
            return DEAD; // All other dead cells remain dead.
    }

}
	/* TODO: for the specified cell, return the number of
	   neighbors that are ALIVE

	   Use get_cell_state(x,y) */

int num_neighbors(int x, int y) {
    int count = 0;
    int i, j;

    for (i = -1; i <= 1; i++) {
        for (j = -1; j <= 1; j++) {
            if (i == 0 && j == 0)
                continue; // Skip the current cell itself

            int neighbor_x = x + i;
            int neighbor_y = y + j;

            if (neighbor_x >= 0 && neighbor_x < WORLDWIDTH && neighbor_y >= 0 && neighbor_y < WORLDHEIGHT) {
                count += get_cell_state(neighbor_x, neighbor_y); // Use get_cell_state to check the state of the neighbor
            }
        }
    }
    return count;
}



/* you shouldn't need to edit anything below this line */

/* initializes the world to a hard-coded pattern, and resets
   all the cells in the next generation to DEAD */
void initialize_world(void) {
	int i, j;

	for (i = 0; i < WORLDWIDTH; i++)
		for (j = 0; j < WORLDHEIGHT; j++)
			world[i][j] = nextstates[i][j] = DEAD;
	/* pattern "glider" */
	world[1][2] = ALIVE;
	world[3][1] = ALIVE;
	world[3][2] = ALIVE;
	world[3][3] = ALIVE;
	world[2][3] = ALIVE;
}

int get_world_width(void) {
	return WORLDWIDTH;
}

int get_world_height(void) {
	return WORLDHEIGHT;
}

int get_cell_state(int x, int y) {
	if (x < 0 || x >= WORLDWIDTH || y < 0 || y >= WORLDHEIGHT)
		return DEAD;
	return world[x][y];
}

void set_cell_state(int x, int y, int state) {
	if (x < 0 || x >= WORLDWIDTH || y < 0 || y >= WORLDHEIGHT) {
		fprintf(stderr,"Error: coordinates (%d,%d) are invalid.\n", x, y);
		abort();
	}
	nextstates[x][y] = state;
}

void finalize_evolution(void) {
	int x, y;
	for (x = 0; x < WORLDWIDTH; x++) {
		for (y = 0; y < WORLDHEIGHT; y++) {
			world[x][y] = nextstates[x][y];
			nextstates[x][y] = DEAD;
		}
	}
}

void output_world(void) {
	char worldstr[2*WORLDWIDTH+2];
	int i, j;

	worldstr[2*WORLDWIDTH+1] = '\0';
	worldstr[0] = '+';
	for (i = 1; i < 2*WORLDWIDTH; i++)
		worldstr[i] = '-';
	worldstr[2*WORLDWIDTH] = '+';
	puts(worldstr);
	for (i = 0; i <= 2*WORLDWIDTH; i+=2)
		worldstr[i] = '|';
	for (i = 0; i < WORLDHEIGHT; i++) {
		for (j = 0; j < WORLDWIDTH; j++)
			worldstr[2*j+1] = world[j][i] == ALIVE ? CHAR_ALIVE : CHAR_DEAD;
		puts(worldstr);
	}
	worldstr[0] = '+';
	for (i = 1; i < 2*WORLDWIDTH; i++)
		worldstr[i] = '-';
	worldstr[2*WORLDWIDTH] = '+';
	puts(worldstr);
}

int main(void)
{
	int n;

	/* TODO: initialize the world by hard-coded function initialize_world() in lifegame.c*/
	initialize_world();
	/* evolutions*/
	for (n = 0; n < NUM_GENERATIONS; n++) {
		next_generation();
		output_world(); // output the world state to console
		printf("Press ENTER to continue...\n");
        getchar(); // program pauses, until you press ENTER key to continue
	}
	return 0;
}