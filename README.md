# numpy_exercises
python numpy exercises

## diamondarray
Return a diamond pattern for a square dimension. Fill and unfill numbers are 1 and 0 respectively and can be overridden as needed.

For N=5:

print(diamondarray(5))

```
[[0. 0. 1. 0. 0.]
 [0. 1. 0. 1. 0.]
 [1. 0. 0. 0. 1.]
 [0. 1. 0. 1. 0.]
 [0. 0. 1. 0. 0.]]
```

For N=8:

print(diamondarray(8))

```
[[0. 0. 0. 1. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0. 1. 0. 0.]
 [0. 1. 0. 0. 0. 0. 1. 0.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 1.]
 [0. 1. 0. 0. 0. 0. 1. 0.]
 [0. 0. 1. 0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 1. 0. 0. 0.]]
```

## bisectorarray
Return a bisected pattern for a square dimension. Fill and unfill numbers are 1 and 0 respectively and can be overridden as needed.

For N=3:

print(bisectorarray(3))

```
[[0. 1. 0.]
 [1. 1. 1.]
 [0. 1. 0.]]
```

For N=6:

print(bisectorarray(6))

```
[[0. 0. 1. 1. 0. 0.]
 [0. 0. 1. 1. 0. 0.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [0. 0. 1. 1. 0. 0.]
 [0. 0. 1. 1. 0. 0.]]
```
