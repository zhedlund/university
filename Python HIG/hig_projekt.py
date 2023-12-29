import random
import math

# Validerar textinput
def input_valid_str(question, error_message, possible_answers):
    answer = input(question)
    while answer not in possible_answers:
        print(error_message)
        answer = input(question)
    return answer

# Validerar att input är ett heltal inom givet intervall
def input_valid_int(question, error_message, min, max):
    while True:
        str = input(question)
        if str.isdigit():
            answer = int(str)
            if answer >= min and answer <= max:
                return answer
        print(error_message)

# Genererar multiplikationsfrågor baserade på vald tabell
def generate_questions(table):
    questions = []
    factors = list(range(13))  # 0-12
    random.shuffle(factors)  # Listan blandas för att ge frågorna i slumpmässig ordning
    for factor in factors:
        question = (factor, table)
        questions.append(question)
    return questions

# Frågar användaren en multiplikationsfråga. Kallar input_valid_int() för att undvika upprepning av kod.
def ask_question(question):
    factor, table = question
    answer = input_valid_int(f"Vad är {factor} gånger {table}? ", "Ange ett giltigt heltal!", 0, math.inf)
    return answer == factor * table

# Låter användaren välja en dörr. Kallar input_valid_int() här istället för i main, för att göra main mer lättläst.
def choose_door(num_doors):
    door = input_valid_int(f"\nVälj en dörr (1-{num_doors}): ", "Ange ett giltigt heltal!", 1, num_doors)
    return door

# Skriver ut introduktion och regler vid spelstart
print("""
🧟 Välkommen till Flykten från Zombiehuset 🧟

Du är fångad i ett hus fyllt av zombies och enda sättet att ta sig ut är genom att lösa matematiska gåtor och välja rätt dörr för att undvika att bli uppäten av zombies.

Reglerna är följande:

1. Välj en multiplikationstabell (2-12)
2. Svara på 12 multiplikationsfrågor
3. Svarar du rätt får du välja en dörr. Bakom en av dörrarna gömmer sig zombies. Antalet dörrar minskar för varje fråga.
4. Om du svarar fel på en fråga eller väljer fel dörr är det game over.
5. Om du lyckas svara rätt på alla 12 frågor och välja rätt dörrar, klarar du dig från zombies och vinner spelet!

För att starta, välj multiplikationstabell och var redo att använda dina mattekunskaper för att undkomma zombies 🧟🧟🧟

Lycka till!
  """)

play_again = "ja"  # Initialiseras till ja för att spelet ska köras minst en gång
while play_again == "ja":
    table = input_valid_int("Välj en multiplikationstabell (2-12): ", "Ange ett heltal mellan 2-12", 2, 12)
    questions = generate_questions(table)  # Genererar frågor utifrån vald tabell
    remaining = 12  # Antal kvarstående frågor
    i = 0
    game_over = False

    while i < 12 and not game_over:
        print(f"\nDu har klarat {i} frågor, {remaining} frågor kvarstår")
        if ask_question(questions[i]):  # Ställer frågan och kontrollerar om svaret är rätt
            if i == 11:  # Sista frågan
                print("\nGrattis! Du svarade rätt på alla frågor och lyckades fly från Zombiehuset!")
                game_over = True
            else:
                num_doors = remaining
                zombie_door = random.randint(1, num_doors)
                print(f"\nDu svarade rätt! Framför dig har du {num_doors} dörrar. Bakom en av dörrarna gömmer sig zombies.")
                door = choose_door(num_doors)  # Användaren väljer dörr
                if door == zombie_door:
                    print(f"Zombies var bakom dörr nr {zombie_door}. Game Over!")
                    game_over = True
                else:
                    print(f"Zombies var bakom dörr nr {zombie_door}. Du klarade dig undan!")
        else:
            print("\nOops! Fel svar. Du blev tagen av zombies :( Game Over!")
            game_over = True
        remaining -= 1  # Minskar antal kvarvarande frågor
        i += 1  # Fortsätter till nästa fråga
    play_again = input_valid_str("\nVill du spela igen? (ja/nej): ", "Ogiltigt svar!", ('ja', 'nej'))
print("Tack för att du spelade Flykten från Zombiehuset!")  # Om användare svarar nej