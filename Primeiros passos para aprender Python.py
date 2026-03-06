# ========================================
# PROGRAMA: Aprendendo Python com Quiz
# ========================================
# Este programa ensina Python e TESTA seu conhecimento!
# Você precisa responder perguntas em cada etapa.

print("🐍 BEMVINDO AO PYTHON INTERATIVO COM QUIZ! 🐍 - Primeiros passos para aprender Python.py:7")
print("= - Primeiros passos para aprender Python.py:8" * 50)
print("Você vai aprender E ser testado em cada conceito! - Primeiros passos para aprender Python.py:9")
print()

pontos = 0  # Contador de acertos

# ========================================
# PARTE 1: O COMANDO PRINT()
# ========================================
print("📢 PARTE 1: O COMANDO PRINT() - Primeiros passos para aprender Python.py:17")
print("" * 50)
print()

print("O comando print() serve para MOSTRAR coisas na tela. - Primeiros passos para aprender Python.py:21")
print("Exemplo: - Primeiros passos para aprender Python.py:22")
print()
print("print('Olá, mundo!') - Primeiros passos para aprender Python.py:24")
print()
print("Isso vai mostrar: Olá, mundo! - Primeiros passos para aprender Python.py:26")
print()

# QUIZ 1
print("❓ PERGUNTA 1: - Primeiros passos para aprender Python.py:30")
print("Se eu escrever:  print('Python é legal') - Primeiros passos para aprender Python.py:31")
print("O que vai aparecer na tela? - Primeiros passos para aprender Python.py:32")
print()
resposta = input("Sua resposta: ")

if resposta.lower() == "python é legal" or resposta.lower() == "python e legal":
    print("✅ CORRETO! Muito bem! - Primeiros passos para aprender Python.py:37")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: Python é legal - Primeiros passos para aprender Python.py:40")
    print("(O print mostra exatamente o que está entre aspas) - Primeiros passos para aprender Python.py:41")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 2
print("❓ PERGUNTA 2: - Primeiros passos para aprender Python.py:48")
print("Qual está CORRETO? - Primeiros passos para aprender Python.py:49")
print()
print("A) print(Olá) - Primeiros passos para aprender Python.py:51")
print("B) print('Olá') - Primeiros passos para aprender Python.py:52")
print("C) Print('Olá') - Primeiros passos para aprender Python.py:53")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! O texto precisa estar entre aspas! - Primeiros passos para aprender Python.py:58")
    print("E 'print' deve ser minúsculo. - Primeiros passos para aprender Python.py:59")
    pontos += 1
else:
    print("❌ ERRADO! A resposta correta é B - Primeiros passos para aprender Python.py:62")
    print("→ Texto precisa ter aspas: print('Olá') - Primeiros passos para aprender Python.py:63")
    print("→ 'print' deve ser minúsculo (não Print) - Primeiros passos para aprender Python.py:64")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 2: VARIÁVEIS
# ========================================
print("📦 PARTE 2: VARIÁVEIS - Primeiros passos para aprender Python.py:73")
print("" * 50)
print()

print("Variáveis são CAIXINHAS que guardam informações. - Primeiros passos para aprender Python.py:77")
print("Para criar uma variável: - Primeiros passos para aprender Python.py:78")
print()
print("nome_da_variavel = valor - Primeiros passos para aprender Python.py:80")
print()
print("Exemplo: - Primeiros passos para aprender Python.py:82")
print("idade = 15 - Primeiros passos para aprender Python.py:83")
print("nome = 'Maria' - Primeiros passos para aprender Python.py:84")
print()

# QUIZ 3
print("❓ PERGUNTA 3: - Primeiros passos para aprender Python.py:88")
print("Se eu escrevo:  cidade = 'São Paulo' - Primeiros passos para aprender Python.py:89")
print("O que fica guardado na variável 'cidade'? - Primeiros passos para aprender Python.py:90")
print()
resposta = input("Sua resposta: ")

if "são paulo" in resposta.lower() or "sao paulo" in resposta.lower():
    print("✅ CORRETO! A variável cidade guarda 'São Paulo' - Primeiros passos para aprender Python.py:95")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: São Paulo - Primeiros passos para aprender Python.py:98")
    print("(O que está depois do = é o que fica guardado) - Primeiros passos para aprender Python.py:99")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 4
print("❓ PERGUNTA 4: - Primeiros passos para aprender Python.py:106")
print("Eu quero guardar o número 25 em uma variável chamada 'pontos'. - Primeiros passos para aprender Python.py:107")
print("Como eu escrevo isso? - Primeiros passos para aprender Python.py:108")
print()
resposta = input("Sua resposta: ")

if "pontos" in resposta.lower() and "25" in resposta and "=" in resposta:
    print("✅ CORRETO! É assim: pontos = 25 - Primeiros passos para aprender Python.py:113")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: pontos = 25 - Primeiros passos para aprender Python.py:116")
    print("(Formato: nome_variavel = valor) - Primeiros passos para aprender Python.py:117")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 3: TIPOS DE DADOS
# ========================================
print("🏷️  PARTE 3: TIPOS DE DADOS - Primeiros passos para aprender Python.py:126")
print("" * 50)
print()

print("Existem 3 tipos principais: - Primeiros passos para aprender Python.py:130")
print()
print("1. STRING (texto) → sempre entre aspas - Primeiros passos para aprender Python.py:132")
print("Exemplo: 'cachorro', 'azul', '123' - Primeiros passos para aprender Python.py:133")
print()
print("2. INTEGER (número inteiro) → sem aspas, sem vírgula - Primeiros passos para aprender Python.py:135")
print("Exemplo: 10, 500, 3 - Primeiros passos para aprender Python.py:136")
print()
print("3. FLOAT (número decimal) → com ponto decimal - Primeiros passos para aprender Python.py:138")
print("Exemplo: 3.14, 10.5, 2.8 - Primeiros passos para aprender Python.py:139")
print()

# QUIZ 5
print("❓ PERGUNTA 5: - Primeiros passos para aprender Python.py:143")
print("Qual é o tipo de dado de:  'Python' - Primeiros passos para aprender Python.py:144")
print()
print("A) String - Primeiros passos para aprender Python.py:146")
print("B) Integer - Primeiros passos para aprender Python.py:147")
print("C) Float - Primeiros passos para aprender Python.py:148")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "A":
    print("✅ CORRETO! Tem aspas = é STRING (texto) - Primeiros passos para aprender Python.py:153")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (String) - Primeiros passos para aprender Python.py:156")
    print("→ Tudo entre aspas é texto/string - Primeiros passos para aprender Python.py:157")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 6
