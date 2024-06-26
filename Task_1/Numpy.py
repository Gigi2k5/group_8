from typing import List, Union, Tuple, Any # imporatation des typesnécessaires 

class Array:
    def __init__(self, data: Union[List[Any], List[List[Any]]]):
        if all(isinstance(i, list) for i in data):
            self.data = data
            self.shape = (len(data), len(data[0]))
        else:
            self.data = [data]
            self.shape = (len(data),)
    
    def __repr__(self):    # permet de retournre une représentation officielle de l'objet utile pour le débogage
        return f'Array({self.data})'
    
    def __len__(self) -> int:
        return self.shape[0]
    
    
    def __add__(self, other: 'Array') -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les tableaux doivent etre de meme forme pour les operations par element")
            if len(self.shape) == 1:
                return Array([a + b for a, b in zip(self.data[0], other.data[0])])
            return Array([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])
        else:
            return Array([[element + other for element in row] for row in self.data])

    def __sub__(self, other: 'Array') -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les tableaux doivent etre de meme forme pour les operations par element")
            if len(self.shape) == 1:
                return Array([a - b for a, b in zip(self.data[0], other.data[0])])
            return Array([[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])
        else:
            return Array([[element - other for element in row] for row in self.data])

    def __mul__(self, other: Union['Array', float, int]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("LLes tableaux doivent etre de meme forme pour les operations par element")
            if len(self.shape) == 1:
                return Array([a * b for a, b in zip(self.data[0], other.data[0])])
            return Array([[a * b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])
        else:
            return Array([[element * other for element in row] for row in self.data])
        
    def __rmul__(self, other: Union[float, int]) -> 'Array':
        return self.__mul__(other)

    def __truediv__(self, other: Union['Array', float, int]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les tableaux doivent etre de meme forme pour les operations par element")
            if len(self.shape) == 1:
                return Array([a / b for a, b in zip(self.data[0], other.data[0])])
            return Array([[a / b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])
        else:
            return Array([[element / other for element in row] for row in self.data])

    def __matmul__(self, other: 'Array') -> float:
        if len(self.shape) == 1 and len(other.shape) == 1:
            if len(self.data[0]) != len(other.data[0]):
                raise ValueError("Les tableaux doivent etre de meme forme pour les operations par element")
            return sum(a * b for a, b in zip(self.data[0], other.data[0]))
        else:
            raise ValueError("Le produit scalaire n’est pris en charge que pour les matrices 1D")
        
    def __contains__(self, item:Any) ->bool:
        return any(item in row for row in self.data)
    
    def __getitem__(self, index: Union[int, Tuple[Union[int, slice], Union[int, slice]]]):
        if isinstance(index, tuple):
            row_index, col_index = index
            if isinstance(row_index, slice) or isinstance(col_index, slice):
                sliced_data = [row[col_index] for row in self.data[row_index]] # Si le slicing retourne une seule ligne, retourner une liste simple
                if len(sliced_data) == 1:
                    return sliced_data[0] # Si le slicing retourne une seule colonne, retourner une liste simple
                if all(isinstance(i, list) and len(i) == 1 for i in sliced_data):
                    return [i[0] for i in sliced_data]
                return Array(sliced_data)
            return self.data[row_index][col_index]
        return self.data[0][index]

    
    def __setitem__(self, index: Union[int, Tuple[int, int]], value: Any):
        if isinstance(index, tuple):
            self.data[index[0]][index[1]] = value
        else:
            self.data[index] = value
    

# Exemple d'utilisation
if __name__ == "__main__":
    # Creation de tableaux
    x = Array([1, 2, 3])
    y = Array([4, 5, 6])
    z = Array([[1, 2], [3, 4]])

    # Operations elements par elements
    print(x + y)  # Array([5, 7, 9])
    print(x - y)  # Array([-3, -3, -3])
    print(x * 2)  # Array([2, 4, 6])
    print(2 * x)
    print(z * 2)  # Array([[2, 4], [6, 8]])

    # Produit scalaire
    print(x @ y)  # 32
    print(x @ y)  # 32

    # Recherche d'elements
    print(2 in x)  # True
    print(5 in x)  # False
    print(34 in y)
    print(84 in z)

    # Indexage et slicing
    print(z[1, 1])  # 4
    print((x[0:2]))  # [1, 2]
    print((x[0:]))
    print((z[0:2, 0]))  # [1, 3]
    print(z[0:2, 0:2])
    print((y[0:1]))

    # Longueur et forme
    print(len(x))  # 3
    print(len(z)) 
    print(z.shape)  # (2, 2)