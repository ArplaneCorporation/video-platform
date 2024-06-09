import os

# ตัวอย่างลิงก์และข้อมูลวิดีโอ
videos = [
    {
        "title": "Sample Video 1",
        "video_id": "dQw4w9WgXcQ",
        "description": "This is a description of Sample Video 1",
        "date": "2024-06-08"
    },
    {
        "title": "Sample Video 2",
        "video_id": "dQw4w9WgXcQ",
        "description": "This is a description of Sample Video 2",
        "date": "2024-06-08"
    }
]

if not os.path.exists('_videos'):
    os.makedirs('_videos')

for video in videos:
    filename = f"_videos/{video['date']}-{video['video_id']}.md"
    with open(filename, 'w') as file:
        file.write(f"---\n")
        file.write(f"title: \"{video['title']}\"\n")
        file.write(f"date: {video['date']}\n")
        file.write(f"video_id: {video['video_id']}\n")
        file.write(f"description: \"{video['description']}\"\n")
        file.write(f"---\n")