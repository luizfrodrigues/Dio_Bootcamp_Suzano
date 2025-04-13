linguagens = ["python", "js", "c", "java", "csharp"]
#linguagens.sort() --> ordenado pela letra inicial
#linguagens.sort(reverse=True) --> ordem inversa
#linguagens.sort(key=lambda x: len(x)) --> ordenado pelo len da str
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

#print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
#print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

valor = [n**2 if n > 6 else n for n in range(10) if n%2 == 0]
print(valor)