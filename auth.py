"""
* User Authentication Factory:
* 		Implement a UserAuthenticatorFactory that produces user authenticator objects based on security levels 
*        (Simple, Two-Factor, Biometric).
"""

class UserAuthenticatorFactory:
    def __init__(self):
        pass

    def createAuthenticator(self, securityLevel):
        if securityLevel == "Simple":
            return SimpleAuthenticator()
        elif securityLevel == "Two-Factor":
            return TwoFactorAuthenticator()
        elif securityLevel == "Biometric":
            return BiometricAuthenticator()
        else:
            return None

class SimpleAuthenticator(UserAuthenticatorFactory):

    def authenticate(self, username, password):
        print(f"Simple authentication for user {username} with password {password}")

class TwoFactorAuthenticator(UserAuthenticatorFactory):
    
    def authenticate(self, username, password):
        print(f"Two-Factor authentication for user {username} with password {password}")


class BiometricAuthenticator(UserAuthenticatorFactory):
    def authenticate(self, username, password):
        print(f"Biometric authentication for user {username} with password {password}")


def main():
    factory = UserAuthenticatorFactory()

    simpleAuthenticator = factory.createAuthenticator("Simple")
    twoFactorAuthenticator = factory.createAuthenticator("Two-Factor")
    biometricAuthenticator = factory.createAuthenticator("Biometric")

    authenticators = [simpleAuthenticator, twoFactorAuthenticator, biometricAuthenticator]
    for authenticator in authenticators:
        authenticator.authenticate("John", "123456")

if __name__ == "__main__":
    main()