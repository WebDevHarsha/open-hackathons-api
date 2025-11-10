# Open Hackathons API

A simple API that provides up-to-date information about open hackathons from various platforms.

## 🔗 API Endpoint

Access the latest hackathon data at:
```
https://WebDevHarsha.github.io/open-hackathons-api/data.json
```

## 📊 Data Format

The API returns a JSON object with the following structure:

```json
{
  "last_updated": "2025-11-10T06:00:00Z",
  "count": 1,
  "hackathons": [
    {
      "_id": "6911476d29da70dc2da0be0f",
      "id": 27203,
      "url": "https://innovation-challenge-2026.devpost.com/",
      "title": "Innovation Challenge 2026",
      "thumbnail_url": "//d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/003/953/790/datas/medium_square.png",
      "featured": false,
      "organization_name": "Thapar University",
      "isOpen": "open",
      "submission_period_dates": "Nov 09 - 20, 2025",
      "displayed_location": "Patiala, Punjab",
      "registrations_count": 6,
      "prizeText": "₹ 135,000",
      "time_left_to_submission": "11 days left",
      "themes": [
        {
          "id": 23,
          "name": "Beginner Friendly"
        },
        {
          "id": 6,
          "name": "Machine Learning/AI"
        },
        {
          "id": 13,
          "name": "Social Good"
        }
      ],
      "start_a_submission_url": "https://innovation-challenge-2026.devpost.com/challenges/start_a_submission",
      "source": "devpost"
    }
  ]
}
```

## 🔧 Setup Instructions

### 1. Fork/Clone this Repository

```bash
git clone https://github.com/username/open-hackathons-api.git
cd open-hackathons-api
```

### 2. Configure GitHub Secrets

Add your MongoDB connection string as a GitHub secret:

1. Go to your repository Settings
2. Navigate to **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `MONGODB_URI`
5. Value: Your MongoDB connection string (e.g., `mongodb+srv://username:password@cluster.mongodb.net/database`)

### 3. Configure MongoDB Collection

Update the `scripts/fetch_data.py` file if needed:
- Modify the collection name if it's different from the common names (`hackathons`, `events`, `challenges`, `devpost`)
- Adjust the query filters if you want to fetch specific hackathons only

### 4. Enable GitHub Pages

1. Go to repository Settings
2. Navigate to **Pages**
3. Under **Source**, select **Deploy from a branch**
4. Select the `main` branch and `/ (root)` folder
5. Click **Save**

Your API will be available at: `https://username.github.io/open-hackathons-api/data.json`

### 5. Test the Workflow

You can manually trigger the workflow:

1. Go to the **Actions** tab in your repository
2. Select **Update Hackathons Data** workflow
3. Click **Run workflow**

## ⏰ Update Schedule

The data is automatically updated every day at 6:00 AM UTC via GitHub Actions.

You can modify the schedule in `.github/workflows/update-data.yml`:

```yaml
schedule:
  - cron: '0 6 * * *'  # Daily at 6:00 AM UTC
```

## 🚀 Usage Examples

### JavaScript/TypeScript

```javascript
fetch('https://username.github.io/open-hackathons-api/data.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Total hackathons: ${data.count}`);
    console.log(`Last updated: ${data.last_updated}`);
    data.hackathons.forEach(hackathon => {
      console.log(`${hackathon.title} - ${hackathon.organization_name}`);
    });
  });
```

### Python

```python
import requests

response = requests.get('https://username.github.io/open-hackathons-api/data.json')
data = response.json()

print(f"Total hackathons: {data['count']}")
print(f"Last updated: {data['last_updated']}")

for hackathon in data['hackathons']:
    print(f"{hackathon['title']} - {hackathon['organization_name']}")
```

### cURL

```bash
curl https://username.github.io/open-hackathons-api/data.json
```

## 📝 Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `_id` | string | MongoDB ObjectId |
| `id` | number | Hackathon ID |
| `url` | string | Hackathon URL |
| `title` | string | Hackathon title |
| `thumbnail_url` | string | Thumbnail image URL |
| `featured` | boolean | Whether hackathon is featured |
| `organization_name` | string | Organizing entity |
| `isOpen` | string | Status (e.g., "open", "closed") |
| `submission_period_dates` | string | Submission period |
| `displayed_location` | string | Location |
| `registrations_count` | number | Number of registrations |
| `prizeText` | string | Prize information |
| `time_left_to_submission` | string | Time remaining |
| `themes` | array | Hackathon themes/categories |
| `start_a_submission_url` | string | Submission URL |
| `source` | string | Data source |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this API for your projects!

## ⚠️ Notes

- The data is cached and updated daily, so it may not reflect real-time changes
- Ensure your MongoDB connection string has read permissions
- The API is rate-limited by GitHub Pages (not by this application)

## 🐛 Troubleshooting

### Workflow fails with "MONGODB_URI not set"
- Ensure you've added the `MONGODB_URI` secret in GitHub repository settings

### Data is not updating
- Check the Actions tab for workflow run status and error logs
- Verify MongoDB connection string is correct and has read permissions

### 404 error on GitHub Pages
- Ensure GitHub Pages is enabled and pointing to the main branch
- Wait a few minutes after enabling GitHub Pages for the first time
