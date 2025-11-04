import streamlit as st
import random

# Lijst met alle woorden
woorden = [
    "Aap", "Achterkant", "Achtbaan", "Adem", "Alarmbel", "Alleen", "Alles", "Altijd", "Amerika", "Angst",
    "Ardennen", "Auto", "Avond", "Baas", "Baby", "Banaan", "Barcelona", "Bed", "Bellen", "Berg",
    "Blauw", "Blijven", "Boek", "Boom", "Boos", "Boot", "Bos", "Boterham", "Brug", "Bus",
    "Buur", "Carnaval", "Couplet", "Courgette", "Dag", "Dans", "Deur", "Dichtbij", "Disco", "Donker",
    "Dromen", "Eend", "Eerlijk", "Eerste", "Eiland", "Even", "Familie", "Fantasie", "Feest", "Feit",
    "Fiets", "Fout", "Gaan", "Geel", "Geloven", "Geluk", "Gitaarmuziek", "Gitaarspel", "Goud", "Groeien",
    "Grens", "Groen", "Haar", "Hallo", "Hart", "Hartslag", "Haten", "Heks", "Heup", "Herinneringen",
    "Hond", "Hoofd", "Hoera", "Hoog", "Hopen", "Hotel", "Huilen", "Ik", "Iemand", "IJs",
    "Jaar", "Jaloers", "Jarig", "Jas", "Jij", "Jongen", "Kapitein", "Kapot", "Kat", "Kerk",
    "Kerst", "Ketting", "Kip", "Klein", "Koe", "Koek", "Komen", "Kracht", "Krokodil", "Krom",
    "Kuiken", "Kunst", "Kus", "Laars", "Lach", "Lantaarnpaal", "Later", "Leeuw", "Leven", "Lezen",
    "Lichaam", "Liefde", "Lied", "Londen", "Loterij", "Luipaard", "Maan", "Mama", "Man", "Meisje",
    "Middernacht", "Miljoen", "Minuut", "Mond", "Mot", "Morgen", "Muur", "Nacht", "Nederland", "Nelson",
    "Nergens", "Neus", "Niemand", "Niets", "Nooit", "Nu", "Oceaan", "Ogen", "Oma", "Opa",
    "Onderbroek", "Opstaan", "Opzij", "Overal", "Oor", "Paard", "Paars", "Paella", "Pan", "Papegaai",
    "Paraplu", "Parijs", "Perfect", "Piano", "Pijn", "Plezier", "Poes", "Praten", "Put", "Radio",
    "Regen", "Regenboog", "Ridder", "Ritme", "Roeien", "Rood", "Rook", "Ruzie", "Schaap", "Schoen",
    "Schoonmaken", "School", "Schuld", "Seconde", "Skelet", "Sneeuw", "Snoep", "Spaghetti", "Spanje", "Spetter",
    "Spijt", "Spook", "Spons", "Springen", "Spruitjes", "Staan", "Stad", "Stem", "Sterren", "Stilte",
    "Storm", "Strand", "Stress", "Superheld", "Taal", "Tandarts", "Teen", "Thuis", "Tijd", "Toekomst",
    "Toeter", "Trap", "Troost", "Trui", "Tuin", "Twee", "Vakantie", "Vader", "Vallen", "Veranderen",
    "Vergeten", "Verhalen", "Verkopen", "Verlangen", "Vertrouwen", "Vlam", "Vliegtuig", "Vogel", "Voet", "Vrijheid",
    "Vragen", "Vrachtwagen", "Vriend", "Vuur", "Waarom", "Wacht", "Wakker", "Water", "Weinig", "Week",
    "Wereld", "Willen", "Winter", "Wit", "Woord", "Zeep", "Zeven", "Zicht", "Zien", "Ziek",
    "Zingen", "Zoek", "Zoeken", "Zomer", "Zon", "Zonnebril", "Zout", "Zus", "Zweet", "Zwemles"
]

# Streamlit-app
st.title("Het boermopper liedjes spel!")
st.write("Klik op de knop om een willekeurig woord te tonen!")

if st.button("Nieuw woord"):
    st.success(random.choice(woorden))
