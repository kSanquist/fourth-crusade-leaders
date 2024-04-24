from skeletons.FactionMultiApp import FactionMultiApp
from faction_pages.venetians import *


class NorthernFrench(FactionMultiApp):
    def __init__(self):
        super().__init__(title="The Venetians", sidebar="expanded")
        super().run(["Overview", "Enrico Dandolo", "Marino Zeno",
                     "Pietro Ziani"], 290)

    def get_option(self, option):
        match option:
            case "Overview":
                Overview.app()
            case "Enrico Dandolo":
                EnricoDandolo.app()
            case "Marino Zeno":
                MarinoZeno.app()
            case "Pietro Ziani":
                PietroZiani.app()


NorthernFrench()