print("❓ PERGUNTA 6: - Primeiros passos para aprender Python.py:164")
print("Qual é o tipo de dado de:  42 - Primeiros passos para aprender Python.py:165")
print()
print("A) String - Primeiros passos para aprender Python.py:167")
print("B) Integer - Primeiros passos para aprender Python.py:168")
print("C) Float - Primeiros passos para aprender Python.py:169")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! Número sem ponto = INTEGER - Primeiros passos para aprender Python.py:174")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (Integer) - Primeiros passos para aprender Python.py:177")
    print("→ Número inteiro, sem aspas, sem ponto = integer - Primeiros passos para aprender Python.py:178")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 7
print("❓ PERGUNTA 7: - Primeiros passos para aprender Python.py:185")
print("Qual é o tipo de dado de:  19.90 - Primeiros passos para aprender Python.py:186")
print()
print("A) String - Primeiros passos para aprender Python.py:188")
print("B) Integer - Primeiros passos para aprender Python.py:189")
print("C) Float - Primeiros passos para aprender Python.py:190")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "C":
    print("✅ CORRETO! Número com ponto = FLOAT - Primeiros passos para aprender Python.py:195")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era C (Float) - Primeiros passos para aprender Python.py:198")
    print("→ Número com ponto decimal = float - Primeiros passos para aprender Python.py:199")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 4: COMENTÁRIOS
# ========================================
print("💬 PARTE 4: COMENTÁRIOS - Primeiros passos para aprender Python.py:208")
print("" * 50)
print()

print("O símbolo # serve para comentários. - Primeiros passos para aprender Python.py:212")
print("Tudo depois do # é IGNORADO pelo Python. - Primeiros passos para aprender Python.py:213")
print()
print("Exemplo: - Primeiros passos para aprender Python.py:215")
print("idade = 20  # Isto é um comentário - Primeiros passos para aprender Python.py:216")
print()
print("O Python só vê: idade = 20 - Primeiros passos para aprender Python.py:218")
print("Ele ignora tudo depois do # - Primeiros passos para aprender Python.py:219")
print()

# QUIZ 8
print("❓ PERGUNTA 8: - Primeiros passos para aprender Python.py:223")
print("Neste código: - Primeiros passos para aprender Python.py:224")
print()
print("nome = 'João'  # guardando o nome - Primeiros passos para aprender Python.py:226")
print()
print("O que o Python vai executar? - Primeiros passos para aprender Python.py:228")
print()
print("A) nome = 'João'  # guardando o nome - Primeiros passos para aprender Python.py:230")
print("B) nome = 'João' - Primeiros passos para aprender Python.py:231")
print("C) # guardando o nome - Primeiros passos para aprender Python.py:232")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! Python ignora tudo depois do # - Primeiros passos para aprender Python.py:237")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B - Primeiros passos para aprender Python.py:240")
    print("→ O # e tudo depois dele é ignorado - Primeiros passos para aprender Python.py:241")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 5: DESAFIO PRÁTICO
# ========================================
print("🎯 PARTE 5: DESAFIO PRÁTICO! - Primeiros passos para aprender Python.py:250")
print("" * 50)
print()

print("Agora você vai ESCREVER código de verdade! - Primeiros passos para aprender Python.py:254")
print()

# DESAFIO 1
print("✏️  DESAFIO 1: - Primeiros passos para aprender Python.py:258")
print("Escreva um comando que mostre a mensagem: Oi! - Primeiros passos para aprender Python.py:259")
print("(Lembrese do comando print e das aspas) - Primeiros passos para aprender Python.py:260")
print()
resposta = input("Seu código: ")

if "print" in resposta.lower() and ("'oi!'" in resposta.lower() or '"oi!"' in resposta.lower() or "'oi'" in resposta.lower() or '"oi"' in resposta.lower()):
    print("✅ CORRETO! Muito bem! - Primeiros passos para aprender Python.py:265")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: print('Oi!') - Primeiros passos para aprender Python.py:268")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 2
print("✏️  DESAFIO 2: - Primeiros passos para aprender Python.py:275")
print("Crie uma variável chamada 'numero' que guarda o valor 100 - Primeiros passos para aprender Python.py:276")
print()
resposta = input("Seu código: ")

if "numero" in resposta.lower() and "100" in resposta and "=" in resposta:
    print("✅ CORRETO! Perfeito! - Primeiros passos para aprender Python.py:281")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: numero = 100 - Primeiros passos para aprender Python.py:284")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 3
print("✏️  DESAFIO 3: - Primeiros passos para aprender Python.py:291")
print("Crie uma variável 'preco' que guarda 49.90 - Primeiros passos para aprender Python.py:292")
print()
resposta = input("Seu código: ")

if "preco" in resposta.lower() and "49.90" in resposta and "=" in resposta:
    print("✅ CORRETO! Você entendeu float! - Primeiros passos para aprender Python.py:297")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: preco = 49.90 - Primeiros passos para aprender Python.py:300")

print()
input("👉 Pressione ENTER para ver seu resultado...")
print()

# ========================================
# RESULTADO FINAL
# ========================================
print("🏆 RESULTADO FINAL - Primeiros passos para aprender Python.py:309")
print("= - Primeiros passos para aprender Python.py:310" * 50)
print()
print(f"Você acertou {pontos} de 11 questões! - Primeiros passos para aprender Python.py:312")
print()

porcentagem = (pontos / 11) * 100

if porcentagem >= 90:
    print("🌟 EXCELENTE! Você é um gênio do Python! - Primeiros passos para aprender Python.py:318")
elif porcentagem >= 70:
    print("😊 MUITO BOM! Você está aprendendo rápido! - Primeiros passos para aprender Python.py:320")
elif porcentagem >= 50:
    print("👍 BOM! Continue praticando! - Primeiros passos para aprender Python.py:322")
else:
    print("💪 Não desista! Revise os conceitos e tente novamente! - Primeiros passos para aprender Python.py:324")

print()
print("Pontuação: {:.1f}% - Primeiros passos para aprender Python.py:327".format(porcentagem))
print()
print("= - Primeiros passos para aprender Python.py:329" * 50)
print("Continue estudando Python! 🐍🚀 - Primeiros passos para aprender Python.py:330")
print("Pratique todos os dias para melhorar! - Primeiros passos para aprender Python.py:331")
print()
print("= - Primeiros passos para aprender Python.py:333" * 50)
# ========================================
# PROGRAMA: Python Avançado com Quiz - PARTE 2
# ========================================
# Continuação: 30 exercícios de LÓGICA DE PROGRAMAÇÃO!

