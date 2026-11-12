
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : +{montant} €")
            print("Dépôt effectué avec succès.")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : -{montant} €")
            print("Retrait effectué avec succès.")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def afficher_operations(self):
        for operation in self._operations:
            print(operation)

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)

    compte.deposer(200)
    compte.retirer(150)

    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    print("\nHistorique des opérations :")
    compte.afficher_operations()
    compte.solde = 600
