def read_cities(filename: str) -> list[tuple[str, int]] | None:
    res = []
    try:
        with open(filename, 'rb') as f:
            # Read the number of cities
            b = f.read(4)
            if len(b) != 4:
                return None
            n = int.from_bytes(b, byteorder='little')
            for i in range(n):
                # Read the city name
                bnome = bytearray()
                while True:
                    b = f.read(1)
                    if len(b) != 1:
                        # Error: file ended before completing the city
                        return None
                    if b == b'\x00':
                        # End of name
                        break
                    bnome += b
                name = bnome.decode()
                # Read the population
                b = f.read(4)
                if len(b) != 4:
                    return None
                population = int.from_bytes(b, byteorder='little')
                res.append((name, population))
            return res
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    print(read_cities('cities00.bin'))
    print('-' * 50)
    print(read_cities('cities01.bin'))
    print('-' * 50)
    print(read_cities('cities02.bin'))
    print('-' * 50)
    print(read_cities('cities03.bin'))
    print('-' * 50)
    print(read_cities('cities04.bin'))
    print('-' * 50)