print("🐍 PYTHON AVANÇADO  PARTE 2: LÓGICA DE PROGRAMAÇÃO! 🐍 - Primeiros passos para aprender Python.py:339")
print("= - Primeiros passos para aprender Python.py:340" * 60)
print("Agora você vai aprender a PENSAR como um programador! - Primeiros passos para aprender Python.py:341")
print()

pontos = 0  # Contador de acertos

# ========================================
# PARTE 6: OPERADORES MATEMÁTICOS
# ========================================
print("➕ PARTE 6: OPERADORES MATEMÁTICOS - Primeiros passos para aprender Python.py:349")
print("" * 60)
print()

print("Python pode fazer contas! Veja os operadores: - Primeiros passos para aprender Python.py:353")
print()
print("+  → Adição        (5 + 3 = 8) - Primeiros passos para aprender Python.py:355")
print("→ Subtração     (10  4 = 6) - Primeiros passos para aprender Python.py:356")
print("*  → Multiplicação (3 * 4 = 12) - Primeiros passos para aprender Python.py:357")
print("/  → Divisão       (10 / 2 = 5.0) - Primeiros passos para aprender Python.py:358")
print("// → Divisão inteira (10 // 3 = 3) - Primeiros passos para aprender Python.py:359")
print("%  → Resto da divisão (10 % 3 = 1) - Primeiros passos para aprender Python.py:360")
print("** → Potência      (2 ** 3 = 8) - Primeiros passos para aprender Python.py:361")
print()

# QUIZ 9
print("❓ PERGUNTA 9: - Primeiros passos para aprender Python.py:365")
print("Qual é o resultado de:  7 + 5 * 2 - Primeiros passos para aprender Python.py:366")
print("(Lembre: multiplicação vem antes da adição!) - Primeiros passos para aprender Python.py:367")
print()
resposta = input("Sua resposta: ")

if resposta == "17":
    print("✅ CORRETO! 5*2=10, depois 7+10=17 - Primeiros passos para aprender Python.py:372")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 17 - Primeiros passos para aprender Python.py:375")
    print("→ Primeiro: 5 * 2 = 10 - Primeiros passos para aprender Python.py:376")
    print("→ Depois: 7 + 10 = 17 - Primeiros passos para aprender Python.py:377")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 10
print("❓ PERGUNTA 10: - Primeiros passos para aprender Python.py:384")
print("Qual é o resultado de:  10 % 3 - Primeiros passos para aprender Python.py:385")
print("(O % retorna o RESTO da divisão) - Primeiros passos para aprender Python.py:386")
print()
resposta = input("Sua resposta: ")

if resposta == "1":
    print("✅ CORRETO! 10 dividido por 3 = 3, sobra 1 - Primeiros passos para aprender Python.py:391")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 1 - Primeiros passos para aprender Python.py:394")
    print("→ 10 ÷ 3 = 3 (sobra 1) - Primeiros passos para aprender Python.py:395")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 11
print("❓ PERGUNTA 11: - Primeiros passos para aprender Python.py:402")
print("Qual é o resultado de:  2 ** 4 - Primeiros passos para aprender Python.py:403")
print("(** significa potência) - Primeiros passos para aprender Python.py:404")
print()
resposta = input("Sua resposta: ")

if resposta == "16":
    print("✅ CORRETO! 2^4 = 2*2*2*2 = 16 - Primeiros passos para aprender Python.py:409")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 16 - Primeiros passos para aprender Python.py:412")
    print("→ 2 ** 4 = 2 × 2 × 2 × 2 = 16 - Primeiros passos para aprender Python.py:413")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 12
print("❓ PERGUNTA 12: - Primeiros passos para aprender Python.py:420")
print("Eu tenho: x = 5 - Primeiros passos para aprender Python.py:421")
print("Depois faço: x = x + 3 - Primeiros passos para aprender Python.py:422")
print("Qual é o valor de x agora? - Primeiros passos para aprender Python.py:423")
print()
resposta = input("Sua resposta: ")

if resposta == "8":
    print("✅ CORRETO! x era 5, agora é 5+3 = 8 - Primeiros passos para aprender Python.py:428")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 8 - Primeiros passos para aprender Python.py:431")
    print("→ Pega o valor atual (5) e soma 3 - Primeiros passos para aprender Python.py:432")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 7: OPERADORES DE COMPARAÇÃO
# ========================================
print("⚖️  PARTE 7: OPERADORES DE COMPARAÇÃO - Primeiros passos para aprender Python.py:441")
print("" * 60)
print()

print("Comparações retornam True (verdadeiro) ou False (falso): - Primeiros passos para aprender Python.py:445")
print()
print("==  → Igual a         (5 == 5 → True) - Primeiros passos para aprender Python.py:447")
print("!=  → Diferente de    (5 != 3 → True) - Primeiros passos para aprender Python.py:448")
print(">   → Maior que       (7 > 5 → True) - Primeiros passos para aprender Python.py:449")
print("<   → Menor que       (3 < 8 → True) - Primeiros passos para aprender Python.py:450")
print(">=  → Maior ou igual  (5 >= 5 → True) - Primeiros passos para aprender Python.py:451")
print("<=  → Menor ou igual  (4 <= 6 → True) - Primeiros passos para aprender Python.py:452")
print()

# QUIZ 13
print("❓ PERGUNTA 13: - Primeiros passos para aprender Python.py:456")
print("Qual é o resultado de:  10 > 5 - Primeiros passos para aprender Python.py:457")
print()
print("A) True - Primeiros passos para aprender Python.py:459")
print("B) False - Primeiros passos para aprender Python.py:460")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "A":
    print("✅ CORRETO! 10 é maior que 5 = True - Primeiros passos para aprender Python.py:465")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (True) - Primeiros passos para aprender Python.py:468")
    print("→ 10 é maior que 5, então é verdadeiro - Primeiros passos para aprender Python.py:469")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 14
