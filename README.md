# 🎬 Movie Recommendation System  

A simple and interactive **Movie Recommendation System** built with **Flask**. It suggests similar movies based on user input using **machine learning**.

## 🚀 Features  

- 🔍 Enter a movie name to get recommendations.  
- 🎨 Interactive and user-friendly UI.  
- 🔥 Built with Flask and Pandas.  
- 📜 Trained on a dataset of movies.  

## 🛠 Tech Stack  

- **Backend:** Flask, Pandas  
- **Frontend:** HTML, CSS, Bootstrap  
- **Data Processing:** Pickle, NumPy, Pandas
- **Model Development:** Scikit-learn

## 📂 Project Structure  

```
📦 Movie-Recommendation-System   
 ┣ 📂 templates  
 ┃ ┣ 📜 index.html  
 ┣ 📜 app.py  
 ┣ 📜 movies.pkl  
 ┣ 📜 similarity.pkl  
 ┣ 📜 requirements.txt
 ┣ 📜 tmdb_5000_movies.csv
 ┣ 📜 tmdb_5000_credits.csv
 ┣ 📜 Movie Recommender System.ipynb
 ┣ 📜 README.md  
```

## 🎯 How It Works  

1. The system loads pre-processed **movie data** and a **similarity matrix** from `.pkl` files.  
2. When a user enters a movie name, the system finds the most **similar movies** using cosine similarity.  
3. The **top 5 recommendations** are displayed.  
