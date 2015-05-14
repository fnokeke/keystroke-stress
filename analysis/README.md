There are three scripts for data analysis: get_keystroke_features.py, get_app_features.py, and stress_prediction.py


get_keystroke_features.py: This script is to extract high level features (for more details about what high level features we use, please refer to section "feature extraction" in our paper) from raw mouse click and keystroke features, and the extracted features will be stored in a CSV file under directory "keystroke_fatures". To run the script, first put your raw keystroke feature file under the directory "keystroke_data", then change the filename to the name of your file with the file extentsion being removed, then run the script. A CSV file called "features_[your_filename].csv" will be generated under directory "keystroke_features".  


get_app_features.py: This script is 

