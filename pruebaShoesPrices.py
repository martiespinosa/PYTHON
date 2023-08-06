print("\n1. Dunk SB St. Patrick's Day\n2. Dunk SB Blue Raspberry\n3. Jordan 1 Chicago Lost & Found\n4. Jordan 4 Fossil\n5. Dunk Graffiti Pink\n6. Vans Imran Potato\n7. Air Force 1 Nocta CLB\n8. Air Force 1 Supreme\n9. Kobe Crazy 1 Stormtrooper\n10. Foam RNNR Ochre\n11. Foam RNNR Onyx\n12. Foam RNNR Sand")

num = input("\nEntra el número de la zapatilla para ver detalles de ella: ")

miDiccionario = {"1":"NikeDunkSBStPatricksDay", "2":"NikeDunkSBBlueRaspberry", "3":"Jordan1ChicagoLost&Found", "4":"Jordan4Fossil", "5":"DunkGraffitiPink", "6":"VansImranPotato", "7":"AirForce1NoctaCLB", "8":"AirForce1Supreme", "9":"KobeCrazy1Stormtrooper", "10":"FoamRNNROchre", "11":"FoamRNNROnyx", "12":"FoamRNNRSand"}

miDiccionarioRetail = {"NikeDunkSBStPatricksDay":110, "NikeDunkSBBlueRaspberry":110, "Jordan1ChicagoLost&Found":180, "Jordan4Fossil":190, "DunkGraffitiPink":110, "VansImranPotato":140, "AirForce1NoctaCLB":140, "AirForce1Supreme":128, "KobeCrazy1Stormtrooper":150, "FoamRNNROchre":90, "FoamRNNROnyx":90, "FoamRNNRSand": 90}

miDiccionarioResell = {"NikeDunkSBStPatricksDay":142, "NikeDunkSBBlueRaspberry":240, "Jordan1ChicagoLost&Found":372, "Jordan4Fossil":416, "DunkGraffitiPink":85, "VansImranPotato":232, "AirForce1NoctaCLB":184, "AirForce1Supreme":141, "KobeCrazy1Stormtrooper":95, "FoamRNNROchre":189, "FoamRNNROnyx":242, "FoamRNNRSand":263}

shoe = miDiccionario.get(num)

print("\nRetail:", miDiccionarioRetail.get(shoe))
print("Resell:", miDiccionarioResell.get(shoe),"\n")