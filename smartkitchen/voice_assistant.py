import speech_recognition as sr
import pyttsx3

# =========================
# VOICE ENGINE
# =========================

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# =========================
# RECIPES
# =========================

RECIPES = {
    'biryani': """
Step 1: Wash rice properly.
Step 2: Cook onions in oil.
Step 3: Add ginger garlic paste.
Step 4: Add chicken and masala.
Step 5: Cook rice separately.
Step 6: Mix rice and chicken.
Step 7: Cook for 15 minutes.
Biryani is ready.
""",

    'tea': """
Step 1: Boil milk.
Step 2: Add tea powder.
Step 3: Add sugar.
Step 4: Boil for 5 minutes.
Tea is ready.
""",

    'coffee': """
Step 1: Boil milk.
Step 2: Add coffee powder.
Step 3: Add sugar.
Step 4: Mix well.
Coffee is ready.
"""
}


# =========================
# LISTEN FUNCTION (ENGLISH ONLY)
# =========================

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(
            audio,
            language='en-US'   # ✅ English only
        )

        print("You Said:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""


# =========================
# FIND RECIPE
# =========================

def find_recipe(command):

    for recipe in RECIPES:
        if recipe in command:
            return recipe

    return None


# =========================
# MAIN ASSISTANT
# =========================

def cooking_assistant():

    command = listen()

    if not command:
        speak("Sorry, I could not understand you.")
        return

    recipe_name = find_recipe(command)

    if recipe_name:
        instructions = RECIPES[recipe_name]

        print("\n🍲 Recipe Found:\n")
        print(instructions)

        speak(f"Here is the recipe for {recipe_name}")
        speak(instructions)

    else:
        speak("Recipe not found")


# =========================
# RUN
# =========================

cooking_assistant()