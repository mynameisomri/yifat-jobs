import json
from datetime import datetime
import pytz

def update_jobs():
    # הגדרת זמן עדכון לפי שעון פלורידה
    tz = pytz.timezone('US/Eastern')
    now_florida = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    # הקריטריונים של יפעת
    output = {
        "metadata": {
            "last_scan": now_florida,
            "target_roles": ["VP Strategy", "VP Operations", "VP Partnerships", "Director"],
            "min_salary": 150000,
            "status": "Active"
        },
        "jobs": [
            {
                "company": "Mercury",
                "role": "VP Strategy & Corporate Development",
                "salary": "$210,000 - $260,000",
                "match_percent": 96,
                "analysis": "בנק הייטק מודרני. הניסיון של יפעת בניהול אופרציות בנקאיות הוא התאמה מדויקת.",
                "link": "https://mercury.com/jobs"
            },
            {
                "company": "Marqeta",
                "role": "VP Strategic Partnerships",
                "salary": "$190,000 - $230,000",
                "match_percent": 92,
                "analysis": "מעבר מצוין לפינטק. שימוש ברקע הבנקאי של יפעת לבניית שותפויות אסטרטגיות.",
                "link": "https://www.marqeta.com/careers"
            }
        ]
    }

    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(f"Jobs updated successfully at {now_florida}")

if __name__ == "__main__":
    update_jobs()
