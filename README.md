# Movie Recommender System

## Description 
A machine learning–powered web application that recommends five similar movies based on user input. Built using the TMDB top 5000 movies dataset from Kaggle, this project applies core NLP techniques like stemming and vectorization, combined with cosine similarity, to find and rank similar titles. The frontend is developed with Streamlit, offering a clean and interactive user experience. 

## Learnings 
* This project deepened my understanding of text-based similarity techniques using scikit-learn.
* I learned how to preprocess textual data for recommendation systems, apply stemming for keyword normalization, and use vectorization (CountVectorizer) and cosine similarity to build a lightweight content-based recommender.
* I also became familiar with deploying quick ML prototypes using Streamlit.

## Challenges
* Key challenges included handling noisy or missing metadata in the dataset, optimizing similarity computations for faster runtime, and ensuring recommendations remained relevant and diverse.
* Additionally, integrating a user-friendly UI with a backend ML model required careful structuring of data flow in Streamlit.

## Database used 
TMDB top 5000 movies (available on kaggle)
## Concepts used 
- Basic data preprocessing using pandas
- Stemming
- Vectorization
- Cosine similarity
## Running the project

1. Download the `similarity.pkl` and `source code.zip` files from the version release v0.0.1
2. Extract all the files to the same directory.
3. Run the `app.py` file in the terminal by using code `streamlit run App.py`.
4. The following screen should appear <br/> ![initial screen](https://github.com/GC-on-git/movie-rec-system-project/assets/128742039/c41d4b7c-ec86-4987-81a5-06435054da97)
5. Select a movie and click **Show Recommendation**. <br/> example: ![example image](https://github.com/GC-on-git/movie-rec-system-project/assets/128742039/d6275354-301b-45b9-829d-29b4d2594195)

### Thank you :)

