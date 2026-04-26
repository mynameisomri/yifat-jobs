import json

def update_jobs():
    new_jobs = [
        {
            "company": "Mercury",
            "role": "VP Strategy & Corporate Development",
            "salary": "$210,000 - $260,000",
            "match_percent": 96,
            "analysis": "בנק הייטק מודרני שצומח מהר. הניסיון שלך מ-SVB הוא נכס אסטרטגי עבורם.",
            "link": "https://mercury.com/jobs"
        },
        {
            "company": "Marqeta",
            "role": "VP Strategic Partnerships",
            "salary": "$190,000 - $230,000",
            "match_percent": 92,
            "analysis": "מעבר לצד של הפינטק. שימוש בניסיון הבנקאי שלך לבניית שותפויות אסטרטגיות.",
            "link": "https://www.marqeta.com/careers"
        }
    ]

    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(new_jobs, f, ensure_ascii=False, indent=4)
    print("Jobs updated successfully.")

if __name__ == "__main__":
    update_jobs()
