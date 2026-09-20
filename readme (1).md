# MPLAD AI Monitoring Dashboard

A single-page dashboard for monitoring the Members of Parliament Local Area Development (MPLAD) scheme. It shows how projects are progressing and how funds are being used, and highlights AI-flagged anomalies, suspected fraud and inefficiencies so reviewers know where to look first.

> **Status:** UI prototype. All figures are sample data.

## Features

- **Summary cards:** total, completed, active and high-risk projects, fund utilization, and an overall AI risk score
- **Filters:** state, district, MP constituency, project status, risk level and date range
- **Project progress chart:** completed and ongoing projects with fund utilization over time
- **AI alert breakdown:** anomalies, fraud suspicion and inefficiencies
- **Risk heatmap:** top risk states (map is a simplified placeholder)
- **Recent AI alerts:** project, district, alert type, risk score and review status
- **Project monitoring:** sanctioned vs. utilized amount, progress, schedule and risk level
- **AI insights and quick actions:** unusual spending, duplicate projects, delays, cost deviation and vendor patterns

## Getting started

No build step or dependencies are needed.

```bash
git clone https://github.com/nidhigangwar0501-cmyk/mplad-dashboard.git
cd mplad-dashboard
```

Then open `mplad-dashboard.html` in a browser.

## Customizing

- Chart data is in the `done`, `ongoing` and `fund` arrays at the bottom of the HTML file. Replace them with data from your API.
- Tables and cards are plain HTML and can be generated from your own data.
- Filters are visual only for now and are not yet connected to any logic.

## Security

Never commit `.env` files or API keys. The included `.gitignore` excludes them. Keep secrets on a backend, not in browser code.

## Roadmap

- Connect filters to real data
- Replace the placeholder map with a state-wise GeoJSON heatmap
- Add a backend and an anomaly-detection service
- Add export for reports

## License

Add a license of your choice, for example MIT.
