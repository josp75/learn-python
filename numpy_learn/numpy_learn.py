import numpy as np

if __name__ == "__main__":
    arr1 = np.array([10, 11, 12, 13, 14, 15])
    arr2 = np.array([20, 21, 22, 23, 24, 25])

    # Enter your code here
    arr3 = arr1 + arr2
    print(arr3)
    arr3 = np.add(arr1, arr2)
    print(arr3)
    print(np.__version__)
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(arr[1:8:2])
    u = np.array([1, 0])
    v = np.array([0, 1])
    z = u + v
    b = np.array([10, 20, 30, 40, 50, 60, 70])

    # Enter your code here
    print(b.size)
    print(b.ndim)
    print(b.shape)
    print(u)
    print(u.dtype)
    print(v)
    print(z)
    y = np.array([1, 2])
    z = 2 * y
    a = np.array([2, 8])
    b = np.array([3, 2])
    print(a * b)
    print(np.dot(a, b))
    print(z)
    pi = np.pi
    c = np.array([0, pi / 2, pi])
    print(c)
    d = np.sin(c)
    print(d)
    print(np.linspace(-5, 4, num=3))

    e = np.linspace(0, 2 * pi, num=100)
    f = np.sin(e)
    print(e)
