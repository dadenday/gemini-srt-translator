import os
import gemini_srt_translator as gst

gst.gemini_api_key = "AIzaSyCmnbIlIIy80WWpWriI4JjyOBZE9pgROdU"
gst.gemini_api_key2 = "AIzaSyDtgkujjhMRYddTd9_yyt5uLiXkeGguOpg" #AIzaSyBVCiozEH0l_Y2oYIIBMSCl-RL-8pYHUnM
gst.target_language = "English"
#gst.input_file = "NEW/NEW NEW DEUN DEUN.srt"
#gst.output_file = "DONE/NEW NEW DEUN DEUN (DONE).srt"
gst.start_line = 1
gst.description = "Youtube video of Korean talk show"
gst.model_name = "gemini-2.0-flash" # gemini-2.0-flash # gemini-2.0-flash-lite # gemini-1.5-pro # gemini-2.0-flash-exp # gemini-2.0-flash-thinking-exp-01-21
gst.batch_size = 30
gst.free_quota = True
gst.skip_upgrade = True

input_directory = "NEW"
output_directory = "DONE"

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
