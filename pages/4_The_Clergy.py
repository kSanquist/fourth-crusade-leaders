from skeletons.FactionMultiApp import FactionMultiApp
from faction_pages.clergy import *


class NorthernFrench(FactionMultiApp):
    def __init__(self):
        super().__init__(title="The Clergy", sidebar="expanded")
        super().run(["Overview", "Conrad of Krosigk", "Martin of Pairis",
                                 "Nivelon de Quierzy", "Peter of Lucedio"], 393)

    def get_option(self, option):
        match option:
            case "Overview":
                Overview.app()
            case "Conrad of Krosigk":
                ConradHalberstadt.app()
            case "Martin of Pairis":
                MartinPairis.app()
            case "Nivelon de Quierzy":
                NivelonsSoissons.app()
            case "Peter of Lucedio":
                PeterLucedio.app()


NorthernFrench()

