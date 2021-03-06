# convert matrix to a vector
import numpy as np
def mat2vec(x):
    m = x.shape[0] * x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i, j]
            c += 1
    return tmp1


def getHebrewLetters():
    # א
    a = np.array([[1, -1, -1, -1, -1, -1, -1, 1, -1, -1],
                  [-1, 1, -1, -1, -1, -1, -1, 1, -1, -1],
                  [-1, -1, 1, -1, -1, -1, -1, 1, -1, -1],
                  [-1, -1, 1, 1, -1, -1, -1, 1, -1, -1],
                  [-1, -1, 1, -1, 1, -1, -1, 1, -1, -1],
                  [-1, -1, 1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, 1, -1, -1, -1, 1, -1, -1, -1],
                  [-1, -1, 1, -1, -1, -1, -1, 1, -1, -1],
                  [-1, -1, 1, -1, -1, -1, -1, -1, 1, -1],
                  [-1, -1, 1, -1, -1, -1, -1, -1, -1, 1],
                  ])
    # ב
    b = np.array([[1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                  [1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  ])
    # ג
    c = np.array([[-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, 1, 1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1],
                  [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1],
                  ])
    # ד
    d = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  ])
    # ה
    e = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, -1, 1, 1],
                  ])
    # ו
    f = np.array([[-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
                  ])
    # ז
    g = np.array([[-1, -1, -1, 1, 1, 1, 1, 1, 1, -1],
                  [-1, -1, -1, 1, 1, 1, 1, 1, 1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1],
                  ])

    # ח
    h = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  ])
    # ט
    i = np.array([[1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, 1, 1, 1],
                  [1, 1, -1, -1, -1, -1, 1, 1, 1, 1],
                  [1, 1, -1, -1, -1, 1, 1, -1, 1, 1],
                  [1, 1, -1, -1, -1, 1, 1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  ])

    ans = [a, b, c, d, e, f, g, h, i]
    # for idx in range(0, 9):
    #     ans[idx] = np.asarray(ans[idx])

    for idx in ans:
        idx = mat2vec(idx)

    return ans