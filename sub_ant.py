def ant_plot(board, w, h, x, y, dx, dy):

    white = (255, 255, 255)
    black = (0, 0, 0)

    if board.iloc[int(x), int(y)] == 0:
        board.iloc[int(x), int(y)] = 1
        temp = dx
        dx = -dy
        dy = temp
        color = black
    else:
        board.iloc[int(x), int(y)] = 0
        temp = dx
        dx = dy
        dy = -temp
        color = white

    x = x + dx
    y = y + dy

    if x == w:
        x = 0
    elif x == -1:
        x = w - 1

    if y == h:
        y = 0
    elif y == -1:
        y = h - 1

    return board,x, y, dx, dy, color
