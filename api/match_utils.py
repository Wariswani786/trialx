from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_trials(profile, trials, threshold=0.05):  # Lower threshold
    """
    Compute similarity scores between a patient profile and a list of clinical trials.
    Returns a list of (trial, score), sorted by descending score,
    filtering out matches below the threshold.
    """
    profile_text = f"{profile.condition} {profile.medications} {profile.gender} {profile.age}"

    trial_texts = [
        f"{trial.title} {trial.inclusion_criteria} {trial.exclusion_criteria} {trial.location}"
        for trial in trials
    ]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([profile_text] + trial_texts)

    profile_vector = vectors[0]
    trial_vectors = vectors[1:]

    scores = cosine_similarity(profile_vector, trial_vectors).flatten()

    matches = list(zip(trials, scores))

    # Filter matches above the updated lower threshold
    relevant_matches = [(trial, score) for trial, score in matches if score > threshold]

    return sorted(relevant_matches, key=lambda x: x[1], reverse=True)
