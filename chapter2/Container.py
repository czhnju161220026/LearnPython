from array import array

'''
'c'	character	1
'b'	signed int	1
'B'	unsigned int	1
'h'	signed int	2
'H'	unsigned int	2
'i'	signed int	2
'I'	unsigned int	2
'l'	signed int	4
'L'	unsigned int	4
'f'	float	4
'd'	double	8
'''
if __name__ == '__main__':
    ints = array('h', (0 for i in range(100)));
    print(ints)
