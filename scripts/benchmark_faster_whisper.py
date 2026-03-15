import os
import time
import json
from faster_whisper import WhisperModel
from calculate_wer import calculate_wer

def run_faster_whisper(audio_dir="data/"):
    model = WhisperModel("small", device="cpu", compute_type="int8")
    results = []

    for f in os.listdir(audio_dir):
        if f.endswith(".wav"):
            audio_path = os.path.join(audio_dir, f)

            start = time.time()
            segments, info = model.transcribe(audio_path)
            inference_time = time.time() - start

            transcript = " ".join([seg.text for seg in segments])

            # Dummy reference transcript
            reference = "this is a sample reference text"

            wer_score = calculate_wer(reference, transcript)

            results.append({
                "file": f,
                "predicted": transcript,
                "wer": wer_score,
                "inference_time": round(inference_time, 3)
            })

    with open("results/faster_whisper_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Benchmark Completed Successfully!")

if __name__ == "__main__":
    run_faster_whisper()