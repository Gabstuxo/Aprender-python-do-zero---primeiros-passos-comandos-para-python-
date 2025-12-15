# ========================================
# PROGRAMA: Aprendendo Python com Quiz
# ========================================
# Este programa ensina Python e TESTA seu conhecimento!
# Você precisa responder perguntas em cada etapa.

print("🐍 BEM-VINDO AO PYTHON INTERATIVO COM QUIZ! 🐍")
print("=" * 50)
print("Você vai aprender E ser testado em cada conceito!")
print()

pontos = 0  # Contador de acertos

# ========================================
# PARTE 1: O COMANDO PRINT()
# ========================================
print("📢 PARTE 1: O COMANDO PRINT()")
print("-" * 50)
print()

print("O comando print() serve para MOSTRAR coisas na tela.")
print("Exemplo:")
print()
print("  print('Olá, mundo!')")
print()
print("Isso vai mostrar: Olá, mundo!")
print()

# QUIZ 1
print("❓ PERGUNTA 1:")
print("Se eu escrever:  print('Python é legal')")
print("O que vai aparecer na tela?")
print()
resposta = input("Sua resposta: ")

if resposta.lower() == "python é legal" or resposta.lower() == "python e legal":
    print("✅ CORRETO! Muito bem!")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: Python é legal")
    print("   (O print mostra exatamente o que está entre aspas)")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 2
print("❓ PERGUNTA 2:")
print("Qual está CORRETO?")
print()
print("A) print(Olá)")
print("B) print('Olá')")
print("C) Print('Olá')")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! O texto precisa estar entre aspas!")
    print("   E 'print' deve ser minúsculo.")
    pontos += 1
else:
    print("❌ ERRADO! A resposta correta é B")
    print("   → Texto precisa ter aspas: print('Olá')")
    print("   → 'print' deve ser minúsculo (não Print)")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 2: VARIÁVEIS
# ========================================
print("📦 PARTE 2: VARIÁVEIS")
print("-" * 50)
print()

print("Variáveis são CAIXINHAS que guardam informações.")
print("Para criar uma variável:")
print()
print("  nome_da_variavel = valor")
print()
print("Exemplo:")
print("  idade = 15")
print("  nome = 'Maria'")
print()

# QUIZ 3
print("❓ PERGUNTA 3:")
print("Se eu escrevo:  cidade = 'São Paulo'")
print("O que fica guardado na variável 'cidade'?")
print()
resposta = input("Sua resposta: ")

if "são paulo" in resposta.lower() or "sao paulo" in resposta.lower():
    print("✅ CORRETO! A variável cidade guarda 'São Paulo'")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: São Paulo")
    print("   (O que está depois do = é o que fica guardado)")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 4
print("❓ PERGUNTA 4:")
print("Eu quero guardar o número 25 em uma variável chamada 'pontos'.")
print("Como eu escrevo isso?")
print()
resposta = input("Sua resposta: ")

if "pontos" in resposta.lower() and "25" in resposta and "=" in resposta:
    print("✅ CORRETO! É assim: pontos = 25")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: pontos = 25")
    print("   (Formato: nome_variavel = valor)")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 3: TIPOS DE DADOS
# ========================================
print("🏷️  PARTE 3: TIPOS DE DADOS")
print("-" * 50)
print()

print("Existem 3 tipos principais:")
print()
print("1. STRING (texto) → sempre entre aspas")
print("   Exemplo: 'cachorro', 'azul', '123'")
print()
print("2. INTEGER (número inteiro) → sem aspas, sem vírgula")
print("   Exemplo: 10, 500, -3")
print()
print("3. FLOAT (número decimal) → com ponto decimal")
print("   Exemplo: 3.14, 10.5, -2.8")
print()

