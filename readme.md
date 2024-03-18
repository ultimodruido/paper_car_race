# Paper Car Race

Electronic version of an old car race game I used to play on paper as a kid :)

## Features planned for version 1.0

- Read track from CSV files -> each field describes a cell
- Each cell should contain either *G* (grass), *T* (Track), *S* (Start), *F* (Finish)
- Text interface (gui planned in a future release)
- Up to 5 players

## Example of a race



### Mini track representation

| G | G | G | G | G |
|---|---|---|---|---|
| S | T | T | T | G |
| S | T | T | T | F |
| G | G | T | T | F | 
| G | G | G | G | G | 

### Players select start position

| G | G | G | G | G |
|---|---|---|---|---|
| 1 | T | T | T | G |
| 2 | T | T | T | F |
| G | G | T | T | F | 
| G | G | G | G | G | 

### First moves

Player start moving to an adjacent cell

| G | G | G | G | G |
|---|---|---|---|---|
| S | 1(T) | T | T | G |
| S | 2(T) | T | T | F |
| G | G | T | T | F | 
| G | G | G | G | G | 

### Next moves

Player 1 would move to X and can eventually chose to correct direction/speed going to a cell with ?
Moves are based on previous positions to the near cells

| G | G | G | G | G |
|---|---|---|---|---|
| S | 1(T) | X(T) | ?(T) | G |
| S | 2(T) | ?(T) | ?(T) | F |
| G | G | T | T | F | 
| G | G | G | G | G | 

Player 2 has a similar choice but has to avoid already occupied cell 

| G | G | G | G | G |
|---|---|---|---|---|
| S | ?(T) | ?(T) | ?(T) | G |
| S | 2(T) | X(T) | 1(T) | F |
| G | G | ?(T) | ?(T) | F | 
| G | G | G | G | G | 

To win, Player 1 has to land exactly on a F cell

| G | G | G | G    | G    |
|---|---|---|------|------|
| S | T | T | T    | G    |
| S | T | T | 1(T) | ?(F) |
| G | G | T | 2(T)    | ?(F) | 
| G | G | G | G    | G    | 

Win!

| G | G | G | G | G    |
|---|---|---|---|------|
| S | T | T | T | G    |
| S | T | T | T | 1(F) |
| G | G | T | 2(T) | F    | 
| G | G | G | G | G    | 
