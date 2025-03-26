"""Pre Prompt hook."""

import sys
import os

try:
    from cookieplone.utils import console

    HAS_COOKIEPLONE = True
except ModuleNotFoundError:
    HAS_COOKIEPLONE = False

# This fetches only the temporary folder
pwd=os.path.dirname(os.getcwd())

def main():
    """Check if we have cookieplone installed."""
    if not HAS_COOKIEPLONE:
        print("This template should be run with cookieplone")
        sys.exit(1)
    else:
        console.print_plone_banner()


PLONE_LOGOTYPE_BANNER = """
          *******                                                                        
      ***************                                                                    
    ***             ***        *********     ***                                     *** 
  ***    ***          ***      ***********   ***                                    * R *
 ***    *****          ***     ***      ***  ***                                     *** 
***      ***            ***    ***       *** ***       ****     ***  ***       ****      
***               ***   ***    ***      ***  ***     ********   *********    ********    
***              *****  ***    ***********   ***    ***    ***  ****   ***  ***    ***   
***      ***      ***   ***    *********     ***    ***    ***  ***    ***  **********   
 ***    *****          ***     ***           ***    ***    ***  ***    ***  *********    
  ***    ***          ***      ***           ****   ***    ***  ***    ***  ***    ...   
    ***             ***        ***            *****  ********   ***    ***   ********    
      ***************          ***              ***    ****     ***    ***     ****      
          *******                                                                        
"""

def print_plone_logotype_banner():
    """Print Plone Logotype banner."""
    style: str = "bold"
    color: str = "blue"
    console.print(PLONE_LOGOTYPE_BANNER, style, color)

def main():
    """Check context."""
    if not HAS_COOKIEPLONE:
        print("This template should be run with cookieplone")
        sys.exit(1)
    else:
        #console.print_plone_banner()
        print_plone_logotype_banner()
        console.print("the Cookieplone main tmp location:")
        console.print(pwd)

if __name__ == "__main__":
    main()