print("❓ PERGUNTA 14: - Primeiros passos para aprender Python.py:476")
print("Qual é o resultado de:  7 == 7 - Primeiros passos para aprender Python.py:477")
print()
print("A) True - Primeiros passos para aprender Python.py:479")
print("B) False - Primeiros passos para aprender Python.py:480")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "A":
    print("✅ CORRETO! 7 é igual a 7 = True - Primeiros passos para aprender Python.py:485")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (True) - Primeiros passos para aprender Python.py:488")
    print("→ == verifica se são iguais - Primeiros passos para aprender Python.py:489")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 15
print("❓ PERGUNTA 15: - Primeiros passos para aprender Python.py:496")
print("Qual é o resultado de:  5 != 5 - Primeiros passos para aprender Python.py:497")
print()
print("A) True - Primeiros passos para aprender Python.py:499")
print("B) False - Primeiros passos para aprender Python.py:500")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "B":
    print("✅ CORRETO! 5 não é diferente de 5 = False - Primeiros passos para aprender Python.py:505")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (False) - Primeiros passos para aprender Python.py:508")
    print("→ != significa 'diferente de' - Primeiros passos para aprender Python.py:509")
    print("→ 5 é igual a 5, então False - Primeiros passos para aprender Python.py:510")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 8: OPERADORES LÓGICOS
# ========================================
print("🔗 PARTE 8: OPERADORES LÓGICOS - Primeiros passos para aprender Python.py:519")
print("" * 60)
print()

print("Juntam várias condições: - Primeiros passos para aprender Python.py:523")
print()
print("and → E (ambos precisam ser True) - Primeiros passos para aprender Python.py:525")
print("True and True → True - Primeiros passos para aprender Python.py:526")
print("True and False → False - Primeiros passos para aprender Python.py:527")
print()
print("or  → OU (pelo menos um precisa ser True) - Primeiros passos para aprender Python.py:529")
print("True or False → True - Primeiros passos para aprender Python.py:530")
print("False or False → False - Primeiros passos para aprender Python.py:531")
print()
print("not → NÃO (inverte) - Primeiros passos para aprender Python.py:533")
print("not True → False - Primeiros passos para aprender Python.py:534")
print("not False → True - Primeiros passos para aprender Python.py:535")
print()

# QUIZ 16
print("❓ PERGUNTA 16: - Primeiros passos para aprender Python.py:539")
print("Qual é o resultado de:  True and False - Primeiros passos para aprender Python.py:540")
print()
print("A) True - Primeiros passos para aprender Python.py:542")
print("B) False - Primeiros passos para aprender Python.py:543")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "B":
    print("✅ CORRETO! Para 'and', AMBOS precisam ser True - Primeiros passos para aprender Python.py:548")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (False) - Primeiros passos para aprender Python.py:551")
    print("→ 'and' só é True se ambos forem True - Primeiros passos para aprender Python.py:552")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 17
print("❓ PERGUNTA 17: - Primeiros passos para aprender Python.py:559")
print("Qual é o resultado de:  True or False - Primeiros passos para aprender Python.py:560")
print()
print("A) True - Primeiros passos para aprender Python.py:562")
print("B) False - Primeiros passos para aprender Python.py:563")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "A":
    print("✅ CORRETO! Para 'or', basta UM ser True - Primeiros passos para aprender Python.py:568")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (True) - Primeiros passos para aprender Python.py:571")
    print("→ 'or' é True se pelo menos um for True - Primeiros passos para aprender Python.py:572")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 18
print("❓ PERGUNTA 18: - Primeiros passos para aprender Python.py:579")
print("Qual é o resultado de:  not True - Primeiros passos para aprender Python.py:580")
print()
print("A) True - Primeiros passos para aprender Python.py:582")
print("B) False - Primeiros passos para aprender Python.py:583")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "B":
    print("✅ CORRETO! 'not' inverte o valor - Primeiros passos para aprender Python.py:588")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (False) - Primeiros passos para aprender Python.py:591")
    print("→ 'not' inverte: True vira False - Primeiros passos para aprender Python.py:592")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 19
print("❓ PERGUNTA 19: - Primeiros passos para aprender Python.py:599")
print("Qual é o resultado de:  (5 > 3) and (10 < 20) - Primeiros passos para aprender Python.py:600")
print()
print("A) True - Primeiros passos para aprender Python.py:602")
print("B) False - Primeiros passos para aprender Python.py:603")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "A":
    print("✅ CORRETO! Ambas comparações são True! - Primeiros passos para aprender Python.py:608")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (True) - Primeiros passos para aprender Python.py:611")
    print("→ 5 > 3 é True - Primeiros passos para aprender Python.py:612")
    print("→ 10 < 20 é True - Primeiros passos para aprender Python.py:613")
    print("→ True and True = True - Primeiros passos para aprender Python.py:614")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 9: ESTRUTURA IF (CONDICIONAIS)
# ========================================
print("🔀 PARTE 9: ESTRUTURA IF (CONDICIONAIS) - Primeiros passos para aprender Python.py:623")
print("" * 60)
print()

print("O IF permite tomar DECISÕES no código: - Primeiros passos para aprender Python.py:627")
print()
print("if condição: - Primeiros passos para aprender Python.py:629")
print("# faz isso se for True - Primeiros passos para aprender Python.py:630")
print()
print("Exemplo: - Primeiros passos para aprender Python.py:632")
print("idade = 18 - Primeiros passos para aprender Python.py:633")
print("if idade >= 18: - Primeiros passos para aprender Python.py:634")
print("print('Você é maior de idade') - Primeiros passos para aprender Python.py:635")
print()
print("IMPORTANTE: A indentação (espaços) é obrigatória! - Primeiros passos para aprender Python.py:637")
print()

# QUIZ 20
print("❓ PERGUNTA 20: - Primeiros passos para aprender Python.py:641")
print("Neste código: - Primeiros passos para aprender Python.py:642")
print()
print("nota = 8 - Primeiros passos para aprender Python.py:644")
print("if nota >= 7: - Primeiros passos para aprender Python.py:645")
print("print('Aprovado') - Primeiros passos para aprender Python.py:646")
print()
print("O que vai aparecer na tela? - Primeiros passos para aprender Python.py:648")
print()
resposta = input("Sua resposta: ")

if "aprovado" in resposta.lower():
    print("✅ CORRETO! nota (8) é >= 7, então mostra 'Aprovado' - Primeiros passos para aprender Python.py:653")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: Aprovado - Primeiros passos para aprender Python.py:656")
    print("→ 8 >= 7 é True, então executa o print - Primeiros passos para aprender Python.py:657")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 21
