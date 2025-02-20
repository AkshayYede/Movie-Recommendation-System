import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)


from flask import Flask, render_template, request
import pickle
import pandas as pd
import gdown

# Google Drive file ID
url = 'https://drive.google.com/file/d/1Yku-PJVMMre5Uv0zXV_r7zsDCrr7bfeI/view?usp=sharing'
output = "similarity.pkl"

try:
    with open(output, "rb") as f:
        similarity = pickle.load(f)
except:
    gdown.download(url, output, quiet=False)
    with open(output, "rb") as f:
        similarity = pickle.load(f)

print("Similarity.pkl loaded successfully!")

app = Flask(__name__)

# Load Pickle Files
movies_dict = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Convert dictionary to DataFrame
df = pd.DataFrame(movies_dict)

# Function to Recommend Movies
def recommend(movie):
    movie = movie.lower().strip()
    title_mapping = {title.lower(): title for title in df['title'].values}

    if movie not in title_mapping:
        return None  # Return None to handle errors gracefully

    original_title = title_mapping[movie]
    index = df[df['title'] == original_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    return [df.iloc[i[0]].title for i in distances[1:6]]

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None
    error_message = None

    if request.method == "POST":
        movie_name = request.form.get("movie_name", "").strip()
        if not movie_name:
            error_message = "Please enter a movie name."
        else:
            recommendations = recommend(movie_name)
            if recommendations is None:
                error_message = "Movie not found. Please check the spelling or try another title."

    return render_template("index.html", recommendations=recommendations, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
