import streamlit as st
import keras
import numpy as np
from keras.models import load_model

# model = pickle.load(open("model.pkl",'rb'))
model = load_model("model-lstm.h5")
heroes = {'Choose': 0, 'Anti-Mage': 1, 'Axe': 2, 'Bane': 3, 'Bloodseeker': 4, 'Crystal Maiden': 5, 'Drow Ranger': 6, 'Earthshaker': 7, 'Juggernaut': 8, 'Mirana': 9, 'Morphling': 10, 'Shadow Fiend': 11, 'Phantom Lancer': 12, 'Puck': 13, 'Pudge': 14, 'Razor': 15, 'Sand King': 16, 'Storm Spirit': 17, 'Sven': 18, 'Tiny': 19, 'Vengeful Spirit': 20, 'Windranger': 21, 'Zeus': 22, 'Kunkka': 23, 'Lina': 25, 'Lion': 26, 'Shadow Shaman': 27, 'Slardar': 28, 'Tidehunter': 29, 'Witch Doctor': 30, 'Lich': 31, 'Riki': 32, 'Enigma': 33, 'Tinker': 34, 'Sniper': 35, 'Necrophos': 36, 'Warlock': 37, 'Beastmaster': 38, 'Queen of Pain': 39, 'Venomancer': 40, 'Faceless Void': 41, 'Wraith King': 42, 'Death Prophet': 43, 'Phantom Assassin': 44, 'Pugna': 45, 'Templar Assassin': 46, 'Viper': 47, 'Luna': 48, 'Dragon Knight': 49, 'Dazzle': 50, 'Clockwerk': 51, 'Leshrac': 52, "Nature's Prophet": 53, 'Lifestealer': 54, 'Dark Seer': 55, 'Clinkz': 56, 'Omniknight': 57, 'Enchantress': 58, 'Huskar': 59, 'Night Stalker': 60, 'Broodmother': 61, 'Bounty Hunter': 62, 'Weaver': 63, 'Jakiro': 64, 'Batrider': 65, 'Chen': 66, 'Spectre': 67, 'Ancient Apparition': 68, 'Doom': 69, 'Ursa': 70, 'Spirit Breaker': 71, 'Gyrocopter': 72, 'Alchemist': 73, 'Invoker': 74, 'Silencer': 75, 'Outworld Destroyer': 76, 'Lycan': 77, 'Brewmaster': 78, 'Shadow Demon': 79, 'Lone Druid': 80, 'Chaos Knight': 81, 'Meepo': 82, 'Treant Protector': 83, 'Ogre Magi': 84, 'Undying': 85, 'Rubick': 86, 'Disruptor': 87, 'Nyx Assassin': 88, 'Naga Siren': 89, 'Keeper of the Light': 90, 'Io': 91, 'Visage': 92, 'Slark': 93, 'Medusa': 94, 'Troll Warlord': 95, 'Centaur Warrunner': 96, 'Magnus': 97, 'Timbersaw': 98, 'Bristleback': 99, 'Tusk': 100, 'Skywrath Mage': 101, 'Abaddon': 102, 'Elder Titan': 103, 'Legion Commander': 104, 'Techies': 105, 'Ember Spirit': 106, 'Earth Spirit': 107, 'Underlord': 108, 'Terrorblade': 109, 'Phoenix': 110, 'Oracle': 111, 'Winter Wyvern': 112, 'Arc Warden': 113, 'Monkey King': 114, 'Dark Willow': 119, 'Pangolier': 120, 'Grimstroke': 121, 'Hoodwink': 123, 'Void Spirit': 126, 'Snapfire': 128, 'Mars': 129, 'Dawnbreaker': 135, 'Marci': 136, 'Primal Beast': 137}

