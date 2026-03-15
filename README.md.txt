-Faster-Whisper ASR Benchmark

Ye project Faster-Whisper model ka basic benchmarking check karta hai. Main ne isme kuch audio files use karke transcription, WER (Word Error Rate) aur inference time test kiya hai. Saari processing simple Python scripts ke through hoti hai.

- Project Structure
- data/ → yaha .wav audio files rakhe hain
- scripts/ → sab Python scripts yaha hain (WER, benchmark aur run script)
- results/ → benchmark ka output JSON file yaha store hota hai
- report/ → final technical report PDF
- requirements.txt → project me use hone wali libraries

-Installation
Project run karne se pehle required libraries install kar lo:


-How to Run
Benchmark run karne ke liye simply ye command chalao:
python scripts/run_benchmark.py


Isse:
- model load hota hai  
- data folder ke audio transcribe hote hain  
- WER calculate hota hai  
- results folder me output JSON file create ho jata hai  

-Output
Benchmark ka result yaha save hota hai:


results/faster_whisper_results.json


Isme har audio file ka predicted text, WER aur inference time mil jata hai.

-Notes
- audio files `.wav` format me hone chahiye  
- Faster-Whisper CPU par bhi kaafi fast chal jata hai  
- pura project simple testing aur learning purpose ke liye banaya gaya hai  


Name - Vaibhav Dhabekar
AI ML Developer.

