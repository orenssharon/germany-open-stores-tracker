import json
import datetime

# רשימת נתונים בסיסית של מיקומים מרכזיים הפתוחים בימי ראשון וחגים בגרמניה
STORES_DATA = [
    {
        "city": "Berlin",
        "state": "Berlin",
        "type": "Supermarkt",
        "store_name": "REWE City",
        "address": "Hauptbahnhof (Europaplatz 1)",
        "opening_hours": "08:00 - 22:00",
        "sunday_open": True,
        "note": "Geöffnet an Sonn- und Feiertagen"
    },
    {
        "city": "Berlin",
        "state": "Berlin",
        "type": "Drogerie",
        "store_name": "Rossmann",
        "address": "Bahnhof Ostbahnhof",
        "opening_hours": "08:00 - 21:00",
        "sunday_open": True,
        "note": "Geöffnet an Sonn- und Feiertagen"
    },
    {
        "city": "München",
        "state": "Bayern",
        "type": "Supermarkt",
        "store_name": "Edeka",
        "address": "Hauptbahnhof (Zwischengeschoss)",
        "opening_hours": "08:00 - 23:00",
        "sunday_open": True,
        "note": "Sonn- und Feiertags geöffnet"
    },
    {
        "city": "München",
        "state": "Bayern",
        "type": "Supermarkt",
        "store_name": "Edeka",
        "address": "Flughafen München (MUC) Zentralallee",
        "opening_hours": "05:30 - 22:00",
        "sunday_open": True,
        "note": "Täglich geöffnet"
    },
    {
        "city": "Hamburg",
        "state": "Hamburg",
        "type": "Supermarkt",
        "store_name": "Edeka Tamme",
        "address": "Hauptbahnhof Wandelhalle",
        "opening_hours": "07:00 - 23:00",
        "sunday_open": True,
        "note": "Sonn- und Feiertags geöffnet"
    },
    {
        "city": "Frankfurt am Main",
        "state": "Hessen",
        "type": "Supermarkt",
        "store_name": "REWE City",
        "address": "Fernbahnhof Flughafen",
        "opening_hours": "06:00 - 22:00",
        "sunday_open": True,
        "note": "Täglich geöffnet"
    },
    {
        "city": "Köln",
        "state": "Nordrhein-Westfalen",
        "type": "Supermarkt",
        "store_name": "REWE To Go",
        "address": "Hauptbahnhof Trankgasse 11",
        "opening_hours": "00:00 - 24:00",
        "sunday_open": True,
        "note": "24/7 Geöffnet"
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
            "category": store["type"],
            "store_name": store["store_name"],
            "address": store["address"],
            "status": f"{status_text} ({store['opening_hours']})",
            "note": store["note"]
        })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"[{updated_str}] Successfully generated data.json with {len(STORES_DATA)} items.")

if __name__ == "__main__":
    generate_live_status()
