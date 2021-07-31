def emptyLine(repeat): print("\n" * repeat)


# ┌─────┬─────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐

# │ id  │ name    │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │

# ├─────┼─────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤

# │ 0   │ main    │ default     │ 0.0.0   │ fork    │ 0        │ 0      │ 0    │ stopped   │ 0%       │ 0b       │ eloua    │ disabled │

# └─────┴─────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘


def listSorting(paramList = ["short", "long_example", "very_long_example"], decroissant = "Non"):


  sorted_list = sorted(paramList, key=len)


  print("Liste triée dans l'ordre de taille : \n- ", ", ".join(sorted_list))


  sorted_decroissant = []



  if decroissant == "Oui":


    i = 1

    while i < (len(sorted_list) + 1): 

      sorted_decroissant.append(sorted_list[len(sorted_list)-i])

      i += 1
    

    print("\n\nTri decroissant : \n- ", ", ".join(sorted_decroissant))




def execute():

  emptyLine(35)


  print("┌────────────────────────────── Consignes ────────────────────────────────────────────────┐")
  print("│                                                                                         │")

  print("│ Écrivez une liste des éléments à trier sous la forme \"element 1, element 2, element 3\". │")

  print("│ (séparés par une virgule et un espace)                                                  │")
  print("│                                                                                         │")

  print("├─────────────────────────────────────────────────────────────────────────────────────────┘")

  inputList = str(input("│ [ WRITE HERE ] : "))
  print("│")


  inputListSplited = inputList.split(", ")


  print("├────────────────────────────── Consignes ────────────────────────────────────────────────┐")
  print("│                                                                                         │")

  print("│ Voulez-vous les classer également dans l'ordre decroissant ?                            │")

  print("│ Répondre par Oui ou Non                                                                 │")
  print("│                                                                                         │")

  print("├─────────────────────────────────────────────────────────────────────────────────────────┘")

  decroissantOrNot = str(input("└ [ WRITE HERE ] : "))


  emptyLine(35)


  listSorting(inputListSplited, decroissantOrNot)


  emptyLine(7)


execute()
