from jiwer import wer

def calculate_wer(reference, hypothesis):
    error = wer(reference, hypothesis)
    return round(error * 100, 2)