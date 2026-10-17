
imiona = ["Artur", "Basia", "Celina", "Dawid", "Eliza"]

# print(list(enumerate(imiona)))
# # [(0, 'Artur'), (1, 'Basia'), (2, 'Celina'), (3, 'Dawid'), (4, 'Eliza')]
# (0, 'Artur')
# for element in enumerate(imiona):
#     print(f"Zawodnik {element[1]} zajął miejsce {element[0]+1}")


x = (0, 'Artur')
print(x)
print(x[0])
print(x[1])

zajęte_miejsce, imie = (0, 'Artur')
print(zajęte_miejsce)
print(imie)

for zajęte_miejsce, imie in enumerate(imiona):
    print(f"Zawodnik {imie} zajął miejsce {zajęte_miejsce+1}")




