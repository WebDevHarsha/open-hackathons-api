# Open Hackathons API

A simple API that provides up-to-date information about open hackathons from various platforms.


## Live API Index

View all available JSON files directly from GitHub Pages:  
👉 **https://webdevharsha.github.io/open-hackathons-api/**

## Official API Documentation

Interactive and developer-friendly API reference:  
👉 **https://bump.sh/void/doc/open-hackathons-api/**

This documentation includes endpoint schemas, field definitions, and response examples.

## 🔗 API Endpoints

Access the latest hackathon data through multiple endpoints:

### All Hackathons
```
https://WebDevHarsha.github.io/open-hackathons-api/data.json
```

### Online Hackathons
```
https://WebDevHarsha.github.io/open-hackathons-api/data-online.json
```

### Offline/In-Person Hackathons
```
https://WebDevHarsha.github.io/open-hackathons-api/data-offline.json
```

### Featured Hackathons
```
https://WebDevHarsha.github.io/open-hackathons-api/data-featured.json
```

### Sorted by Prize Amount
```
https://WebDevHarsha.github.io/open-hackathons-api/data-by-prize.json
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
git clone https://github.com/WebDevHarsha/open-hackathons-api.git
cd open-hackathons-api
```

### 2. Configure GitHub Secrets

Add your MongoDB connection string as a GitHub secret:

1. Go to your repository Settings
2. Navigate to **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `MONGODB_URI`
5. Value: Your MongoDB connection string (e.g., `mongodb+srv://username:password@cluster.mongodb.net/dumpy`)

### 3. MongoDB Setup

The API fetches data from:
- **Database**: `dumpy`
- **Collection**: `hackathons`

Update `scripts/fetch_data.py` if your database/collection names are different.
- Adjust the query filters if you want to fetch specific hackathons only

### 4. Enable GitHub Pages

1. Go to repository Settings
2. Navigate to **Pages**
3. Under **Source**, select **Deploy from a branch**
4. Select the `master` branch and `/ (root)` folder
5. Click **Save**

Your API will be available at: `https://WebDevHarsha.github.io/open-hackathons-api/`

### 5. Test the Workflow

You can manually trigger the workflow:

1. Go to the **Actions** tab in your repository
2. Select **Update Hackathons Data** workflow
3. Click **Run workflow**

## ⏰ Update Schedule

The data is automatically updated every day at 12:00 AM UTC (midnight) via GitHub Actions.

You can modify the schedule in `.github/workflows/update-data.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Daily at 12:00 AM UTC (midnight)
```

## 📊 Available Endpoints

| Endpoint | Description | Use Case |
|----------|-------------|----------|
| `data.json` | All hackathons | Get complete list of hackathons |
| `data-online.json` | Online hackathons only | Filter for remote hackathons |
| `data-offline.json` | In-person hackathons | Filter for local/physical hackathons |
| `data-featured.json` | Featured hackathons | Highlighted or promoted hackathons |
| `data-by-prize.json` | Sorted by prize amount | Find high-value competitions |

## 🚀 Usage Examples

### JavaScript/TypeScript

```javascript
// Fetch all hackathons
fetch('https://WebDevHarsha.github.io/open-hackathons-api/data.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Total hackathons: ${data.count}`);
    console.log(`Last updated: ${data.last_updated}`);
    data.hackathons.forEach(hackathon => {
      console.log(`${hackathon.title} - ${hackathon.organization_name}`);
    });
  });

// Fetch only online hackathons
fetch('https://WebDevHarsha.github.io/open-hackathons-api/data-online.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Online hackathons: ${data.count}`);
  });
```

### Python

```python
import requests

# Fetch all hackathons
response = requests.get('https://WebDevHarsha.github.io/open-hackathons-api/data.json')
data = response.json()

print(f"Total hackathons: {data['count']}")
print(f"Last updated: {data['last_updated']}")

for hackathon in data['hackathons']:
    print(f"{hackathon['title']} - {hackathon['organization_name']}")

# Fetch hackathons by prize
prize_response = requests.get('https://WebDevHarsha.github.io/open-hackathons-api/data-by-prize.json')
prize_data = prize_response.json()
print(f"Top prize: {prize_data['hackathons'][0]['prizeText']}")
```

### cURL

```bash
# All hackathons
curl https://WebDevHarsha.github.io/open-hackathons-api/data.json

# Online only
curl https://WebDevHarsha.github.io/open-hackathons-api/data-online.json

# Offline only
curl https://WebDevHarsha.github.io/open-hackathons-api/data-offline.json
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
| `displayed_location` | string | Location (Online, or City/Country) |
| `registrations_count` | number | Number of registrations |
| `prizeText` | string | Prize information |
| `time_left_to_submission` | string | Time remaining |
| `themes` | array | Hackathon themes/categories |
| `start_a_submission_url` | string | Submission URL |
| `source` | string | Data source (e.g., "devpost") |

## 🎯 Features

- ✅ **5 API Endpoints** - All, Online, Offline, Featured, By Prize
- ✅ **Daily Updates** - Automatic data refresh at 6:00 AM UTC
- ✅ **MongoDB Integration** - Direct database connection
- ✅ **GitHub Actions** - Automated workflow
- ✅ **GitHub Pages** - Free hosting
- ✅ **RESTful JSON** - Clean, structured data format
- ✅ **No Authentication** - Public API, free to use

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this API for your projects!

## ⚠️ Notes

- The data is cached and updated daily, so it may not reflect real-time changes
- Ensure your MongoDB connection string has read permissions
- The API is rate-limited by GitHub Pages (not by this application)
- All hackathons in the database are currently open (active)

## 🐛 Troubleshooting

### Workflow fails with "MONGODB_URI not set"
- Ensure you've added the `MONGODB_URI` secret in GitHub repository settings

### Data is not updating
- Check the Actions tab for workflow run status and error logs
- Verify MongoDB connection string is correct and has read permissions

### 404 error on GitHub Pages
- Ensure GitHub Pages is enabled and pointing to the `master` branch
- Wait a few minutes after enabling GitHub Pages for the first time

---

Made with ❤️ by [WebDevHarsha](https://github.com/WebDevHarsha)
