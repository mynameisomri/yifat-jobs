import json
import os

def update_jobs():
    # המשרות הטובות ביותר ליפעת - מעודכן ל-25 באפריל
    new_jobs = [
        {
            "company": "BNY Mellon",
            "role": "Senior Vice President, Client Operations Manager",
            "salary": "$175,000 - $235,000",
            "match_percent": 98,
            "analysis": "משרת ה-SVP בלייק מרי. זו ההזדמנות הכי טובה כרגע: מטה טהור, דקות נסיעה מהבית, ושכר שמתאים לניסיון שלך.",
            "link": "https://www.bnymellon.com/careers"
        },
        {
            "company": "Circle",
            "role": "VP - Global Head of Product Security and Risk",
            "salary": "$318,000 - $365,000",
            "match_percent": 97,
            "analysis": "תפקיד הנהלה בכיר ב-Remote מלא. למרות השם הטכני, מדובר בניהול סיכונים ותפעול אסטרטגי בחברת קריפטו מובילה.",
            "link": "https://www.circle.com/careers"
        },
        {
            "company": "Carta",
            "role": "Director, Private Equity & Fund Admin Ops",
            "salary": "$180,000 - $240,000",
            "match_percent": 95,
            "analysis": "ניהול אופרציות הון סיכון (VC) ב-Remote. Carta היא ה-Match המושלם לרקע שלך מ-SVB.",
            "link": "https://carta.com/careers"
        }
    ]

    # כתיבת הקובץ עם תמיכה מלאה בעברית (UTF-8)
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(new_jobs, f, ensure_ascii=False, indent=2)
    print(f"Successfully updated jobs.json with {len(new_jobs)} jobs.")

if __name__ == "__main__":
    update_jobs()
