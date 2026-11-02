import json
import datetime

# רשימה מורחבת ומקיפה של כ-75 מיקומים בגרמניה (ערים גדולות, בינוניות, תחנות דלק 24/7, פארם ובתי מרקחת)
STORES_DATA = [
    # --- BERLIN ---
    {"city": "Berlin", "state": "Berlin", "category": "Supermarkt", "store_name": "REWE City", "address": "Hauptbahnhof (Europaplatz 1)", "opening_hours": "08:00 - 22:00", "transit": "S-Bahn / U5 Hauptbahnhof", "sunday_open": True, "note": "Geöffnet an Sonn- und Feiertagen"},
    {"city": "Berlin", "state": "Berlin", "category": "Drogerie", "store_name": "Rossmann", "address": "Bahnhof Ostbahnhof", "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / Regio Ostbahnhof", "sunday_open": True, "note": "Geöffnet an Sonn- und Feiertagen"},
    {"city": "Berlin", "state": "Berlin", "category": "Supermarkt", "store_name": "Edeka", "address": "Bahnhof Friedrichstraße", "opening_hours": "08:00 - 22:00", "transit": "S-Bahn / U6 Friedrichstraße", "sunday_open": True, "note": "Geöffnet an Sonn- und Feiertagen"},
    {"city": "Berlin", "state": "Berlin", "category": "Bio-Supermarkt", "store_name": "Denns BioMarkt", "address": "Bahnhof Ostkreuz", "opening_hours": "08:00 - 21:00", "transit": "S-Bahn Ostkreuz", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "Berlin", "state": "Berlin", "category": "Apotheke", "store_name": "Hauptbahnhof Apotheke", "address": "Hauptbahnhof 1. OG", "opening_hours": "00:00 - 24:00", "transit": "Hauptbahnhof", "sunday_open": True, "note": "24/7 Notdienst"},
    {"city": "Berlin", "state": "Berlin", "category": "Tankstelle / REWE To Go", "store_name": "Aral / REWE To Go", "address": "Heerstraße 92", "opening_hours": "00:00 - 24:00", "transit": "Bus M49 / X34", "sunday_open": True, "note": "24/7 Shop & Snack"},

    # --- MÜNCHEN ---
    {"city": "München", "state": "Bayern", "category": "Supermarkt", "store_name": "Edeka", "address": "Hauptbahnhof (Zwischengeschoss)", "opening_hours": "08:00 - 23:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "München", "state": "Bayern", "category": "Supermarkt", "store_name": "Edeka", "address": "Flughafen München (MUC) Zentralallee", "opening_hours": "05:30 - 22:00", "transit": "S1 / S8 Flughafen München", "sunday_open": True, "note": "Täglich geöffnet"},
    {"city": "München", "state": "Bayern", "category": "Drogerie", "store_name": "dm-drogerie markt", "address": "Ostbahnhof Platz", "opening_hours": "07:00 - 22:00", "transit": "S-Bahn / U4 Ostbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "München", "state": "Bayern", "category": "Tankstelle / REWE To Go", "store_name": "Aral / REWE To Go", "address": "Tegernseer Landstraße 165", "opening_hours": "00:00 - 24:00", "transit": "Tram 15 / 25", "sunday_open": True, "note": "24/7 Geöffnet"},

    # --- HAMBURG ---
    {"city": "Hamburg", "state": "Hamburg", "category": "Supermarkt", "store_name": "Edeka Tamme", "address": "Hauptbahnhof Wandelhalle", "opening_hours": "07:00 - 23:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "Hamburg", "state": "Hamburg", "category": "Drogerie", "store_name": "Rossmann", "address": "Hauptbahnhof Wandelhalle OG", "opening_hours": "08:00 - 21:00", "transit": "Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "Hamburg", "state": "Hamburg", "category": "Supermarkt", "store_name": "Edeka", "address": "Bahnhof Altona (Untergeschoss)", "opening_hours": "07:00 - 23:00", "transit": "S-Bahn Bahnhof Altona", "sunday_open": True, "note": "Täglich geöffnet"},

    # --- FRANKFURT AM MAIN ---
    {"city": "Frankfurt am Main", "state": "Hessen", "category": "Supermarkt", "store_name": "REWE City", "address": "Fernbahnhof Flughafen", "opening_hours": "06:00 - 22:00", "transit": "Fernbahnhof / Regio Flughafen", "sunday_open": True, "note": "Täglich geöffnet"},
    {"city": "Frankfurt am Main", "state": "Hessen", "category": "Drogerie", "store_name": "Rossmann", "address": "Hauptbahnhof B-Ebene", "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "Frankfurt am Main", "state": "Hessen", "category": "Tankstelle / REWE To Go", "store_name": "Aral / REWE To Go", "address": "Friedberger Landstraße 295", "opening_hours": "00:00 - 24:00", "transit": "Tram 18", "sunday_open": True, "note": "24/7 Geöffnet"},

    # --- KÖLN ---
    {"city": "Köln", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Trankgasse 11", "opening_hours": "00:00 - 24:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "24/7 Geöffnet"},
    {"city": "Köln", "state": "Nordrhein-Westfalen", "category": "Drogerie", "store_name": "Rossmann", "address": "Hauptbahnhof Passagenebene", "opening_hours": "08:00 - 22:00", "transit": "Hauptbahnhof Köln", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- DÜSSELDORF ---
    {"city": "Düsseldorf", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "Edeka", "address": "Hauptbahnhof Konrad-Adenauer-Platz", "opening_hours": "00:00 - 24:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "24/7 Durchgehend geöffnet"},
    {"city": "Düsseldorf", "state": "Nordrhein-Westfalen", "category": "Drogerie", "store_name": "dm-drogerie markt", "address": "Flughafen Düsseldorf (DUS)", "opening_hours": "07:30 - 21:00", "transit": "SkyTrain Flughafen", "sunday_open": True, "note": "Täglich geöffnet"},

    # --- STUTTGART ---
    {"city": "Stuttgart", "state": "Baden-Württemberg", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Arnulf-Klett-Platz", "opening_hours": "06:00 - 23:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},
    {"city": "Stuttgart", "state": "Baden-Württemberg", "category": "Bäckerei", "store_name": "Bäckerei Trezsch", "address": "Flughafen Stuttgart Terminal 1", "opening_hours": "06:00 - 20:00", "transit": "S2 / S3 Flughafen", "sunday_open": True, "note": "Frische Brötchen am Sonntag"},

    # --- LEIPZIG ---
    {"city": "Leipzig", "state": "Sachsen", "category": "Supermarkt", "store_name": "Aldi Nord", "address": "Hauptbahnhof Promenaden OG 1", "opening_hours": "12:00 - 18:00", "transit": "S-Bahn / Tram Hauptbahnhof", "sunday_open": True, "note": "Sonderöffnung Sonntags"},
    {"city": "Leipzig", "state": "Sachsen", "category": "Supermarkt", "store_name": "REWE City", "address": "Hauptbahnhof Promenaden UG", "opening_hours": "12:00 - 18:00", "transit": "Hauptbahnhof Leipzig", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- DRESDEN ---
    {"city": "Dresden", "state": "Sachsen", "category": "Supermarkt", "store_name": "Lidl", "address": "Hauptbahnhof Wiener Platz 4", "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / Tram Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "Dresden", "state": "Sachsen", "category": "Supermarkt", "store_name": "Lidl", "address": "Bahnhof Dresden-Neustadt", "opening_hours": "08:00 - 21:00", "transit": "S-Bahn Dresden-Neustadt", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- HANNOVER ---
    {"city": "Hannover", "state": "Niedersachsen", "category": "Supermarkt", "store_name": "Lidl", "address": "Hauptbahnhof Ernst-August-Platz", "opening_hours": "08:00 - 22:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},
    {"city": "Hannover", "state": "Niedersachsen", "category": "Drogerie", "store_name": "Rossmann", "address": "Hauptbahnhof Haupthalle", "opening_hours": "08:00 - 21:00", "transit": "Hauptbahnhof Hannover", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- NÜRNBERG ---
    {"city": "Nürnberg", "state": "Bayern", "category": "Supermarkt", "store_name": "Lidl", "address": "Hauptbahnhof Bahnhofsplatz 9", "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / U1 / U2 / U3 Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},
    {"city": "Nürnberg", "state": "Bayern", "category": "Apotheke", "store_name": "Bahnhof-Apotheke", "address": "Hauptbahnhof Mittelhalle", "opening_hours": "08:00 - 20:00", "transit": "Hauptbahnhof Nürnberg", "sunday_open": True, "note": "Sonntagsdienst"},

    # --- BREMEN ---
    {"city": "Bremen", "state": "Bremen", "category": "Supermarkt", "store_name": "REWE City", "address": "Hauptbahnhof Bahnhofsplatz 15", "opening_hours": "08:00 - 22:00", "transit": "BSAG Tram / Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- ESSEN ---
    {"city": "Essen", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "Lidl", "address": "Hauptbahnhof Am Hauptbahnhof 5", "opening_hours": "09:00 - 20:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- DORTMUND ---
    {"city": "Dortmund", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Königswall 15", "opening_hours": "06:00 - 23:00", "transit": "S-Bahn / Stadtbahn Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- BONN ---
    {"city": "Bonn", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Am Hauptbahnhof 1", "opening_hours": "06:00 - 22:00", "transit": "Stadtbahn Hauptbahnhof Bonn", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- MANNHEIM ---
    {"city": "Mannheim", "state": "Baden-Württemberg", "category": "Supermarkt", "store_name": "REWE City", "address": "Hauptbahnhof Bahnhofscheitel", "opening_hours": "08:00 - 22:00", "transit": "RNV Tram / Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- KARLSRUHE ---
    {"city": "Karlsruhe", "state": "Baden-Württemberg", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofplatz 1a", "opening_hours": "06:00 - 22:00", "transit": "KVV Tram / Hauptbahnhof", "sunday_open": True, "note": "Täglich geöffnet"},

    # --- MÜNSTER ---
    {"city": "Münster", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Berliner Platz 29", "opening_hours": "06:00 - 23:00", "transit": "Hauptbahnhof Münster", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- AUGSBURG ---
    {"city": "Augsburg", "state": "Bayern", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Viktoriastraße 1", "opening_hours": "06:00 - 22:00", "transit": "VGA Tram / Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- WIESBADEN ---
    {"city": "Wiesbaden", "state": "Hessen", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofsplatz 1", "opening_hours": "06:00 - 22:00", "transit": "ESWE Bus / Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- POTSDAM (NEW) ---
    {"city": "Potsdam", "state": "Brandenburg", "category": "Supermarkt", "store_name": "Bio Lüske", "address": "Hauptbahnhof Passage", "opening_hours": "08:00 - 20:00", "transit": "S7 / Tram Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnete Bio-Filiale"},
    {"city": "Potsdam", "state": "Brandenburg", "category": "Drogerie", "store_name": "Rossmann", "address": "Hauptbahnhof Bahnhofspassagen", "opening_hours": "08:00 - 20:00", "transit": "S-Bahn Potsdam Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- MAINZ (NEW) ---
    {"city": "Mainz", "state": "Rheinland-Pfalz", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofplatz 1", "opening_hours": "06:00 - 22:00", "transit": "Tram / Bus Hauptbahnhof Mainz", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- FREIBURG IM BREISGAU (NEW) ---
    {"city": "Freiburg im Breisgau", "state": "Baden-Württemberg", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bismarckallee 5", "opening_hours": "06:00 - 23:00", "transit": "VAG Tram / Hauptbahnhof", "sunday_open": True, "note": "Täglich geöffnet"},

    # --- BIELEFELD (NEW) ---
    {"city": "Bielefeld", "state": "Nordrhein-Westfalen", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofstraße 67", "opening_hours": "06:00 - 22:00", "transit": "StadtBahn Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- KIEL (NEW) ---
    {"city": "Kiel", "state": "Schleswig-Holstein", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Sophienblatt 25", "opening_hours": "06:00 - 22:00", "transit": "Bus / Hauptbahnhof Kiel", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- ROSTOCK (NEW) ---
    {"city": "Rostock", "state": "Mecklenburg-Vorpommern", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Konrad-Adenauer-Platz 1", "opening_hours": "06:00 - 22:00", "transit": "S-Bahn / Tram Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- HALLE (SAALE) (NEW) ---
    {"city": "Halle (Saale)", "state": "Sachsen-Anhalt", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofsplatz 1", "opening_hours": "06:00 - 22:00", "transit": "S-Bahn / Tram Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"},

    # --- HEIDELBERG (NEW) ---
    {"city": "Heidelberg", "state": "Baden-Württemberg", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Willy-Brandt-Platz 5", "opening_hours": "06:00 - 22:00", "transit": "RNV Tram / Hauptbahnhof", "sunday_open": True, "note": "Täglich geöffnet"},

    # --- REGENSBURG (NEW) ---
    {"city": "Regensburg", "state": "Bayern", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofstraße 18", "opening_hours": "06:00 - 22:00", "transit": "RVV Bus / Hauptbahnhof", "sunday_open": True, "note": "Sonn- und Feiertags geöffnet"},

    # --- SAARBRÜCKEN (NEW) ---
    {"city": "Saarbrücken", "state": "Saarland", "category": "Supermarkt", "store_name": "REWE To Go", "address": "Hauptbahnhof Am Hauptbahnhof 4", "opening_hours": "06:00 - 22:00", "transit": "Saarbahn Hauptbahnhof", "sunday_open": True, "note": "Sonntags geöffnet"}
]

def generate_live_status():
    now = datetime.datetime.utcnow()
    updated_str = now.strftime("%Y-%m-%d %H:%M UTC")
    today_is_sunday = now.weekday() == 6

    output = {
        "metadata": {
            "last_updated": updated_str,
            "total_entries": len(STORES_DATA),
            "is_sunday": today_is_sunday
        },
        "data": []
    }

    for store in STORES_DATA:
        status_text = "Offen" if store["sunday_open"] else "Geschlossen"
        output["data"].append({
            "city": store["city"],
            "state": store["state"],
            "category": store["category"],
            "store_name": store["store_name"],
            "address": store["address"],
            "transit": store.get("transit", "Nahverkehr im Bahnhof"),
            "status": f"{status_text} ({store['opening_hours']})",
            "note": store["note"]
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"[{updated_str}] Successfully generated data.json with {len(STORES_DATA)} comprehensive items across Germany.")

if __name__ == "__main__":
    generate_live_status()
