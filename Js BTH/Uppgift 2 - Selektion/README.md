[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Oi4VocEP)
# Temp converter
Den här uppgiften behandlar selektion.
Du behöver även skapa en funktion.

### Krav för uppgiften
Ditt program ska kunna konvertera temperaturer från en skala till en annan.

Skapa en fil som heter **temperatureConverter.js** och i den implementera en funktion som heter **convertTemperature**.

Funktionen ska kunna konvertera en angiven temperatur i en viss skala till en annan skala.
Skalorna som ska kunna konverteras är Celsius, Fahrenheit och Kelvin.
Exempelvis ska funktionen kunna konvertera 20 grader Celsius till korrekt gradantal i Kelvin, eller t ex 80 grader Fahrenheit till Celsius.

Förutom att testet ska kunna köras utan fel så är det ett krav att **selektion måste implementeras**. 

Exempelvis så kan du inkludera if, else-if, else eller t ex switch-strukturer i din källkod.

Funktionens signatur är som följer;

**convertTemperature(temperature, fromUnit, toUnit)**

Där parametrarna är;
- temperature - grader (t ex 20, 119 eller 80)
- fromUnit - i vilken skala vi anger temperature (Celsius, Fahrenheit eller Kelvin)
- toUnit - till vilken skala temperature ska konverteras till (Celsius, Fahrenheit eller Kelvin)

Retur-värdet från funktionen är alltså ett tal som är en konvertering av antalet grader (temperature) från en skala (fromUnit) till en annan skala (toUnit).
Exempelvis så ska 32 grader Fahrenheit bli 0 grader Celsius.


Testet som följer med i repot (temperatureConverter.test.js) ska användas (får ej ändras) och godkänt ges om testet körs utan fel.
Du kan installera jest med kommandot;


    $ npm install jest


För att köra testet;


    $npm test temperatureConverter.test.js


I övrigt gäller att package.json får ändras, men inga packages/andra moduler får tillämpas i din lösning.
Glöm heller inte att din lösning, när testet körs utan fel, ska lämnas in på Canvas som en zip för den här uppgiften.
I ditt repos startsida (den här) kan du t ex klicka på "Code" och välja zip i dropdown-menyn.
