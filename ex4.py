"""
Задача №4

 Дано рядок, що складається з рівно двох слів,
 розділених пропуском. Надрукуйте новий рядок,
 у якому позиції першого та другого слова змінені
 (друге слово друкується спочатку). У завданні не
 можна використовувати цикли і вказівку «якщо».

Автор: Новосад Сніжана
"""

input_string = input("Введіть рядок з двома словами, розділеними пропуском: ")

word1, word2 = input_string.split()

new_string = f"{word2} {word1}"

print(new_string)
