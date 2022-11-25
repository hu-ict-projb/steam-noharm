# Python heeft een aantal verschillende manieren om dingen op te splitsen

# De makkelijkste manier is een file
from analysis import lees_aantal_games, lees_gemiddelde_prijs_games
from gui import start
from bad_module.lastig import dut_niet_zo_goed

dut_niet_zo_goed()
boodschap = f'Er zijn {lees_aantal_games()} games, die gemiddeld {lees_gemiddelde_prijs_games()} euro kosten'
start(boodschap)
