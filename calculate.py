import circle
import square
import rectangle
import triangle

FIGS = ['circle', 'square', 'triangle', 'rectangle']
FUNCS = ['perimeter', 'area']
SIZES = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
    'perimeter-rectangle': 2,
    'area-rectangle': 2,
    'perimeter-triangle': 3,
    'area-triangle': 3,
}


def calc(fig, func, size):
    if any(isinstance(s, str) for s in size):
        return
    elif all(s > 0 for s in size):
        assert fig in FIGS
        assert func in FUNCS

        result = eval(f'{fig}.{func}(*{size})')
        return result
    else:
        print("Sizes must be positive integers\n")
        return


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in FIGS:
        fig = input(f"Enter figure name, available are {FIGS}:\n")

    while func not in FUNCS:
        func = input(f"Enter function name, available are {FUNCS}:\n")

    while len(size) != SIZES.get(f"{func}-{fig}", 1):
        try:
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space," 
                        " 1 for circle and square\n"
                    ).split()
                )
            )
        except ValueError:
            print("Invalid input. Please enter integers only.")

    result = calc(fig, func, size)
    print(result)
