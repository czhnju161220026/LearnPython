
if __name__ == '__main__':
    colors = ['black', 'white', 'gray']
    size = ['S', 'M', 'L', 'XL']
    for (color, s) in ((color, s) for color in colors for s in size):
        print(color,s)
