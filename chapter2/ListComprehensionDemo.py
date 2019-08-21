
if __name__ == '__main__':
    colors = ['black', 'white', 'gray']
    size = ['S', 'M', 'L', 'XL']
    print([(color, s) for color in colors for s in size])
    print([(color, s) for s in size for color in colors])
