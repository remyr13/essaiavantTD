"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.console import Console
from rich.markdown import Markdown


def moyenne(valeurs):
    # docstrings en markdown
    """
    # Calcule la moyenne des valeurs.

    **Paramètres**
    - `valeurs` : valeurs dont on veut calculer la moyenne

    **Retour**
    - la moyenne des valeurs

    **Exceptions**
    - `ValueError` : si la liste est vide

    ---
    """
    if len(valeurs) == 0 : raise ValueError
    s = 0
    for v in valeurs:
        s+=v

    return(s/len(valeurs))


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
