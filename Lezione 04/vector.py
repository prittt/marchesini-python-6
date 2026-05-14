from typing import Union, List, Tuple, Set, Self, cast

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
    

print(v0 := Vector(1))
print(v1 := Vector(1, 2, 3, 4, 5, 6, 7))
print(v2 := Vector([1, 2, 3, 4, 5, 6, 7]))
print(v3 := Vector({1, 2, 3, 4, 5, 6, 7}))
print(v4 := Vector((1, 2, 3, 4, 5, 6, 7)))

print(v3 := v1 + v2)
print(v4 := v1 + 1)
print(v5 := 1 + v2)

v4 += v1
v4 += v3