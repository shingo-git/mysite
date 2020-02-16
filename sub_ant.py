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

    if x >= w-1:
        x = 1
    elif x <= 0:
        x = w-1

    if y >= h-1:
        y = 1
    elif y <= 0:
        y = h-1

    x = x + dx
    y = y + dy

    return board,x, y, dx, dy, color
