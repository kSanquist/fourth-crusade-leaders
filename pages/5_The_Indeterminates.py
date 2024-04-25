from skeletons.FactionMultiApp import FactionMultiApp
from faction_pages.indeterminates import *


class Indeterminates(FactionMultiApp):
    def __init__(self):
        super().__init__(title="The Indeterminates", sidebar="expanded")
        super().run(["Overview", "Robert de Clari", "Theodore Branas",
                     "Othon de la Roche"], 330)

    def get_option(self, option):
        match option:
            case "Overview":
                Overview.app()
            case "Robert de Clari":
                RobertClari.app()
            case "Theodore Branas":
                TheodoreBranas.app()
            case "Othon de la Roche":
                OthonLaRoche.app()


Indeterminates()

