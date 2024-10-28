def boje(hex_color):
    # Uklanjamo znak '#' sa početka heksadekadnog zapisa
    hex_color = hex_color.lstrip('#')

    # Izdvajamo dva po dva karaktera za svaku boju i pretvaramo u dekadni sistem
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    # Pravljenje rečnika sa vrednostima za svaki kanal
    return {"Red": red, "Green": green, "Blue": blue}


# Testiranje funkcije
print(boje("#FA1AA0"))  # Očekivani izlaz: {'Red': 250, 'Green': 26, 'Blue': 160}

#drugi nacin
def boje(heksa):
    # Uzimamo po dva karaktera za svaki kanal i prevodimo iz heksadecimalnog u dekadni sistem
    red = int(heksa[1:3], 16)
    green = int(heksa[3:5], 16)
    blue = int(heksa[5:7], 16)

    # Vraćamo rečnik sa dekadnim vrednostima za svaki kanal
    return {"Red": red, "Green": green, "Blue": blue}


# Testiranje funkcije
print(boje("#FA1AA0"))
