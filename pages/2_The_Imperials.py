from skeletons.FactionMultiApp import FactionMultiApp
from faction_pages.imperials import *


class NorthernFrench(FactionMultiApp):
    def __init__(self):
        super().__init__(title="The Imperials", sidebar="expanded")
        super().run(["Overview", "Boniface I of Montferrat",
                     "Oberto II of Biandrate", "Berthold II von Katzenelnbogen"], 393)

    def get_option(self, option):
        match option:
            case "Overview":
                Overview.app()
            case "Boniface I of Montferrat":
                BonifaceMont.app()
            case "Oberto II of Biandrate":
                ObertoBiandrate.app()
            case "Berthold II von Katzenelnbogen":
                BertholdKatz.app()


NorthernFrench()

