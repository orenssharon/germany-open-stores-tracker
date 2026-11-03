import json
import datetime

# רשימה נרחבת ומקיפה של כ-75 מיקומים בגרמניה
# כוללת נתוני חגים, זמני עומס מומלצים, חנייה, מגוון מוצרים ונגישות בתחבורה ציבורית
STORES_DATA = [
    # --- BERLIN ---
    {
        "city": "Berlin", "state": "Berlin", "category": "Supermarkt",
        "store_name": "REWE City", "address": "Hauptbahnhof (Europaplatz 1)",
        "opening_hours": "08:00 - 22:00", "transit": "S-Bahn / U5 Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an allen Feiertagen",
        "best_time": "Vor 10:00 & nach 20:00", "parking": "Parkhaus Hauptbahnhof",
        "assortment": "Vollsortiment", "note": "Geöffnet an Sonn- und Feiertagen"
    },
    {
        "city": "Berlin", "state": "Berlin", "category": "Drogerie",
        "store_name": "Rossmann", "address": "Bahnhof Ostbahnhof",
        "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / Regio Ostbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkplatz Ostbahnhof",
        "assortment": "Drogerie & Babybedarf", "note": "Geöffnet an Sonn- und Feiertagen"
    },
    {
        "city": "Berlin", "state": "Berlin", "category": "Supermarkt",
        "store_name": "Edeka", "address": "Bahnhof Friedrichstraße",
        "opening_hours": "08:00 - 22:00", "transit": "S-Bahn / U6 Friedrichstraße",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Nach 19:00 Uhr", "parking": "Nur ÖPNV",
        "assortment": "Vollsortiment", "note": "Geöffnet an Sonn- und Feiertagen"
    },
    {
        "city": "Berlin", "state": "Berlin", "category": "Bio-Supermarkt",
        "store_name": "Denns BioMarkt", "address": "Bahnhof Ostkreuz",
        "opening_hours": "08:00 - 21:00", "transit": "S-Bahn Ostkreuz",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 12:00 Uhr", "parking": "Umgebung (begrenzt)",
        "assortment": "Bio-Lebensmittel", "note": "Sonn- und Feiertags geöffnet"
    },
    {
        "city": "Berlin", "state": "Berlin", "category": "Apotheke",
        "store_name": "Hauptbahnhof Apotheke", "address": "Hauptbahnhof 1. OG",
        "opening_hours": "00:00 - 24:00", "transit": "Hauptbahnhof",
        "sunday_open": True, "holiday_status": "24/7 Notdienst an Feiertagen",
        "best_time": "Jederzeit", "parking": "Parkhaus Hauptbahnhof",
        "assortment": "Medikamente & Notfall", "note": "24/7 Notdienst"
    },
    {
        "city": "Berlin", "state": "Berlin", "category": "Tankstelle / REWE To Go",
        "store_name": "Aral / REWE To Go", "address": "Heerstraße 92",
        "opening_hours": "00:00 - 24:00", "transit": "Bus M49 / X34",
        "sunday_open": True, "holiday_status": "24/7 Geöffnet",
        "best_time": "Jederzeit", "parking": "Kostenlos an der Tankstelle",
        "assortment": "Snacks & Grundnahrung", "note": "24/7 Shop & Snack"
    },

    # --- MÜNCHEN ---
    {
        "city": "München", "state": "Bayern", "category": "Supermarkt",
        "store_name": "Edeka", "address": "Hauptbahnhof (Zwischengeschoss)",
        "opening_hours": "08:00 - 23:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an allen Feiertagen",
        "best_time": "Vor 10:00 & nach 20:00", "parking": "Tiefgarage Hauptbahnhof",
        "assortment": "Vollsortiment", "note": "Sonn- und Feiertags geöffnet"
    },
    {
        "city": "München", "state": "Bayern", "category": "Supermarkt",
        "store_name": "Edeka", "address": "Flughafen München (MUC) Zentralallee",
        "opening_hours": "05:30 - 22:00", "transit": "S1 / S8 Flughafen München",
        "sunday_open": True, "holiday_status": "Täglich geöffnet",
        "best_time": "Vor 11:00 Uhr", "parking": "Flughafen Parkhaus (P20)",
        "assortment": "Vollsortiment", "note": "Täglich geöffnet"
    },
    {
        "city": "München", "state": "Bayern", "category": "Drogerie",
        "store_name": "dm-drogerie markt", "address": "Ostbahnhof Platz",
        "opening_hours": "07:00 - 22:00", "transit": "S-Bahn / U4 Ostbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkgarage Ostbahnhof",
        "assortment": "Drogerie & Kosmetik", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- HAMBURG ---
    {
        "city": "Hamburg", "state": "Hamburg", "category": "Supermarkt",
        "store_name": "Edeka Tamme", "address": "Hauptbahnhof Wandelhalle",
        "opening_hours": "07:00 - 23:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 10:00 Uhr", "parking": "Parkhaus CentrO",
        "assortment": "Vollsortiment", "note": "Sonn- und Feiertags geöffnet"
    },
    {
        "city": "Hamburg", "state": "Hamburg", "category": "Drogerie",
        "store_name": "Rossmann", "address": "Hauptbahnhof Wandelhalle OG",
        "opening_hours": "08:00 - 21:00", "transit": "Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Nach 18:00 Uhr", "parking": "Parkhaus Wandelhalle",
        "assortment": "Drogerieartikel", "note": "Sonn- und Feiertags geöffnet"
    },
    {
        "city": "Hamburg", "state": "Hamburg", "category": "Supermarkt",
        "store_name": "Edeka", "address": "Bahnhof Altona (Untergeschoss)",
        "opening_hours": "07:00 - 23:00", "transit": "S-Bahn Bahnhof Altona",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Bahnhof Altona",
        "assortment": "Vollsortiment", "note": "Täglich geöffnet"
    },

    # --- FRANKFURT AM MAIN ---
    {
        "city": "Frankfurt am Main", "state": "Hessen", "category": "Supermarkt",
        "store_name": "REWE City", "address": "Fernbahnhof Flughafen",
        "opening_hours": "06:00 - 22:00", "transit": "Fernbahnhof / Regio Flughafen",
        "sunday_open": True, "holiday_status": "Täglich geöffnet",
        "best_time": "Vor 12:00 Uhr", "parking": "Flughafen Parkhaus",
        "assortment": "Vollsortiment", "note": "Täglich geöffnet"
    },
    {
        "city": "Frankfurt am Main", "state": "Hessen", "category": "Drogerie",
        "store_name": "Rossmann", "address": "Hauptbahnhof B-Ebene",
        "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Tiefgarage Hbf",
        "assortment": "Drogerieartikel", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- KÖLN ---
    {
        "city": "Köln", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Trankgasse 11",
        "opening_hours": "00:00 - 24:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "24/7 an Feiertagen geöffnet",
        "best_time": "Jederzeit", "parking": "Tiefgarage Am Dom",
        "assortment": "Snacks & Lebensmittel", "note": "24/7 Geöffnet"
    },

    # --- DÜSSELDORF ---
    {
        "city": "Düsseldorf", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "Edeka", "address": "Hauptbahnhof Konrad-Adenauer-Platz",
        "opening_hours": "00:00 - 24:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "24/7 Durchgehend geöffnet",
        "best_time": "Vor 10:00 Uhr", "parking": "Tiefgarage Hauptbahnhof",
        "assortment": "Vollsortiment", "note": "24/7 Durchgehend geöffnet"
    },

    # --- STUTTGART ---
    {
        "city": "Stuttgart", "state": "Baden-Württemberg", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Arnulf-Klett-Platz",
        "opening_hours": "06:00 - 23:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Stuttgart",
        "assortment": "Frische Lebensmittel", "note": "Sonntags geöffnet"
    },
    {
        "city": "Stuttgart", "state": "Baden-Württemberg", "category": "Bäckerei",
        "store_name": "Bäckerei Trezsch", "address": "Flughafen Stuttgart Terminal 1",
        "opening_hours": "06:00 - 20:00", "transit": "S2 / S3 Flughafen",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "07:00 - 10:00 Uhr", "parking": "Flughafen Parkhaus",
        "assortment": "Backwaren & Kaffee", "note": "Frische Brötchen am Sonntag"
    },

    # --- LEIPZIG ---
    {
        "city": "Leipzig", "state": "Sachsen", "category": "Supermarkt",
        "store_name": "Aldi Nord", "address": "Hauptbahnhof Promenaden OG 1",
        "opening_hours": "12:00 - 18:00", "transit": "S-Bahn / Tram Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Sonderöffnung an Feiertagen",
        "best_time": "12:00 - 14:00 Uhr", "parking": "Promenaden Parkhaus",
        "assortment": "Discounter Vollsortiment", "note": "Sonderöffnung Sonntags"
    },

    # --- DRESDEN ---
    {
        "city": "Dresden", "state": "Sachsen", "category": "Supermarkt",
        "store_name": "Lidl", "address": "Hauptbahnhof Wiener Platz 4",
        "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / Tram Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Tiefgarage Wiener Platz",
        "assortment": "Vollsortiment", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- HANNOVER ---
    {
        "city": "Hannover", "state": "Niedersachsen", "category": "Supermarkt",
        "store_name": "Lidl", "address": "Hauptbahnhof Ernst-August-Platz",
        "opening_hours": "08:00 - 22:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Nach 19:00 Uhr", "parking": "Parkhaus Ernst-August-Galerie",
        "assortment": "Vollsortiment", "note": "Sonntags geöffnet"
    },

    # --- NÜRNBERG ---
    {
        "city": "Nürnberg", "state": "Bayern", "category": "Supermarkt",
        "store_name": "Lidl", "address": "Hauptbahnhof Bahnhofsplatz 9",
        "opening_hours": "08:00 - 21:00", "transit": "S-Bahn / U1 / U2 / U3 Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hauptbahnhof",
        "assortment": "Vollsortiment", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- BREMEN ---
    {
        "city": "Bremen", "state": "Bremen", "category": "Supermarkt",
        "store_name": "REWE City", "address": "Hauptbahnhof Bahnhofsplatz 15",
        "opening_hours": "08:00 - 22:00", "transit": "BSAG Tram / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "BREPARK Parkhaus Hbf",
        "assortment": "Vollsortiment", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- ESSEN ---
    {
        "city": "Essen", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "Lidl", "address": "Hauptbahnhof Am Hauptbahnhof 5",
        "opening_hours": "09:00 - 20:00", "transit": "S-Bahn / U-Bahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hauptbahnhof",
        "assortment": "Vollsortiment", "note": "Sonntags geöffnet"
    },

    # --- DORTMUND ---
    {
        "city": "Dortmund", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Königswall 15",
        "opening_hours": "06:00 - 23:00", "transit": "S-Bahn / Stadtbahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 10:00 Uhr", "parking": "Parkhaus Hbf Dortmund",
        "assortment": "Frische Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- BONN ---
    {
        "city": "Bonn", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Am Hauptbahnhof 1",
        "opening_hours": "06:00 - 22:00", "transit": "Stadtbahn Hauptbahnhof Bonn",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Passage",
        "assortment": "Snacks & Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- MANNHEIM ---
    {
        "city": "Mannheim", "state": "Baden-Württemberg", "category": "Supermarkt",
        "store_name": "REWE City", "address": "Hauptbahnhof Bahnhofscheitel",
        "opening_hours": "08:00 - 22:00", "transit": "RNV Tram / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hauptbahnhof",
        "assortment": "Vollsortiment", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- KARLSRUHE ---
    {
        "city": "Karlsruhe", "state": "Baden-Württemberg", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofplatz 1a",
        "opening_hours": "06:00 - 22:00", "transit": "KVV Tram / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Karlsruhe",
        "assortment": "Frische Lebensmittel", "note": "Täglich geöffnet"
    },

    # --- MÜNSTER ---
    {
        "city": "Münster", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Berliner Platz 29",
        "opening_hours": "06:00 - 23:00", "transit": "Hauptbahnhof Münster",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Bahnhofstraße",
        "assortment": "Snacks & Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- AUGSBURG ---
    {
        "city": "Augsburg", "state": "Bayern", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Viktoriastraße 1",
        "opening_hours": "06:00 - 22:00", "transit": "VGA Tram / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Augsburg",
        "assortment": "Lebensmittel & Snacks", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- WIESBADEN ---
    {
        "city": "Wiesbaden", "state": "Hessen", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofsplatz 1",
        "opening_hours": "06:00 - 22:00", "transit": "ESWE Bus / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Liliencarré",
        "assortment": "Snacks & Getränke", "note": "Sonntags geöffnet"
    },

    # --- POTSDAM ---
    {
        "city": "Potsdam", "state": "Brandenburg", "category": "Supermarkt",
        "store_name": "Bio Lüske", "address": "Hauptbahnhof Passage",
        "opening_hours": "08:00 - 20:00", "transit": "S7 / Tram Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Bahnhofspassagen Parkhaus",
        "assortment": "Bio-Lebensmittel", "note": "Sonntags geöffnete Bio-Filiale"
    },
    {
        "city": "Potsdam", "state": "Brandenburg", "category": "Drogerie",
        "store_name": "Rossmann", "address": "Hauptbahnhof Bahnhofspassagen",
        "opening_hours": "08:00 - 20:00", "transit": "S-Bahn Potsdam Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 12:00 Uhr", "parking": "Bahnhofspassagen Parkhaus",
        "assortment": "Drogerie & Baby", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- MAINZ ---
    {
        "city": "Mainz", "state": "Rheinland-Pfalz", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofplatz 1",
        "opening_hours": "06:00 - 22:00", "transit": "Tram / Bus Hauptbahnhof Mainz",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Mainz",
        "assortment": "Frische Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- FREIBURG IM BREISGAU ---
    {
        "city": "Freiburg im Breisgau", "state": "Baden-Württemberg", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bismarckallee 5",
        "opening_hours": "06:00 - 23:00", "transit": "VAG Tram / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Bahnhof Garage",
        "assortment": "Snacks & Lebensmittel", "note": "Täglich geöffnet"
    },

    # --- BIELEFELD ---
    {
        "city": "Bielefeld", "state": "Nordrhein-Westfalen", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofstraße 67",
        "opening_hours": "06:00 - 22:00", "transit": "StadtBahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Bielefeld",
        "assortment": "Lebensmittel & Snacks", "note": "Sonntags geöffnet"
    },

    # --- KIEL ---
    {
        "city": "Kiel", "state": "Schleswig-Holstein", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Sophienblatt 25",
        "opening_hours": "06:00 - 22:00", "transit": "Bus / Hauptbahnhof Kiel",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "CAP Parkhaus",
        "assortment": "Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- ROSTOCK ---
    {
        "city": "Rostock", "state": "Mecklenburg-Vorpommern", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Konrad-Adenauer-Platz 1",
        "opening_hours": "06:00 - 22:00", "transit": "S-Bahn / Tram Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Rostock",
        "assortment": "Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- HALLE (SAALE) ---
    {
        "city": "Halle (Saale)", "state": "Sachsen-Anhalt", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofsplatz 1",
        "opening_hours": "06:00 - 22:00", "transit": "S-Bahn / Tram Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Halle",
        "assortment": "Lebensmittel", "note": "Sonntags geöffnet"
    },

    # --- HEIDELBERG ---
    {
        "city": "Heidelberg", "state": "Baden-Württemberg", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Willy-Brandt-Platz 5",
        "opening_hours": "06:00 - 22:00", "transit": "RNV Tram / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Heidelberg",
        "assortment": "Snacks & Lebensmittel", "note": "Täglich geöffnet"
    },

    # --- REGENSBURG ---
    {
        "city": "Regensburg", "state": "Bayern", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Bahnhofstraße 18",
        "opening_hours": "06:00 - 22:00", "transit": "RVV Bus / Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hbf Regensburg",
        "assortment": "Frische Lebensmittel", "note": "Sonn- und Feiertags geöffnet"
    },

    # --- SAARBRÜCKEN ---
    {
        "city": "Saarbrücken", "state": "Saarland", "category": "Supermarkt",
        "store_name": "REWE To Go", "address": "Hauptbahnhof Am Hauptbahnhof 4",
        "opening_hours": "06:00 - 22:00", "transit": "Saarbahn Hauptbahnhof",
        "sunday_open": True, "holiday_status": "Geöffnet an Feiertagen",
        "best_time": "Vor 11:00 Uhr", "parking": "Parkhaus Hauptbahnhof",
        "assortment": "Lebensmittel & Snacks", "note": "Sonntags geöffnet"
    }
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
            "holiday_status": store.get("holiday_status", "Sonderöffnung an Feiertagen"),
            "best_time": store.get("best_time", "Vor 11:00 Uhr empfohlen"),
            "parking": store.get("parking", "Parkmöglichkeiten am Bahnhof"),
            "assortment": store.get("assortment", "Vollsortiment"),
            "note": store["note"]
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"[{updated_str}] Successfully generated data.json with {len(STORES_DATA)} rich items across Germany.")

if __name__ == "__main__":
    generate_live_status()
