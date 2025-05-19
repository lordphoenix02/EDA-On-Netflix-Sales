# EDA-On-Netflix-Sales
Overview:
This project involves performing Exploratory Data Analysis (EDA) on Netflix sales data to uncover patterns, trends, and insights related to user preferences, popular content types, and revenue performance. The goal is to understand the business performance and customer engagement by analyzing streaming behavior.

Dataset:
The dataset used in this project includes the following columns:

Show ID – Unique identifier for each show/movie

Title – Name of the content

Type – Movie or TV Show

Director – Director of the content

Cast – Leading actors

Country – Country of origin

Date Added – When the title was added to Netflix

Release Year – Year of release

Rating – Content rating (e.g., PG, TV-MA)

Duration – Length of content (minutes/seasons)

Genre – Type of content (e.g., Drama, Comedy)

Revenue/Sales – Revenue or sales generated (if available)

Platform Metrics – Viewer count, hours watched, etc. (if available)

Objective:
To explore and analyze the Netflix dataset to understand trends in content, audience preferences, and sales.

To identify which types of content perform best in terms of viewership and revenue.

To provide insights that can guide Netflix’s content strategy and investment.

Libraries Used:
Pandas – For data manipulation and analysis.

NumPy – For numerical operations.

Matplotlib – For basic data visualizations.

Seaborn – For enhanced statistical visualizations.

Plotly – For interactive data plots.

Power BI (if applicable) – For interactive dashboards and visual storytelling.

EDA Steps Followed:
Loading and understanding the dataset – Checked column types, missing values, and basic statistics.

Data cleaning – Removed or imputed missing data, standardized categorical columns.

Univariate Analysis – Analyzed individual features like content types, ratings, and genres.

Bivariate Analysis – Explored relationships such as genre vs. revenue or year vs. number of releases.

Time Series Analysis – Analyzed trends over time in content addition and sales.

Geographical Analysis – Checked how content distribution and sales vary by country.

Revenue Analysis – Investigated which genres or content types drive higher sales.

Visualization – Created charts, graphs, and dashboards for key insights.

Key Insights:
📈 TV Shows and Movies added after 2018 have increased significantly.

🌍 USA and India contribute to the highest number of content titles.

🎭 Drama and Comedy are the most common genres across the platform.

💰 Content rated TV-MA and R tends to generate higher revenue.

🕒 Longer duration content tends to have more watch time but doesn't always correlate with higher sales.

📊 Peak content releases are seen in the last quarter of each year.

Conclusion:
The EDA reveals that Netflix’s content library is diverse and growing, with a strong presence in drama and comedy genres. Strategic content types and countries show patterns of higher sales and engagement. These insights can help Netflix optimize its content strategy, focusing on high-performing genres, countries, and durations to improve viewer satisfaction and revenue.
