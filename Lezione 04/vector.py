from typing import Union, List, Tuple, Set, Self, cast

# class VectorIteratorReverse:
#     def __init__(self, sequence):
#         self._sequence = sequence
#         self._index = len(self._sequence) - 1 
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self._index >= 0:
#             item = self._sequence[self._index]
#             self._index -= 1
#             return item
#         else:
#             raise StopIteration


class VectorSortedIterator:
    def __init__(self, vector):
        self._sorted = sorted(vector) 
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sorted):
            item = self._sorted[self._index]
            self._index += 1
            return item
        raise StopIteration


class VectorSortedIteratorLazy:

    def __init__(self, vector):
        self._vector = vector
        self._last = None   
        self._last_count = 0
        self._yielded = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._yielded == len(self._vector):
            raise StopIteration

        skip = self._last_count

        candidate = None
        for i in range(len(self._vector)):
            val = self._vector[i]
            if self._last is not None and val < self._last:
                continue
            if self._last is not None and val == self._last:
                if skip > 0:
                    skip -= 1
                    continue
            
            if candidate is None or val < candidate:
                candidate = val

        if candidate == self._last:
            self._last_count += 1
        else:
            self._last = candidate
            self._last_count = 1

        self._yielded += 1
        return candidate
        

class Vector:    
    def __init__(self, *initializer: Union[int, float, List[Union[int, float]], Tuple[Union[int, float], ...], Set[Union[int, float]]]):
        if len(initializer) == 1 and isinstance(initializer[0], (list, tuple, set)):
            self.__data: List[Union[int, float]] = list(initializer[0])
        elif all(isinstance(x, (int, float)) for x in initializer):
            self.__data: List[Union[int, float]] = cast(List[Union[int, float]], list(initializer))
        else:
            raise TypeError("Expected numbers or a single list/tuple/set of numbers")
        
    # def __init__(self, *initializer):
    #     if len(initializer) == 1 and isinstance(initializer[0], (list, tuple, set)):
    #         self.__data = list(initializer[0])
    #     elif all(isinstance(x, (int, float)) for x in initializer):
    #         self.__data = list(initializer)
    #     else:
    #         raise TypeError("Expected numbers or a single list/tuple/set of numbers")


    def __str__(self) -> str:
        return "{" + f"{self.__data.__str__().replace("[", "").replace("]","")}" + "}"

    def __repr__(self) -> str:
        return f"Vector({self.__data})"

    def __len__(self) -> int:
        return len(self.__data) 

    def __add__(self, other: Union[Self, int, float]) -> "Vector":  
        if isinstance(other, Vector):
            if len(self.__data) != len(other.__data):
                raise ValueError("Vectors must have the same length for addition")
            #return Vector([self.__data[i] + other.__data[i] for i in range(len(self.__data))])
            
            # for i in range(len(self.__data)):
            #     self.__data[i] + other.__data[i] 
            
            # for i, e in enumerate(self.__data):
            #     e + other.__data[i]

            # [e1 + e2 for e1, e2 in zip(self.__data, other.__data)]
                
            return Vector([a + b for a, b in zip(self.__data, other.__data)])
        elif isinstance(other, (int, float)):
            # ret = []
            # for e in self.__data:
            #     ret += [e + other]  
            return Vector([a + other for a in self.__data])
        else:
            return NotImplemented

    def __iadd__(self, other: Self) -> Self:
        result = self + other
        self.__data = result.__data
        return self

    def __radd__(self, other: Union[int, float]) -> "Vector":
        return self + other

    # --- Subtraction ---
    def __sub__(self, other: Union[Self, int, float]) -> "Vector":
        if isinstance(other, Vector):
            if len(self.__data) != len(other.__data):
                raise ValueError("Vectors must have the same length for subtraction")
            return Vector([a - b for a, b in zip(self.__data, other.__data)])
        elif isinstance(other, (int, float)):
            return Vector([a - other for a in self.__data])
        else:
            return NotImplemented

    def __isub__(self, other: Union[Self, int, float]) -> Self:
        result = self - other
        self.__data = result.__data
        return self

    def __rsub__(self, other: Union[int, float]) -> "Vector":
        # s - a  =>  vector where each element = s - a[i]
        return Vector([other - a for a in self.__data])

    # --- Multiplication ---
    def __mul__(self, other: Union[Self, int, float]) -> "Union[Vector, float]":
        if isinstance(other, Vector):
            # dot (inner) product -> scalar
            if len(self.__data) != len(other.__data):
                raise ValueError("Vectors must have the same length for dot product")
            return sum(a * b for a, b in zip(self.__data, other.__data))
        elif isinstance(other, (int, float)):
            return Vector([a * other for a in self.__data])
        else:
            return NotImplemented

    def __imul__(self, other: Union[int, float]) -> Self:
        result = self * other
        self.__data = cast(List[Union[int, float]], result.__data)  # type: ignore[union-attr]
        return self

    def __rmul__(self, other: Union[int, float]) -> "Vector":
        return self * other  # type: ignore[return-value]

    # --- Division ---
    def __truediv__(self, other: Union[int, float]) -> "Vector":
        return Vector([a / other for a in self.__data])

    def __itruediv__(self, other: Union[int, float]) -> Self:
        result = self / other
        self.__data = result.__data
        return self

    def __rtruediv__(self, other: Union[int, float]) -> "Vector":
        # s / a  =>  vector where each element = s / a[i]
        return Vector([other / a for a in self.__data])

    def __floordiv__(self, other: Union[int, float]) -> "Vector":
        return Vector([a // other for a in self.__data])

    def __ifloordiv__(self, other: Union[int, float]) -> Self:
        result = self // other
        self.__data = result.__data
        return self

    def __rfloordiv__(self, other: Union[int, float]) -> "Vector":
        return Vector([other // a for a in self.__data])

    # --- Negation ---
    def __neg__(self) -> "Vector":
        return Vector([-a for a in self.__data])

    # --- Indexing ---
    def __getitem__(self, index: Union[int, slice]) -> "Union[int, float, Vector]":
        result = self.__data[index]
        if isinstance(result, list):
            return Vector(result)
        return result

    def __setitem__(self, index: Union[int, slice], value: Union[int, float, List[Union[int, float]]]) -> None:
        if isinstance(index, slice) and isinstance(value, (list, Vector)):
            self.__data[index] = value.__data if isinstance(value, Vector) else value
        elif isinstance(index, int) and isinstance(value, (int, float)):
            self.__data[index] = value
        else:
            raise TypeError("Index must be int or slice, value must be a number or Vector/list for slices")
    
    # def __iter__(self):
    #     return VectorIteratorReverse(self)

    def sorted_iter(self, lazy: bool = False):
        if lazy:
            return VectorSortedIteratorLazy(self)
        return VectorSortedIterator(self)

print(v0 := Vector(1))
print(v1 := Vector(1, 2, 3, 4, 5, 6, 7))
print(v2 := Vector([1, 2, 3, 4, 5, 6, 7]))
print(v3 := Vector({1, 2, 3, 4, 5, 6, 7}))
print(v4 := Vector((1, 2, 3, 4, 5, 6, 7)))

# vector_iterator = VectorIteratorReverse(v1)
# for e in vector_iterator:
#     print(e)

for e in v1.sorted_iter():
    print(e)

for e in v1.sorted_iter(lazy=True):
    print(e)


# addition
print(v1 + v2)       # vector + vector
print(v1 + 1)        # vector + scalar
print(1 + v2)        # scalar + vector  (__radd__)

# subtraction
print(v1 - v2)       # vector - vector
print(v1 - 1)        # vector - scalar
print(10 - v1)       # scalar - vector  (__rsub__)

# dot product / scalar multiplication
print(v1 * v2)       # dot product -> scalar
print(v1 * 2)        # vector * scalar
print(2 * v1)        # scalar * vector  (__rmul__)

# division
print(v1 / 2)        # vector / scalar
print(10 / v1)       # scalar / vector  (__rtruediv__)
print(v1 // 2)       # floor division
print(10 // v1)      # scalar // vector (__rfloordiv__)

# negation
print(-v1)

# indexing / slicing
# print(v1[0])         # single element
# print(v1[1:4])       # slice -> Vector

# in-place
a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
a += b;  print(a)
a -= b;  print(a)
a *= 2;  print(a)
a /= 2;  print(a)
a //= 2; print(a)

# len
print(len(v1))






# l1 = [1, 2, 3, 4, 5, 6]
# it = iter(l1)
# val = next(it)
# val = next(it)
