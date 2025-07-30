# match_utils.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_trials(profile, trials):
    """
    Compute similarity scores between a patient profile and a list of clinical trials.
    Returns a list of tuples: (trial, similarity_score), sorted by score descending.
    """
    # Convert profile data to a single text string
    profile_text = f"{profile.condition} {profile.medications} {profile.gender} {profile.age}"

    # Convert each trial into a single text string
    trial_texts = [
        f"{trial.title} {trial.inclusion_criteria} {trial.exclusion_criteria} {trial.location}"
        for trial in trials
    ]

    # Vectorize the texts
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([profile_text] + trial_texts)

    # Split into profile vector and trial vectors
    profile_vector = vectors[0]
    trial_vectors = vectors[1:]

    # Calculate cosine similarity
    scores = cosine_similarity(profile_vector, trial_vectors).flatten()

    # Return trials with scores, sorted by highest score
    return sorted(zip(trials, scores), key=lambda x: x[1], reverse=True)