data = {
    "Duration": 0,
    "rad_hero1_id": 0,"rad_hero1_kills": 0,"rad_hero1_deaths": 0,"rad_hero1_assists": 0,
    "rad_hero2_id": 0,"rad_hero2_kills": 0,"rad_hero2_deaths": 0,"rad_hero2_assists": 0,
    "rad_hero3_id": 0,"rad_hero3_kills": 0,"rad_hero3_deaths": 0,"rad_hero3_assists": 0,
    "rad_hero4_id": 0,"rad_hero4_kills": 0,"rad_hero4_deaths": 0,"rad_hero4_assists": 0,
    "rad_hero5_id": 0,"rad_hero5_kills": 0,"rad_hero5_deaths": 0,"rad_hero5_assists": 0,
    "dir_hero1_id": 0,"dir_hero1_kills": 0,"dir_hero1_deaths": 0,"dir_hero1_assists": 0,
    "dir_hero2_id": 0,"dir_hero2_kills": 0,"dir_hero2_deaths": 0,"dir_hero2_assists": 0,
    "dir_hero3_id": 0,"dir_hero3_kills": 0,"dir_hero3_deaths": 0,"dir_hero3_assists": 0,
    "dir_hero4_id": 0,"dir_hero4_kills": 0,"dir_hero4_deaths": 0,"dir_hero4_assists": 0,
    "dir_hero5_id": 0,"dir_hero5_kills": 0,"dir_hero5_deaths": 0,"dir_hero5_assists": 0,
}
st.set_page_config(page_title="DOTA2 Winner Prediction", page_icon="icon.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.header("Radiant Team")

col1, scol1, scol2, scol3 = st.columns([1,1,1,1])
with col1:
    rad_hero1 = st.selectbox("Hero 1", heroes, key=11)
    rad_hero2 = st.selectbox("Hero 2", heroes, key=12)
    rad_hero3 = st.selectbox("Hero 3", heroes, key=13)
    rad_hero4 = st.selectbox("Hero 4", heroes, key=14)
    rad_hero5 = st.selectbox("Hero 5", heroes, key=15)

    data['rad_hero1_id'] = heroes[rad_hero1]
    data['rad_hero2_id'] = heroes[rad_hero2]
    data['rad_hero3_id'] = heroes[rad_hero3]
    data['rad_hero4_id'] = heroes[rad_hero4]
    data['rad_hero5_id'] = heroes[rad_hero5]

with scol1:
    data['rad_hero1_kills'] = st.number_input("Kills", key=11, min_value=0, max_value=None, step=1)
    data['rad_hero2_kills'] = st.number_input("Kills", key=12, min_value=0, max_value=None, step=1)
    data['rad_hero3_kills'] = st.number_input("Kills", key=13, min_value=0, max_value=None, step=1)
    data['rad_hero4_kills'] = st.number_input("Kills", key=14, min_value=0, max_value=None, step=1)
    data['rad_hero5_kills'] = st.number_input("Kills", key=15, min_value=0, max_value=None, step=1)
with scol2:
    data['rad_hero1_deaths'] = st.number_input("Deaths", key=21, min_value=0, max_value=None, step=1)
    data['rad_hero2_deaths'] = st.number_input("Deaths", key=22, min_value=0, max_value=None, step=1)
    data['rad_hero3_deaths'] = st.number_input("Deaths", key=23, min_value=0, max_value=None, step=1)
    data['rad_hero4_deaths'] = st.number_input("Deaths", key=24, min_value=0, max_value=None, step=1)
    data['rad_hero5_deaths'] = st.number_input("Deaths", key=25, min_value=0, max_value=None, step=1)
with scol3:
    data['rad_hero1_assists'] = st.number_input("Assists", key=31, min_value=0, max_value=None, step=1)
    data['rad_hero2_assists'] = st.number_input("Assists", key=32, min_value=0, max_value=None, step=1)
    data['rad_hero3_assists'] = st.number_input("Assists", key=33, min_value=0, max_value=None, step=1)
    data['rad_hero4_assists'] = st.number_input("Assists", key=34, min_value=0, max_value=None, step=1)
    data['rad_hero5_assists'] = st.number_input("Assists", key=35, min_value=0, max_value=None, step=1)


st.header("Dire Team")

col1, scol1, scol2, scol3 = st.columns([1,1,1,1])
with col1:
    dir_hero1 = st.selectbox("Hero 1", heroes, key=21)
    dir_hero2 = st.selectbox("Hero 2", heroes, key=22)
    dir_hero3 = st.selectbox("Hero 3", heroes, key=23)
    dir_hero4 = st.selectbox("Hero 4", heroes, key=24)
    dir_hero5 = st.selectbox("Hero 5", heroes, key=25)

    data['dir_hero1_id'] = heroes[dir_hero1]
    data['dir_hero2_id'] = heroes[dir_hero2]
    data['dir_hero3_id'] = heroes[dir_hero3]
    data['dir_hero4_id'] = heroes[dir_hero4]
    data['dir_hero5_id'] = heroes[dir_hero5]

with scol1:
    data['dir_hero1_kills'] = st.number_input("Kills", key=41, min_value=0, max_value=None, step=1)
    data['dir_hero2_kills'] = st.number_input("Kills", key=42, min_value=0, max_value=None, step=1)
    data['dir_hero3_kills'] = st.number_input("Kills", key=43, min_value=0, max_value=None, step=1)
    data['dir_hero4_kills'] = st.number_input("Kills", key=44, min_value=0, max_value=None, step=1)
    data['dir_hero5_kills'] = st.number_input("Kills", key=45, min_value=0, max_value=None, step=1)
with scol2:
    data['dir_hero1_deaths'] = st.number_input("Deaths", key=51, min_value=0, max_value=None, step=1)
    data['dir_hero2_deaths'] = st.number_input("Deaths", key=52, min_value=0, max_value=None, step=1)
    data['dir_hero3_deaths'] = st.number_input("Deaths", key=53, min_value=0, max_value=None, step=1)
    data['dir_hero4_deaths'] = st.number_input("Deaths", key=54, min_value=0, max_value=None, step=1)
    data['dir_hero5_deaths'] = st.number_input("Deaths", key=55, min_value=0, max_value=None, step=1)
with scol3:
    data['dir_hero1_assists'] = st.number_input("Assists", key=61, min_value=0, max_value=None, step=1)
    data['dir_hero2_assists'] = st.number_input("Assists", key=62, min_value=0, max_value=None, step=1)
    data['dir_hero3_assists'] = st.number_input("Assists", key=63, min_value=0, max_value=None, step=1)
    data['dir_hero4_assists'] = st.number_input("Assists", key=64, min_value=0, max_value=None, step=1)
    data['dir_hero5_assists'] = st.number_input("Assists", key=65, min_value=0, max_value=None, step=1)

dur =  st.slider('Match Duration (Mins)', 20, 80, 30)
data['Duration'] = dur * 60

def predictor():
    winner = "(Not Predicted)"
    x = np.array(list(data.values())).reshape(-1,1,41)
    y_pred = model.predict(x)
    winner = "Radiant" if int(y_pred[0]) == 0 else "Dire"

    st.sidebar.success(f"Predicted Winner: {winner}")
    

st.button("PREDICT WINNER", on_click=predictor)

st.sidebar.title("Dota 2 Match Prediction")
st.sidebar.write("""
With the rapid development of e-sports, games are now using machine learning techniques in several scopes of application. One of the most important applications of game is insights over winner and predictions. In this work, we used the match stats data of kills-deaths-assists along with the match duration and the heroes to predict the winner of a game based on a stacked Bi-LSTM model. The data of the matches to train the model, were collected from OpenDota API.
""")


st.warning("This application is made with streamlit, and not UI compatible with Mobile views. Please try with a Desktop view.")