# d = dict(
#     one=1,
#     two=3,
#     three=999,
#     four='hello'
# )
#
# for key, value in d.items():
#     print(key, '-->', value, end='')
#     print('!')

l = [
    [
        [0, 1, 5],
        [3, 6, 9]
    ],
    [
        [3, 7, 9],
        [5, 2, 1]
    ],
    [
        [5, 0, 3],
        [4, 7, 4]
    ]
]

for value_1 in l:
    for value_2 in value_1:
        for value_3 in value_2:
            print(value_3)