print("❓ PERGUNTA 21: - Primeiros passos para aprender Python.py:664")
print("Neste código: - Primeiros passos para aprender Python.py:665")
print()
print("temperatura = 15 - Primeiros passos para aprender Python.py:667")
print("if temperatura > 25: - Primeiros passos para aprender Python.py:668")
print("print('Está quente') - Primeiros passos para aprender Python.py:669")
print()
print("O que vai aparecer na tela? - Primeiros passos para aprender Python.py:671")
print()
print("A) Está quente - Primeiros passos para aprender Python.py:673")
print("B) Nada - Primeiros passos para aprender Python.py:674")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "B":
    print("✅ CORRETO! 15 não é > 25, então não executa - Primeiros passos para aprender Python.py:679")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (Nada) - Primeiros passos para aprender Python.py:682")
    print("→ 15 > 25 é False, então pula o print - Primeiros passos para aprender Python.py:683")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 10: IF-ELSE
# ========================================
print("🔀 PARTE 10: IFELSE - Primeiros passos para aprender Python.py:692")
print("" * 60)
print()

print("O ELSE executa quando o IF é False: - Primeiros passos para aprender Python.py:696")
print()
print("if condição: - Primeiros passos para aprender Python.py:698")
print("# faz isso se True - Primeiros passos para aprender Python.py:699")
print("else: - Primeiros passos para aprender Python.py:700")
print("# faz isso se False - Primeiros passos para aprender Python.py:701")
print()
print("Exemplo: - Primeiros passos para aprender Python.py:703")
print("idade = 15 - Primeiros passos para aprender Python.py:704")
print("if idade >= 18: - Primeiros passos para aprender Python.py:705")
print("print('Maior de idade') - Primeiros passos para aprender Python.py:706")
print("else: - Primeiros passos para aprender Python.py:707")
print("print('Menor de idade') - Primeiros passos para aprender Python.py:708")
print()

# QUIZ 22
print("❓ PERGUNTA 22: - Primeiros passos para aprender Python.py:712")
print("Neste código: - Primeiros passos para aprender Python.py:713")
print()
print("saldo = 50 - Primeiros passos para aprender Python.py:715")
print("if saldo >= 100: - Primeiros passos para aprender Python.py:716")
print("print('Rico') - Primeiros passos para aprender Python.py:717")
print("else: - Primeiros passos para aprender Python.py:718")
print("print('Pobre') - Primeiros passos para aprender Python.py:719")
print()
print("O que vai aparecer? - Primeiros passos para aprender Python.py:721")
print()
resposta = input("Sua resposta: ")

if "pobre" in resposta.lower():
    print("✅ CORRETO! saldo (50) não é >= 100, então vai pro else - Primeiros passos para aprender Python.py:726")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: Pobre - Primeiros passos para aprender Python.py:729")
    print("→ 50 >= 100 é False - Primeiros passos para aprender Python.py:730")
    print("→ Executa o else - Primeiros passos para aprender Python.py:731")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 23
print("❓ PERGUNTA 23: - Primeiros passos para aprender Python.py:738")
print("Eu quero verificar se um número é PAR ou ÍMPAR. - Primeiros passos para aprender Python.py:739")
print("Qual operador uso para verificar se é par? - Primeiros passos para aprender Python.py:740")
print()
print("A) numero / 2 - Primeiros passos para aprender Python.py:742")
print("B) numero % 2 - Primeiros passos para aprender Python.py:743")
print("C) numero == 2 - Primeiros passos para aprender Python.py:744")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! numero % 2 == 0 significa que é par - Primeiros passos para aprender Python.py:749")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B - Primeiros passos para aprender Python.py:752")
    print("→ % retorna o resto da divisão - Primeiros passos para aprender Python.py:753")
    print("→ Se numero % 2 == 0, é par - Primeiros passos para aprender Python.py:754")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 11: IF-ELIF-ELSE
# ========================================
print("🔀 PARTE 11: IFELIFELSE - Primeiros passos para aprender Python.py:763")
print("" * 60)
print()

print("ELIF permite testar VÁRIAS condições: - Primeiros passos para aprender Python.py:767")
print()
print("if condição1: - Primeiros passos para aprender Python.py:769")
print("# executa isso - Primeiros passos para aprender Python.py:770")
print("elif condição2: - Primeiros passos para aprender Python.py:771")
print("# executa isso - Primeiros passos para aprender Python.py:772")
print("else: - Primeiros passos para aprender Python.py:773")
print("# executa isso - Primeiros passos para aprender Python.py:774")
print()
print("Exemplo: - Primeiros passos para aprender Python.py:776")
print("nota = 7 - Primeiros passos para aprender Python.py:777")
print("if nota >= 9: - Primeiros passos para aprender Python.py:778")
print("print('A') - Primeiros passos para aprender Python.py:779")
print("elif nota >= 7: - Primeiros passos para aprender Python.py:780")
print("print('B') - Primeiros passos para aprender Python.py:781")
print("else: - Primeiros passos para aprender Python.py:782")
print("print('C') - Primeiros passos para aprender Python.py:783")
print()

# QUIZ 24
print("❓ PERGUNTA 24: - Primeiros passos para aprender Python.py:787")
print("Neste código: - Primeiros passos para aprender Python.py:788")
print()
print("pontos = 85 - Primeiros passos para aprender Python.py:790")
print("if pontos >= 90: - Primeiros passos para aprender Python.py:791")
print("print('Ótimo') - Primeiros passos para aprender Python.py:792")
print("elif pontos >= 70: - Primeiros passos para aprender Python.py:793")
print("print('Bom') - Primeiros passos para aprender Python.py:794")
print("else: - Primeiros passos para aprender Python.py:795")
print("print('Ruim') - Primeiros passos para aprender Python.py:796")
print()
print("O que vai aparecer? - Primeiros passos para aprender Python.py:798")
print()
resposta = input("Sua resposta: ")

if "bom" in resposta.lower():
    print("✅ CORRETO! 85 não é >= 90, mas é >= 70 - Primeiros passos para aprender Python.py:803")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: Bom - Primeiros passos para aprender Python.py:806")
    print("→ 85 >= 90 é False - Primeiros passos para aprender Python.py:807")
    print("→ 85 >= 70 é True → executa o elif - Primeiros passos para aprender Python.py:808")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 12: LAÇO WHILE
# ========================================
print("🔄 PARTE 12: LAÇO WHILE (REPETIÇÃO) - Primeiros passos para aprender Python.py:817")
print("" * 60)
print()

