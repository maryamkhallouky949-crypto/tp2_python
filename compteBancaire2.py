
class CompteBancaire:
    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : +{montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : -{montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde

    def afficher_operations(self):
        for operation in self._operations:
            print(operation)


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.compte = CompteBancaire()

    def afficher(self):
        print(
            f"Client : {self.nom}, "
            f"Solde : {self.compte.get_solde()} €"
        )


if __name__ == "__main__":
    cli = Client("maryam")

    cli.compte.deposer(200)
    cli.compte.retirer(30)

    cli.afficher()

    print("Historique des opérations :")
    cli.compte.afficher_operations()
