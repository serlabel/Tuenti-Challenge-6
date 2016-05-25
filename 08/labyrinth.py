#!/usr/bin/env python3

import telnetlib

def save_labyrinth(lab):
    ''' Save the labyrinth in file '''
    with open('labyrinth.txt', 'w') as fout:
        for row in lab:
            for elem in row:
                fout.write(elem)
            fout.write('\n')

def update_maze(maze, lab, posx, posy):
    ''' Update the maze '''
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            maze[posx+i][posy+j] = lab[i][j]


if __name__ == "__main__":
    tn = telnetlib.Telnet("52.49.91.111", 1986)
    
    # The size was adjusted after getting the labyrinth
    maze = [[' ' for _ in range(90)] for _ in range(90)]
    posx, posy = 40, 40
    # Starting looking up and without movement
    lookat = 'u'
    move = ''
    new_move = False
    while True:
        labyrinth = []
        for _ in range(7):
            line = tn.read_until(b"\n").decode('ascii')
            print(line, end='')
            labyrinth.append(line[:7])
        update_maze(maze, labyrinth, posx, posy)
        save_labyrinth(maze)
        new_move = False
        while not new_move:
            if lookat == 'u':
                if labyrinth[3][4] == ' ':
                    move = 'r'
                    lookat = 'r'
                    new_move = True
                elif labyrinth[2][3] == '#':
                    lookat = 'l'
                elif labyrinth[3][4] == '#':
                    move = 'u'
                    new_move = True
            elif lookat == 'd':
                if labyrinth[3][2] == ' ':
                    move = 'l'
                    lookat = 'l'
                    new_move = True
                elif labyrinth[4][3] == '#':
                    lookat = 'r'
                elif labyrinth[3][2] == '#':
                    move = 'd'
                    new_move = True
            elif lookat == 'l':
                if labyrinth[2][3] == ' ':
                    move = 'u'
                    lookat = 'u'
                    new_move = True
                elif labyrinth[3][2] == '#':
                    lookat = 'd'
                elif labyrinth[2][3] == '#':
                    move = 'l'
                    new_move = True
            elif lookat == 'r':
                if labyrinth[4][3] == ' ':
                    move = 'd'
                    lookat = 'd'
                    new_move = True
                elif labyrinth[3][4] == '#':
                    lookat = 'u'
                elif labyrinth[4][3] == '#':
                    move = 'r'
                    new_move = True
        tn.write(move.encode('ascii')+b"\n")
        if move == 'u':
            posx -= 1
        if move == 'd':
            posx += 1
        if move == 'l':
            posy -= 1
        if move == 'r':
            posy += 1
    tn.read_all()

