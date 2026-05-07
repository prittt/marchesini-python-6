import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] {elapsed:.6f}s")
        return result
    return wrapper

def other_name():
    pass

if __name__ == "__main__":
    print("questo è il modulo time")