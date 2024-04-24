from skeletons.FactionMultiApp import FactionMultiApp
from faction_pages.northern_french import *


class NorthernFrench(FactionMultiApp):
    def __init__(self):
        super().__init__(title="The Northern French", sidebar="expanded")
        super().run(["Overview", "Baldwin of Flanders", "Louis of Blois",
                     "Hugh of Saint-Pol", "Geoffrey of Vollehardouin",
                     "Henry of Flanders"], 393)

    def get_option(self, option):
        match option:
            case "Overview":
                Overview.app()
            case "Baldwin of Flanders":
                BaldwinFlanders.app()
            case "Louis of Blois":
                LouisBlois.app()
            case "Hugh of Saint-Pol":
                HughSaintPol.app()
            case "Geoffrey of Vollehardouin":
                GeoffreyVolleh.app()
            case "Henry of Flanders":
                HenryFlanders.app()


NorthernFrench()

