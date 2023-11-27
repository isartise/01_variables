

# Tekst, ciąg znaków (Strings)

text = "Lorem ipsum"
print(text)

# Możemy używać cudzysłowów lub apostrofów

my_name = "john"
print(my_name)

my_name = 'john'
print(my_name)


# Stringi można łączyć za pomocą operatora dodawania

part_one = "The quick brown fox"
part_two = "jumps over the lazy dog"

full_text = part_one + " " + part_two
print(full_text)


# Stringi można również mnożyć przez liczbę całkowitą

result = "echo" * 3
print(result)


# Stringi zawierają określoną liczbę znaków, możemy obliczyć ich długość za pomocą funkcji len()

text = "The quick brown fox"
text_length = len(text)
print(text_length)


# Możemy także tworzyć stringi z liczb

float_value = 3.14
text = "My favorite number is: " + str(float_value)
print(text)
