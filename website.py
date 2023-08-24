"""
* 		Website Theme Factory:
* 		Implement a WebsiteThemeFactory that generates website theme objects (Dark, Light, Minimal) for a user's choice.
"""

class WebsiteThemeFactory:
    def createTheme(self, themeType):
        if themeType == "Dark":
            return DarkTheme()
        elif themeType == "Light":
            return LightTheme()
        elif themeType == "Minimal":
            return MinimalTheme()
        else:
            return None

class DarkTheme:
    def getTheme(self):
        print("Dark Theme")

class LightTheme:
    def getTheme(self):
        print("Light Theme")

class MinimalTheme:
    def getTheme(self):
        print("Minimal Theme")

def main():
    factory = WebsiteThemeFactory()

    darkTheme = factory.createTheme("Dark")
    lightTheme = factory.createTheme("Light")
    minimalTheme = factory.createTheme("Minimal")

    themes = [darkTheme, lightTheme, minimalTheme]
    for theme in themes:
        theme.getTheme()

if __name__ == "__main__":
    main()