print("WHILE repete código ENQUANTO a condição for True: - Primeiros passos para aprender Python.py:821")
print()
print("contador = 0 - Primeiros passos para aprender Python.py:823")
print("while contador < 3: - Primeiros passos para aprender Python.py:824")
print("print(contador) - Primeiros passos para aprender Python.py:825")
print("contador = contador + 1 - Primeiros passos para aprender Python.py:826")
print()
print("Isso vai mostrar: 0, 1, 2 - Primeiros passos para aprender Python.py:828")
print()
print("CUIDADO: Se a condição nunca ficar False, loop infinito! - Primeiros passos para aprender Python.py:830")
print()

# QUIZ 25
print("❓ PERGUNTA 25: - Primeiros passos para aprender Python.py:834")
print("Neste código: - Primeiros passos para aprender Python.py:835")
print()
print("x = 1 - Primeiros passos para aprender Python.py:837")
print("while x <= 3: - Primeiros passos para aprender Python.py:838")
print("print(x) - Primeiros passos para aprender Python.py:839")
print("x = x + 1 - Primeiros passos para aprender Python.py:840")
print()
print("Quantas vezes o print será executado? - Primeiros passos para aprender Python.py:842")
print()
resposta = input("Sua resposta: ")

if resposta == "3":
    print("✅ CORRETO! Vai mostrar 1, 2, 3 (3 vezes) - Primeiros passos para aprender Python.py:847")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 3 - Primeiros passos para aprender Python.py:850")
    print("→ x=1: print(1), x vira 2 - Primeiros passos para aprender Python.py:851")
    print("→ x=2: print(2), x vira 3 - Primeiros passos para aprender Python.py:852")
    print("→ x=3: print(3), x vira 4 - Primeiros passos para aprender Python.py:853")
    print("→ x=4: 4 <= 3 é False, para - Primeiros passos para aprender Python.py:854")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 26
print("❓ PERGUNTA 26: - Primeiros passos para aprender Python.py:861")
print("Este código vai parar alguma hora? - Primeiros passos para aprender Python.py:862")
print()
print("while True: - Primeiros passos para aprender Python.py:864")
print("print('Oi') - Primeiros passos para aprender Python.py:865")
print()
print("A) Sim - Primeiros passos para aprender Python.py:867")
print("B) Não (loop infinito) - Primeiros passos para aprender Python.py:868")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "B":
    print("✅ CORRETO! True é sempre True = loop infinito! - Primeiros passos para aprender Python.py:873")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B - Primeiros passos para aprender Python.py:876")
    print("→ True nunca vira False - Primeiros passos para aprender Python.py:877")
    print("→ O loop nunca para! - Primeiros passos para aprender Python.py:878")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 13: LAÇO FOR
# ========================================
print("🔄 PARTE 13: LAÇO FOR (REPETIÇÃO) - Primeiros passos para aprender Python.py:887")
print("" * 60)
print()

print("FOR repete código um NÚMERO ESPECÍFICO de vezes: - Primeiros passos para aprender Python.py:891")
print()
print("for i in range(5): - Primeiros passos para aprender Python.py:893")
print("print(i) - Primeiros passos para aprender Python.py:894")
print()
print("Isso mostra: 0, 1, 2, 3, 4 - Primeiros passos para aprender Python.py:896")
print()
print("range(5) gera números de 0 até 4 (5 números) - Primeiros passos para aprender Python.py:898")
print("range(2, 7) gera: 2, 3, 4, 5, 6 - Primeiros passos para aprender Python.py:899")
print()

# QUIZ 27
print("❓ PERGUNTA 27: - Primeiros passos para aprender Python.py:903")
print("Quantos números o range(10) gera? - Primeiros passos para aprender Python.py:904")
print()
resposta = input("Sua resposta: ")

if resposta == "10":
    print("✅ CORRETO! Gera 0,1,2,3,4,5,6,7,8,9 (10 números) - Primeiros passos para aprender Python.py:909")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 10 - Primeiros passos para aprender Python.py:912")
    print("→ range(10) = 0 até 9 (10 números) - Primeiros passos para aprender Python.py:913")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 28
print("❓ PERGUNTA 28: - Primeiros passos para aprender Python.py:920")
print("Neste código: - Primeiros passos para aprender Python.py:921")
print()
print("for i in range(3, 6): - Primeiros passos para aprender Python.py:923")
print("print(i) - Primeiros passos para aprender Python.py:924")
print()
print("O que vai aparecer? - Primeiros passos para aprender Python.py:926")
print()
print("A) 3, 4, 5 - Primeiros passos para aprender Python.py:928")
print("B) 3, 4, 5, 6 - Primeiros passos para aprender Python.py:929")
print("C) 0, 1, 2, 3, 4, 5 - Primeiros passos para aprender Python.py:930")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "A":
    print("✅ CORRETO! range(3,6) = 3,4,5 (6 não entra) - Primeiros passos para aprender Python.py:935")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A - Primeiros passos para aprender Python.py:938")
    print("→ range(início, fim) - Primeiros passos para aprender Python.py:939")
    print("→ Começa no 'início', para ANTES do 'fim' - Primeiros passos para aprender Python.py:940")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 14: BREAK E CONTINUE
# ========================================
print("⛔ PARTE 14: BREAK E CONTINUE - Primeiros passos para aprender Python.py:949")
print("" * 60)
print()

print("BREAK para o loop imediatamente: - Primeiros passos para aprender Python.py:953")
print()
print("for i in range(10): - Primeiros passos para aprender Python.py:955")
print("if i == 5: - Primeiros passos para aprender Python.py:956")
print("break - Primeiros passos para aprender Python.py:957")
print("print(i) - Primeiros passos para aprender Python.py:958")
print("→ Mostra: 0,1,2,3,4 (para quando i=5) - Primeiros passos para aprender Python.py:959")
print()
print("CONTINUE pula para a próxima iteração: - Primeiros passos para aprender Python.py:961")
print()
print("for i in range(5): - Primeiros passos para aprender Python.py:963")
print("if i == 2: - Primeiros passos para aprender Python.py:964")
print("continue - Primeiros passos para aprender Python.py:965")
print("print(i) - Primeiros passos para aprender Python.py:966")
print("→ Mostra: 0,1,3,4 (pula o 2) - Primeiros passos para aprender Python.py:967")
print()

