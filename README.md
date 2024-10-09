# Netflix Data Visualization Challenge

This project analyzes and visualizes data on movies and TV shows available on Netflix. The goal is to explore the dataset and answer specific questions about the content on the platform using Python libraries such as Pandas, Seaborn, and Matplotlib.

## Table of Contents
- [About the Dataset](#about-the-dataset)
- [Project Goals](#project-goals)
- [Requirements](#requirements)
- [Project Setup](#project-setup)
- [Data Exploration & Analysis](#data-exploration--analysis)
- [Business Questions Addressed](#business-questions-addressed)
  -  Proportion of Movies vs. TV Shows
  -  Distribution of Movies and Series by Release Year
  -  Additions of Movies and Series Over Time
  -  Distribution of Ratings
- [Visualizations](#visualizations)
- [Future Work](#future-work)
- [License](#license)

## About the Dataset
The dataset contains information on movies and TV shows available on Netflix, with the following columns:

- **id**: Unique identifier for each title
- **type**: Type of content (Movie or TV Show)
- **title**: Title of the movie or series
- **director**: Director of the film
- **cast**: Main actors in the title
- **date_added**: Date when the content was added to Netflix
- **release_year**: Release year of the content
- **rating**: Content rating (e.g., PG, R, etc.)
- **duration**: Duration of the movie or number of seasons for a series

## Project Goals
1. **Data Cleaning**: Handle missing values, remove duplicates, and ensure proper data formatting.
2. **Data Exploration**: Provide a statistical summary of the data and analyze the distribution of variables.
3. **Data Visualization**: Use Matplotlib and Seaborn to create meaningful visualizations that address specific business questions.
4. **Business Insights**: Draw insights regarding the content on Netflix, such as content type distribution, yearly trends, and rating analysis.

## Requirements
This project uses Python and requires the following libraries:

- `pandas`
- `matplotlib`
- `seaborn`

To install the libraries, you can use the following command:
```bash
pip install pandas matplotlib seaborn
```
## Project Setup
1. **Clone the Repository:**
 ```bash
git clone https://github.com/victorsimasdev/Netflix-Data-Visualization
```
2. **Navigate to the Directory:**
```bash
cd Netflix-Data-Visualization
```
3. **Run the Python Script:**
```bash
python netflix-data.py
```
## Data Exploration & Analysis
- **Data Loading:** Load the dataset using Pandas.
- **Handling Missing Data:** Identify and handle any null values.
- **Data Cleaning:** Remove duplicates and convert columns to the appropriate data types.
- **Statistical Summary:** Use ```describe()``` to get summary of the data.

## Business Questions Addressed
1. **Distribution of Movies vs. TV Shows:**
   - **Question:** What is the ratio of movies to TV shows in the dataset?
![Figure_1](https://github.com/user-attachments/assets/7e734dc5-96a1-47ef-948d-5e45014c1379)

2. **Content Added Over Time:**
   - **Question:** How does the distribution of movies and series vary by release year?
![Figure_2](https://github.com/user-attachments/assets/741af2f4-d383-4fba-8eb5-c4b924a853ef)

3. **Rating Analysis:**
   - **Question:** How many movies and TV shows were added to Netflix each year?
![Figure_3](https://github.com/user-attachments/assets/ccb0846a-6a1b-455e-b233-8b2538718e70)
     
4. **Content Duration:**
   - **Question:** What is the distribution of content ratings?
![Figure_4](https://github.com/user-attachments/assets/8000ce08-30c8-4db4-9420-35814db068d6)
  
## Visualizations
The project includes various visualizations to support the analysis and business questions.

## Future Work
Potential future enhancements include:
   - Analyzing genre popularity over time.
   - Creating more interactive visualizations using Plotly.
   - Exploring correlations between the director, cast, and content popularity.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
