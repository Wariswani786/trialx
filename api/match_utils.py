from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_trials(user_profile_text, trials):
    trial_texts = [
        trial.inclusion_criteria + ' ' + trial.exclusion_criteria for trial in trials
    ]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user_profile_text] + trial_texts)
    
    user_vector = vectors[0]
    trial_vectors = vectors[1:]
    
    similarities = cosine_similarity(user_vector, trial_vectors).flatten()

    # Attach similarity score to each trial
    scored_trials = [
        (trial, score) for trial, score in zip(trials, similarities)
    ]

    # Sort by score descending
    scored_trials.sort(key=lambda x: x[1], reverse=True)

    return scored_trials



# match_utils.py
def match_trials_to_profile(profile, trials):
    # build profile text
    profile_text = f"{profile.condition} {profile.medications} {profile.gender} {profile.age}"

    trial_texts = [f"{t.title} {t.inclusion_criteria} {t.exclusion_criteria} {t.location}" for t in trials]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([profile_text] + trial_texts)

    profile_vector = vectors[0]
    trial_vectors = vectors[1:]

    scores = cosine_similarity(profile_vector, trial_vectors).flatten()

    # ✅ Return as list of tuples
    return list(zip(trials, scores))
