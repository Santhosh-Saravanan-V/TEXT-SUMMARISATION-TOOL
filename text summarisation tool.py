# Import necessary modules
from transformers import pipeline

# Set up the summarization pipeline with the chosen model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Provide the text to be summarized
input_text = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed 
to think and act like humans. The term may also be applied to any machine that exhibits traits associated 
with a human mind such as learning and problem-solving. The ideal characteristic of artificial intelligence 
is its ability to rationalize and take actions that have the best chance of achieving a specific goal. 
Machine learning is a subset of AI and refers to the concept that computer programs can automatically learn 
and adapt to new data without being assisted by humans. Deep learning techniques enable this automatic learning 
through the absorption of huge amounts of unstructured data such as text, images, or video.
"""

# Perform text summarization
summary = summarizer(input_text, max_length=60, min_length=25, do_sample=False)

# Print the original text and its summarized version
print("Original Text:\n", input_text)
print("\nSummarized Text:\n", summary[0]['summary_text'])
