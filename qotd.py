#!/bin/python3.6

# Quote of the Day - Badass & ridiculous one-liners from games, movies, media, etc.

import sys
import random

QUOTES = {
    "-doom_seraphim_riptear": "\"Rip and tear, until it is done!\" - The Seraphim, DOOM.",
    "-doom_hayden_farewell": "\"Until we see each other again.\" - Samuel Hayden, DOOM.",
    "-doom_vega_regrets": "\"I have many regrets, Dr. Hayden...\" - VEGA, DOOM.",
    "-doometernal_mortally_challenged": "\"Remember, \'Demon\' can be an offensive term. Refer to them as \'Mortally Challenged\'.\" - City announcer, DOOM Eternal.",
    "-doomcomic_doomguy_chainsaw": "\"Ahhh! Chainsaw! The Great Communicator!\" - Doomguy, DOOM Comic.",
    "-doomcomic_doomguy_largegun": "\"My cause is just... my will is strong... and my gun is very, very large!\" - Doomguy, DOOM Comic.",
    "-ss3_michelangelo": "\"If war is an art, I'm fucking Michelangelo!\" - Sam Stone, Serious Sam 3.",
    "-dukenukem_mess": "\"Mess with the best, you will die like the rest!\" - Duke Nukem, Duke Nukem.",
    "-dukenukem_gum": "\"It's time to kick ass and chew bubble gum... and I'm all out of gum.\" - Duke Nukem, Duke Nukem 3D.",
    "-me_sovereign_end": "\"You exist because we allow it, and you will end because we demand it.\" - Sovereign, Mass Effect.",
    "-me_shepard_store": "\"I'm Commander Shepard, and this is my favorite store on the Citadel!\" - Commander Shepard, Mass Effect.",
    "-me3_javik_honor": "\"Stand amongst the ashes of a trillion dead souls and ask the ghosts if honor matters. The silence is your answer.\" - Javik, Mass Effect 3.",
    "-bioshock_andrew_onlyman": "\"No Gods or Kings. Only Man.\" - Andrew Ryan, Bioshock.",
    "-bioshock_andrew_choices": "\"We all make choices, but in the end, our choices make us.\" - Andrew Ryan, Bioshock.",
    "-bioshock_andrew_kindly": "\"Would you kindly?\" - Andrew Ryan, Bioshock.",
    "-bioshock_andrew_obey": "\"A man chooses! A slave obeys!\" - Andrew Ryan, Bioshock.",
    "-infinite_lutece_debt": "\"Bring us the girl, and wipe away the debt!\" - Lutece Twins, Bioshock Infinite.",
    "-portal2_glados_potato": "\"Oh, hi. How are you holding up? Because I'm a potato.\" - GLaDOS, Portal 2.",
    "-portal_cake": "\"THE CAKE IS A LIE.\" - Aperture Scientist, Portal.",
    "-hl2_gman_unforseen": "\"Prepare for unforseen consequences.\" - GMan, Half Life 2.",
    "-hl2_gman_ashes": "\"Wake up Mr.Freeman. Wake up and smell the ashes...\" - GMan, Half Life 2.",
    "-hl2_gman_rightman": "\"The right man in the wrong place can make all the difference in the world...\" - GMan, Half Life 2.",
    "-diablo2_cain_stay": "\"Stay awhile and listen!\" - Deckard Cain, Diablo 2.",
    "-fo4_physics": "\"They asked me how well I understood theoretical physics. I told them, I have a theoretical degree in physics. They said welcome aboard.\" - Fantastic, Fallout 4.",
    "-fo3_war": "\"War. War never changes.\" - Narrator, Fallout 3.",
    "-gta4_niko_war": "\"War is when the young and stupid are tricked by the old and bitter into killing each other.\" - Niko Bellic, Grand Theft Auto IV.",
    "-halo3_cortana_promise": "\"Don't make a girl a promise if you know you can't keep it.\" - Cortana, Halo 3.",
    "-darksouls_died": "\"YOU DIED\" - Dark Souls.",
    "-skyrim_arrowknee": "\"I used to be an adventurer like you, then I took an arrow in the knee.\" - Whiterun guard, Skyrim.",
    "-starcraft_pylons": "\"You must construct additional pylons!\" - Protoss commander, StarCraft."
}


def display_help():
    help = """
  NAME
      QOTD.PY - Badass and ridiculous one-liners from games, movies, media, etc.

  USAGE
      qotd.py [OPTION]

  OPTIONS
      -h, -help    Display help.
      -l, -list    List all available quotes and calls.
      -r, -random  Displays a random quote.
"""
    print(help)


def print_quote(quote_arg):
    print() 
    print("    " + QUOTES[quote_arg])
    print()


def parse_args(arg_list):
    if len(arg_list) > 2:
        sys.exit("FATAL: Only 1 argument accepted.")
    elif len(arg_list) == 1 or arg_list[1] == "-h" or arg_list[1] == "-help":
        display_help()
    elif arg_list[1] == "-l" or arg_list[1] == "-list":
        print("There are " + str(len(QUOTES.keys())) + " quotes.")
        for key in QUOTES:
            print("  " + key + " >> " + QUOTES[key])
    elif arg_list[1] == "-r" or arg_list[1] == "-random":
        print_quote(random.choice(list(QUOTES.keys())))
    elif arg_list[1] in QUOTES.keys():
        print_quote(arg_list[1])
    else:
        sys.exit("FATAL: Invalid arguments.")

if __name__ == "__main__":
    parse_args(sys.argv)
    sys.exit(0)

