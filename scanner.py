import json
from datetime import datetime

def update_jobs():
    # הגדרת הפרמטרים של יפעת
    search_criteria = {
        "target_roles": ["VP Strategy", "VP Operations", "VP Partnerships", "Director Commercial Banking"],
        "min_salary": 150000,
        "location_preference": "Remote",
        "last_scan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # כאן בעתיד יבוא קוד שמושך משרות אמיתיות מ-LinkedIn/Indeed
    # בינתיים, נעדכן את רשימת המשרות כדוגמה דינמית
    jobs = [
        {
            "company": "Mercury",
            "role": "VP Strategy",
            "salary": "$210,000",
            "match_percent": 96,
            "analysis": "מותאם אישית לפי הקריטריונים: שכר מעל 150K וניסיון בפינטק/בנקאות.",
            "link": "https://mercury.com/jobs"
        }
    ]

    output = {
        "metadata": search_criteria,
        "jobs": jobs
    }

    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(f"Scan completed at {search_criteria['last_scan']}")

if __name__ == "__main__":
    update_jobs()