# QUIZ 5
print("❓ PERGUNTA 5:")
print("Qual é o tipo de dado de:  'Python'")
print()
print("A) String")
print("B) Integer")
print("C) Float")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "A":
    print("✅ CORRETO! Tem aspas = é STRING (texto)")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (String)")
    print("   → Tudo entre aspas é texto/string")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 6
print("❓ PERGUNTA 6:")
print("Qual é o tipo de dado de:  42")
print()
print("A) String")
print("B) Integer")
print("C) Float")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! Número sem ponto = INTEGER")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (Integer)")
    print("   → Número inteiro, sem aspas, sem ponto = integer")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 7
print("❓ PERGUNTA 7:")
print("Qual é o tipo de dado de:  19.90")
print()
print("A) String")
print("B) Integer")
print("C) Float")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "C":
    print("✅ CORRETO! Número com ponto = FLOAT")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era C (Float)")
    print("   → Número com ponto decimal = float")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 4: COMENTÁRIOS
# ========================================
print("💬 PARTE 4: COMENTÁRIOS")
print("-" * 50)
print()

print("O símbolo # serve para comentários.")
print("Tudo depois do # é IGNORADO pelo Python.")
print()
print("Exemplo:")
print("  idade = 20  # Isto é um comentário")
print()
print("O Python só vê: idade = 20")
print("Ele ignora tudo depois do #")
print()

# QUIZ 8
print("❓ PERGUNTA 8:")
print("Neste código:")
print()
print("  nome = 'João'  # guardando o nome")
print()
print("O que o Python vai executar?")
print()
print("A) nome = 'João'  # guardando o nome")
print("B) nome = 'João'")
print("C) # guardando o nome")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! Python ignora tudo depois do #")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B")
    print("   → O # e tudo depois dele é ignorado")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 5: DESAFIO PRÁTICO
# ========================================
print("🎯 PARTE 5: DESAFIO PRÁTICO!")
print("-" * 50)
print()

print("Agora você vai ESCREVER código de verdade!")
print()

# DESAFIO 1
print("✏️  DESAFIO 1:")
print("Escreva um comando que mostre a mensagem: Oi!")
print("(Lembre-se do comando print e das aspas)")
print()
resposta = input("Seu código: ")

if "print" in resposta.lower() and ("'oi!'" in resposta.lower() or '"oi!"' in resposta.lower() or "'oi'" in resposta.lower() or '"oi"' in resposta.lower()):
    print("✅ CORRETO! Muito bem!")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: print('Oi!')")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 2
print("✏️  DESAFIO 2:")
print("Crie uma variável chamada 'numero' que guarda o valor 100")
print()
resposta = input("Seu código: ")

if "numero" in resposta.lower() and "100" in resposta and "=" in resposta:
    print("✅ CORRETO! Perfeito!")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: numero = 100")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 3
print("✏️  DESAFIO 3:")
print("Crie uma variável 'preco' que guarda 49.90")
print()
resposta = input("Seu código: ")

if "preco" in resposta.lower() and "49.90" in resposta and "=" in resposta:
    print("✅ CORRETO! Você entendeu float!")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: preco = 49.90")

print()
input("👉 Pressione ENTER para ver seu resultado...")
print()

# ========================================
# RESULTADO FINAL
# ========================================
print("🏆 RESULTADO FINAL")
print("=" * 50)
print()
print(f"Você acertou {pontos} de 11 questões!")
print()

porcentagem = (pontos / 11) * 100

if porcentagem >= 90:
    print("🌟 EXCELENTE! Você é um gênio do Python!")
elif porcentagem >= 70:
    print("😊 MUITO BOM! Você está aprendendo rápido!")
elif porcentagem >= 50:
    print("👍 BOM! Continue praticando!")
else:
    print("💪 Não desista! Revise os conceitos e tente novamente!")

print()
print("Pontuação: {:.1f}%".format(porcentagem))
print()
print("=" * 50)
print("Continue estudando Python! 🐍🚀")
print("Pratique todos os dias para melhorar!")
print()
print("=" * 50)