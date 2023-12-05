import pandas as pd
from docx import Document
from collections import defaultdict

def calculate_conditional_probabilities(df, base_column, conditional_columns):
    probabilities_data = []
    all_probabilities = {}
    
    for conditional_column in conditional_columns:
        # Count the co-occurrences and the total occurrences
        co_occurrences = defaultdict(int)
        total_occurrences = defaultdict(int)

        for index, row in df.iterrows():
            base_value = row[base_column]
            conditional_value = row[conditional_column]

            co_occurrences[(base_value, conditional_value)] += 1
            total_occurrences[base_value] += 1

        # Calculate the conditional probabilities
        for (base_value, conditional_value), count in co_occurrences.items():
            probability = round(count / total_occurrences[base_value], 3)
            all_probabilities[(base_value, conditional_value)] = probability
            probabilities_data.append({
                f'{base_column}': base_value,
                'Next Image': conditional_value,
                'Probability': probability
            })
            
    return all_probabilities, probabilities_data

def save_probabilities_to_docx(probabilities, filename):
    doc = Document()
    for (base_value, conditional_value), probability in probabilities.items():
        text = f"p({conditional_value}|{base_value}) = {probability:.2f}"
        doc.add_paragraph(text, style='Normal')
    doc.save(filename)

def save_probabilities_to_csv(probabilities_data, filename):
    df = pd.DataFrame(probabilities_data)
    df.to_csv(filename, index=False)

def main():
    # Load the data
    df = pd.read_csv('Study3_learningtrials.csv')
    
    # Calculate the conditional probabilities
    sr_probabilities, sr_probabilities_data = calculate_conditional_probabilities(df, 's1_image', ['s3_image', 's2_image'])
    pr_probabilities, pr_probabilities_data = calculate_conditional_probabilities(df, 's3_image', ['s1_image']) # Assuming you meant s3_image here
    pr2_probabilities, pr2_probabilities_data = calculate_conditional_probabilities(df, 's3_image', ['s2_image'])
    
    # Combine PR probabilities and data
    pr_probabilities.update(pr2_probabilities)
    pr_probabilities_data.extend(pr2_probabilities_data)
    
    # Save the results to Word documents
    save_probabilities_to_docx(sr_probabilities, 'SR_probabilities.docx')
    save_probabilities_to_docx(pr_probabilities, 'PR_probabilities.docx')
    
    # Save the results to CSV files
    save_probabilities_to_csv(sr_probabilities_data, 'SR_probabilities.csv')
    save_probabilities_to_csv(pr_probabilities_data, 'PR_probabilities.csv')

if __name__ == "__main__":
    main()