# QUIZ 29
print("❓ PERGUNTA 29: - Primeiros passos para aprender Python.py:971")
print("Neste código: - Primeiros passos para aprender Python.py:972")
print()
print("for i in range(1, 6): - Primeiros passos para aprender Python.py:974")
print("if i == 3: - Primeiros passos para aprender Python.py:975")
print("break - Primeiros passos para aprender Python.py:976")
print("print(i) - Primeiros passos para aprender Python.py:977")
print()
print("O que vai aparecer? - Primeiros passos para aprender Python.py:979")
print()
print("A) 1, 2 - Primeiros passos para aprender Python.py:981")
print("B) 1, 2, 3 - Primeiros passos para aprender Python.py:982")
print("C) 1, 2, 4, 5 - Primeiros passos para aprender Python.py:983")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "A":
    print("✅ CORRETO! Para ANTES de mostrar o 3 - Primeiros passos para aprender Python.py:988")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A - Primeiros passos para aprender Python.py:991")
    print("→ i=1: mostra 1 - Primeiros passos para aprender Python.py:992")
    print("→ i=2: mostra 2 - Primeiros passos para aprender Python.py:993")
    print("→ i=3: break (para tudo) - Primeiros passos para aprender Python.py:994")

print()
input("👉 Pressione ENTER para continuar...")
print()

# QUIZ 30
print("❓ PERGUNTA 30: - Primeiros passos para aprender Python.py:1001")
print("Neste código: - Primeiros passos para aprender Python.py:1002")
print()
print("for i in range(1, 5): - Primeiros passos para aprender Python.py:1004")
print("if i == 2: - Primeiros passos para aprender Python.py:1005")
print("continue - Primeiros passos para aprender Python.py:1006")
print("print(i) - Primeiros passos para aprender Python.py:1007")
print()
print("O que vai aparecer? - Primeiros passos para aprender Python.py:1009")
print()
print("A) 1, 3, 4 - Primeiros passos para aprender Python.py:1011")
print("B) 1, 2, 3, 4 - Primeiros passos para aprender Python.py:1012")
print("C) 3, 4 - Primeiros passos para aprender Python.py:1013")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "A":
    print("✅ CORRETO! Continue PULA o 2, mostra os outros - Primeiros passos para aprender Python.py:1018")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A - Primeiros passos para aprender Python.py:1021")
    print("→ i=1: mostra 1 - Primeiros passos para aprender Python.py:1022")
    print("→ i=2: continue (pula) - Primeiros passos para aprender Python.py:1023")
    print("→ i=3: mostra 3 - Primeiros passos para aprender Python.py:1024")
    print("→ i=4: mostra 4 - Primeiros passos para aprender Python.py:1025")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 15: DESAFIOS DE LÓGICA
# ========================================
print("🧠 PARTE 15: DESAFIOS DE LÓGICA! - Primeiros passos para aprender Python.py:1034")
print("" * 60)
print()

# DESAFIO 4
print("✏️  DESAFIO 4: - Primeiros passos para aprender Python.py:1039")
print("Escreva uma condição que verifica se um número é MAIOR que 10 - Primeiros passos para aprender Python.py:1040")
print("Use a variável 'num' na sua resposta - Primeiros passos para aprender Python.py:1041")
print()
resposta = input("Seu código: ")

if "num" in resposta.lower() and ">" in resposta and "10" in resposta:
    print("✅ CORRETO! Exemplo: if num > 10: - Primeiros passos para aprender Python.py:1046")
    pontos += 1
else:
    print("❌ ERRADO! Exemplo: if num > 10: - Primeiros passos para aprender Python.py:1049")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 5
print("✏️  DESAFIO 5: - Primeiros passos para aprender Python.py:1056")
print("Complete: Um número é PAR quando ______ % 2 == 0 - Primeiros passos para aprender Python.py:1057")
print()
resposta = input("Preencha o espaço: ")

if "numero" in resposta.lower() or "num" in resposta.lower() or "n" == resposta.lower():
    print("✅ CORRETO! numero % 2 == 0 - Primeiros passos para aprender Python.py:1062")
    pontos += 1
else:
    print("❌ ERRADO! Resposta: numero % 2 == 0 - Primeiros passos para aprender Python.py:1065")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 6
print("✏️  DESAFIO 6: - Primeiros passos para aprender Python.py:1072")
print("Escreva um loop FOR que conta de 0 até 4 - Primeiros passos para aprender Python.py:1073")
print()
resposta = input("Seu código: ")

if "for" in resposta.lower() and "range" in resposta.lower() and "5" in resposta:
    print("✅ CORRETO! for i in range(5): - Primeiros passos para aprender Python.py:1078")
    pontos += 1
else:
    print("❌ ERRADO! Resposta: for i in range(5): - Primeiros passos para aprender Python.py:1081")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 7
print("✏️  DESAFIO 7: - Primeiros passos para aprender Python.py:1088")
print("Qual comando para o loop imediatamente? - Primeiros passos para aprender Python.py:1089")
print()
print("A) stop - Primeiros passos para aprender Python.py:1091")
print("B) break - Primeiros passos para aprender Python.py:1092")
print("C) end - Primeiros passos para aprender Python.py:1093")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! break para o loop - Primeiros passos para aprender Python.py:1098")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B (break) - Primeiros passos para aprender Python.py:1101")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 8
print("✏️  DESAFIO 8: - Primeiros passos para aprender Python.py:1108")
print("Verdadeiro ou Falso: - Primeiros passos para aprender Python.py:1109")
print("Em Python, a INDENTAÇÃO (espaços) é obrigatória? - Primeiros passos para aprender Python.py:1110")
print()
print("A) Verdadeiro - Primeiros passos para aprender Python.py:1112")
print("B) Falso - Primeiros passos para aprender Python.py:1113")
print()
resposta = input("Digite A ou B: ").upper()

if resposta == "A":
    print("✅ CORRETO! Python usa indentação para blocos de código - Primeiros passos para aprender Python.py:1118")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era A (Verdadeiro) - Primeiros passos para aprender Python.py:1121")
    print("→ Indentação é OBRIGATÓRIA em Python! - Primeiros passos para aprender Python.py:1122")

print()
input("👉 Pressione ENTER para continuar...")
print()

# ========================================
# PARTE 16: DESAFIOS PRÁTICOS AVANÇADOS
# ========================================
print("💪 PARTE 16: DESAFIOS PRÁTICOS AVANÇADOS! - Primeiros passos para aprender Python.py:1131")
print("" * 60)
print()

