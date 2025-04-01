import os
import gemini_srt_translator as gst

gst.gemini_api_key = "YOUR_GEMINI_API_KEY" #your gemini api key
gst.gemini_api_key2 = "YOUR_GEMINI_API_KEY" #your other gemini api key/spare key
gst.target_language = "English"
gst.start_line = 1
gst.description = "Youtube video of Korean talk show" #prompt for them to do the translation with eg.: there are 3 people in this video, speaker1: name, speaker2: name, ... remove speaker label after translation (files with speaker diarization )
gst.model_name = "gemini-2.0-flash" # gemini-2.0-flash # gemini-2.0-flash-lite # gemini-1.5-pro # gemini-2.0-flash-exp # gemini-2.0-flash-thinking-exp-01-21
gst.batch_size = 30 #default, bigger the number faster the translation (not recommended)
gst.free_quota = False #Skip version upgrade check (default: False).
gst.skip_upgrade = True #Use colors in the console output (default: True).

input_directory = "original_file" #your folder of original language files
output_directory = "translated_file" #your folder of translated files

# --- End Configuration ---

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created output directory: {output_directory}")

# Get list of .srt files in the input directory
try:
    files_to_process = [f for f in os.listdir(input_directory) if f.endswith(".srt")]
except FileNotFoundError:
    print(f"Error: Input directory '{input_directory}' not found.")
    exit() # Exit if input directory doesn't exist

if not files_to_process:
    print(f"No .srt files found in '{input_directory}'.")
    exit()

print(f"Found {len(files_to_process)} .srt files in '{input_directory}'.")

# Process each file
for filename in files_to_process:
    input_filepath = os.path.join(input_directory, filename)
    # Construct the output filepath with the same filename in the output directory
    output_filepath = os.path.join(output_directory, filename)

    print("-" * 20)
    print(f"Processing: {filename}")

    # 1. Check if the translated file already exists
    if os.path.exists(output_filepath):
        print(f"Skipping: Output file already exists at '{output_filepath}'")
        continue # Skip to the next file

    # 2. Set input and output for the translator
    gst.input_file = input_filepath
    gst.output_file = output_filepath # Set the desired output path

    # 3. Translate the file
    try:
        print(f"Translating '{input_filepath}' to '{output_filepath}'...")
        gst.translate() # Call the translation function
        print("Translation complete.")
    except Exception as e:
        print(f"Error translating {filename}: {e}")
        # Optional: Decide if you want to stop or continue on error
        # continue

print("-" * 20)
print("Finished processing all files.")
