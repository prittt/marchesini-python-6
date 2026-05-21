def read_gruppi(filename: str) -> list[int] | None:
    res = []
    try:
        with open(filename) as f:
            s = None
            for line in f:
                if line == '\n':
                    res.append(s)
                    s = None
                else:
                    s = (s or 0) + int(line)
            if s is not None:
                res.append(s)
            return res
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    print(read_gruppi('file0.txt'))
    print('-' * 50)
    print(read_gruppi('file1.txt'))
    print('-' * 50)
    print(read_gruppi('file2.txt'))
    print('-' * 50)
    print(read_gruppi('file3.txt'))
    print('-' * 50)
