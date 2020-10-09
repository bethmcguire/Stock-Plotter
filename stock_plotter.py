# author: Beth McGuire
# class: CSc 110
# description: Emulate the stock market using horizontal and vertical graphs based on user input.
#              Most of the code is commented to further explain what happens.

# ask user for plot orientation. if not vertical or horizontal, while loops until valid
plot_orientation = input('Enter stock plotter mode:\n')
while plot_orientation != 'horizontal' and plot_orientation != 'vertical':
    plot_orientation = input('Enter horizontal or vertical: \n')

# ask user for stock plot string. if not an even # of characters, while loops until valid
plot_string = input('Enter stock plot input string: \n')
while len(plot_string) % 2 != 0:
    plot_string = input(
        "Make sure number of characters are even:\n")

# create a variable to track rows, as well as the outer edges of the graphs
row = 0
edge = '##' + "#" * (len(plot_string)//2) + '##'
edge_2 = '#' * 19

# setup logic for the horizontal graph
if plot_orientation == 'horizontal':
    print(edge)
    while row < 17:
        # represents center of the graph starting point
        d = 8
        # represents the first string character
        i = 0
        # represents the second string character
        i_2 = 1
        # used to determine *, # or ' '
        line = '# '
        while i < len(plot_string):
            if plot_string[i] == 'u':
                # if u, shifts starting point up
                d -= int(plot_string[i_2])
                # determines where to place asterisk
                if row == d:
                    line += '*'
                else:
                    line += ' '
            elif plot_string[i] == 'd':
                # if d, shifts starting point down
                d += int(plot_string[i_2])
                # determines where to places asterisk
                if row == d:
                    line += "*"
                else:
                    line += " "
            # jumps to the next u or d
            i += 2
            # jumps to the next number in plot string
            i_2 += 2
        print(line + ' #')
        # jumps to the next row
        row += 1
    print(edge)
# setup logic for the vertical graph
else:
    print(edge_2)
    # starting index point for u or d
    i = 0
    # starting index point for numbers following u or d
    i_2 = 1
    # starting center point for graph
    d = 9
    while i < len(plot_string):
        # runs logic of matching u in plot string
        if plot_string[i] == 'u':
            # if u for up, adds number to d variable
            d += int(plot_string[i_2])
            # this logic determines where to place asterisk
            print('#' + ' ' * (d - 1) + "*" + ' ' * (17 - d) + '#')
            # logic same as above, except for the down part in the plot_string
        elif plot_string[i] == 'd':
            d -= int(plot_string[i_2])
            print('#' + ' ' * (d - 1) + "*" + ' ' * (17 - d) + '#')
        # adds 2 to the first index as well as the second index
        i += 2
        i_2 += 2
    # prints lower edge
    print(edge_2)
