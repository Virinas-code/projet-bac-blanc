from random import random
import names

nombres_etudiants = 100
n_periodes = 110
ratio = nombres_etudiants / n_periodes
periodes = ["" for _ in range(n_periodes)]

prof = []


class Etudiant:
    def __init__(self, nom: str, dispo: list, boul=False, jours=-1) -> None:
        self.nom = nom
        self.dispo = dispo
        self.b = boul
        self.jours = jours
        v = 0
        for i in range(n_periodes):
            if self.dispo[i] == True:
                v += 1
        self.valeur = v


def proba(P):
    return random() < P


def init(p_prof, p_etudiant1, p_etudiant2, ratio):
    prof = [proba(p_prof) for _ in range(n_periodes)]

    etudiants = []
    for _ in range(nombres_etudiants):
        nom = f"{names.get_first_name()} {names.get_last_name()}"
        if proba(ratio):
            etudiants.append(
                Etudiant(nom, [proba(p_etudiant1) for i in range(n_periodes)])
            )
        else:
            etudiants.append(
                Etudiant(nom, [proba(p_etudiant2) for i in range(n_periodes)])
            )
    return prof, etudiants


def etape1():
    for i in range(n_periodes):
        if prof[i] == False:
            for e in etudiants:
                e.dispo[i] = False
    return prof, etudiants


def valeur_periodes():
    v = [0 for _ in range(n_periodes)]
    for i in range(n_periodes):
        for e in etudiants:
            if e.dispo[i] == True and e.b == False:
                v[i] += 1
    return v


def valeur_etudiants():
    vi = n_periodes
    ef = etudiants[0]
    for e in etudiants:
        if e.valeur < vi and e.b == False:
            vi = e.valeur
            ef = e

    return ef


def comp(e: Etudiant):
    vi = nombres_etudiants
    ft = -1
    for t in range(n_periodes):
        z = e.dispo[t]

        if z == True and vp[t] <= vi:
            ft = t
            vi = vp[t]

    return ft


prof, etudiants = init(0.9, 0.8, 0.5, 0.70)
etape1()
ve = valeur_etudiants()
vp = valeur_periodes()


def main():
    global etudiants, vp  # Add this line to modify the global variable 'etudiants'
    for _ in range(nombres_etudiants):
        etape1()
        vp = valeur_periodes()
        ve = valeur_etudiants()

        ft = comp(ve)

        prof[ft] = False
        ve.b = True
        ve.jours = ft
        periodes[ft] = ve.nom
        etudiants = [
            e for e in etudiants if e.nom != ve.nom
        ]  # Update the list of students


main()
print(f"resultat final: {periodes}")
ok = 0
for i in range(n_periodes):
    if periodes[i]:
        ok += 1

print(f"Ratio de complétion: {ok/nombres_etudiants}")