# DESAFIO 9
print("✏️  DESAFIO 9: - Primeiros passos para aprender Python.py:1136")
print("Resolva mentalmente: - Primeiros passos para aprender Python.py:1137")
print("Se x = 10 e y = 3, qual é o valor de: x // y - Primeiros passos para aprender Python.py:1138")
print()
resposta = input("Sua resposta: ")

if resposta == "3":
    print("✅ CORRETO! 10 // 3 = 3 (divisão inteira) - Primeiros passos para aprender Python.py:1143")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: 3 - Primeiros passos para aprender Python.py:1146")
    print("→ // remove a parte decimal - Primeiros passos para aprender Python.py:1147")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 10
print("✏️  DESAFIO 10: - Primeiros passos para aprender Python.py:1154")
print("O que este código faz? - Primeiros passos para aprender Python.py:1155")
print()
print("for i in range(5): - Primeiros passos para aprender Python.py:1157")
print("if i % 2 == 0: - Primeiros passos para aprender Python.py:1158")
print("print(i) - Primeiros passos para aprender Python.py:1159")
print()
print("A) Mostra números ímpares - Primeiros passos para aprender Python.py:1161")
print("B) Mostra números pares - Primeiros passos para aprender Python.py:1162")
print("C) Mostra todos os números - Primeiros passos para aprender Python.py:1163")
print()
resposta = input("Digite A, B ou C: ").upper()

if resposta == "B":
    print("✅ CORRETO! i % 2 == 0 detecta números pares - Primeiros passos para aprender Python.py:1168")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era B - Primeiros passos para aprender Python.py:1171")
    print("→ % 2 == 0 significa divisível por 2 = par - Primeiros passos para aprender Python.py:1172")

print()
input("👉 Pressione ENTER para continuar...")
print()

# DESAFIO 11
print("✏️  DESAFIO 11: - Primeiros passos para aprender Python.py:1179")
print("Analise este código: - Primeiros passos para aprender Python.py:1180")
print()
print("x = 5 - Primeiros passos para aprender Python.py:1182")
print("y = 10 - Primeiros passos para aprender Python.py:1183")
print("if x > 3 and y < 15: - Primeiros passos para aprender Python.py:1184")
print("resultado = 'Sim' - Primeiros passos para aprender Python.py:1185")
print("else: - Primeiros passos para aprender Python.py:1186")
print("resultado = 'Não' - Primeiros passos para aprender Python.py:1187")
print()
print("Qual será o valor de 'resultado'? - Primeiros passos para aprender Python.py:1189")
print()
resposta = input("Sua resposta: ")

if "sim" in resposta.lower():
    print("✅ CORRETO! Ambas condições são True - Primeiros passos para aprender Python.py:1194")
    pontos += 1
else:
    print("❌ ERRADO! A resposta era: Sim - Primeiros passos para aprender Python.py:1197")
    print("→ 5 > 3 é True - Primeiros passos para aprender Python.py:1198")
    print("→ 10 < 15 é True - Primeiros passos para aprender Python.py:1199")
    print("→ True and True = True - Primeiros passos para aprender Python.py:1200")

print()
input("👉 Pressione ENTER para o resultado final...")
print()

# ========================================
# RESULTADO FINAL
# ========================================
print("🏆 RESULTADO FINAL  PARTE 2 - Primeiros passos para aprender Python.py:1209")
print("= - Primeiros passos para aprender Python.py:1210" * 60)
print()
print(f"Você acertou {pontos} de 30 questões nesta parte! - Primeiros passos para aprender Python.py:1212")
print()

porcentagem = (pontos / 30) * 100

if porcentagem >= 90:
    print("🌟 EXTRAORDINÁRIO! Você dominou a lógica de programação! - Primeiros passos para aprender Python.py:1218")
    print("Você está pronto para desafios mais avançados! - Primeiros passos para aprender Python.py:1219")
elif porcentagem >= 70:
    print("😊 PARABÉNS! Você tem uma boa base de lógica! - Primeiros passos para aprender Python.py:1221")
    print("Continue praticando para ser expert! - Primeiros passos para aprender Python.py:1222")
elif porcentagem >= 50:
    print("👍 BOM TRABALHO! Você está no caminho certo! - Primeiros passos para aprender Python.py:1224")
    print("Revise os conceitos de condicionais e loops! - Primeiros passos para aprender Python.py:1225")
else:
    print("💪 Não desista! Lógica de programação precisa de prática! - Primeiros passos para aprender Python.py:1227")
    print("Revise cada parte com calma e tente novamente! - Primeiros passos para aprender Python.py:1228")

print()
print("Pontuação: {:.1f}% - Primeiros passos para aprender Python.py:1231".format(porcentagem))
print()
print("= - Primeiros passos para aprender Python.py:1233" * 60)
print()

print("📚 RESUMO DO QUE VOCÊ APRENDEU: - Primeiros passos para aprender Python.py:1236")
print()
print("✓ Operadores matemáticos (+, , *, /, %, **, //) - Primeiros passos para aprender Python.py:1238")
print("✓ Operadores de comparação (==, !=, >, <, >=, <=) - Primeiros passos para aprender Python.py:1239")
print("✓ Operadores lógicos (and, or, not) - Primeiros passos para aprender Python.py:1240")
print("✓ Estruturas condicionais (if, elif, else) - Primeiros passos para aprender Python.py:1241")
print("✓ Laços de repetição (while, for) - Primeiros passos para aprender Python.py:1242")
print("✓ Controle de fluxo (break, continue) - Primeiros passos para aprender Python.py:1243")
print("✓ Lógica de programação básica - Primeiros passos para aprender Python.py:1244")
print()
print("= - Primeiros passos para aprender Python.py:1246" * 60)
print()

print("🎯 PRÓXIMOS PASSOS: - Primeiros passos para aprender Python.py:1249")
print()
print("1. Pratique criando programas simples - Primeiros passos para aprender Python.py:1251")
print("2. Estude sobre LISTAS e DICIONÁRIOS - Primeiros passos para aprender Python.py:1252")
print("3. Aprenda sobre FUNÇÕES - Primeiros passos para aprender Python.py:1253")
print("4. Explore projetos práticos - Primeiros passos para aprender Python.py:1254")
print()
print("🐍 Continue sua jornada Python! 🚀 - Primeiros passos para aprender Python.py:1256")
print()
print("= - Primeiros passos para aprender Python.py:1258" * 60)
