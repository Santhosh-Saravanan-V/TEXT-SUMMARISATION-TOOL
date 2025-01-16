# Importing necessary modules
from transformers import pipeline

# Setting up the summarization pipeline with the model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# feeding  the text to be summarized
input_text = """
 Sir Lewis Carl Davidson Hamilton (born 7 January 1985) is a British racing driver, who is set to compete in Formula One for Ferrari. Hamilton has won a joint-record seven Formula One World Drivers' Championship titles—tied with Michael Schumacher—and holds the records for most wins (105), pole positions (104), and podium finishes (202), among others.
Born and raised in Stevenage, Hamilton began his career in karting aged six, winning several national titles and attracting the attention of Ron Dennis, who signed him to the McLaren-Mercedes Young Driver Programme in 1998. After winning the direct-drive Karting World Cup and European Championship in 2000, Hamilton progressed to junior formulae, where his successes included winning the Formula 3 Euro Series and the GP2 Series. He subsequently signed for McLaren in 2007, becoming the first black driver to compete in Formula One at the Australian Grand Prix. In his rookie season, Hamilton won four Grands Prix and set several records as he finished runner-up to Kimi Räikkönen by one point. Hamilton won his maiden title in 2008, making a title-deciding overtake on the last lap of the last race of the season to become the then-youngest World Drivers' Champion. The dominant Red Bull-Renault combination prevailed throughout his remaining four seasons at McLaren, with Hamilton achieving multiple race wins in each, including his involvement in a four-way title battle in 2010.
"""

# Performing the text summarization
summary = summarizer(input_text, max_length=60, min_length=25, do_sample=False)

# Printing  the original text and its summarized version
print("Original Text:\n", input_text)
print("\nSummarized Text:\n", summary[0]['summary_text'])
