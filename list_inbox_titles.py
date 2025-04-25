import os
from pathlib import Path

# Define the articles directory
articles_dir = Path("articles")

# Get all .txt files
article_files = list(articles_dir.glob("*.txt"))

# Display the list of articles with indices
print("Article Titles:")
for idx, file in enumerate(article_files, start=1):
    print(f"{idx}. {file.stem}")

# Prompt user to select articles
selection = input("\nEnter the numbers of articles to create .txt files for (comma-separated), or 'all' to select all: ")

# Determine selected files
if selection.strip().lower() == 'all':
    selected_files = article_files
else:
    try:
        indices = [int(i.strip()) - 1 for i in selection.split(',') if i.strip().isdigit()]
        selected_files = [article_files[i] for i in indices if 0 <= i < len(article_files)]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        exit()

# Create .txt files for selected articles
output_dir = Path("inbox")
output_dir.mkdir(parents=True, exist_ok=True)

for file_path in selected_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from the first line
    lines = content.strip().splitlines()
    title = lines[0] if lines else "Untitled Article"

    # Prompt user for additional metadata
    meta_title = input(f"\nEnter Meta Title for '{title}': ")
    description = input(f"Enter Meta Description for '{title}': ")
    summary = input(f"Enter Summary for '{title}': ")
    goal = input(f"Enter Goal for '{title}': ")
    tone = input(f"Enter Tone for '{title}': ")
    keywords = input(f"Enter Keywords (for SEO) for '{title}': ")
    writer = input(f"Enter Writer for '{title}': ")
    publish_date = input(f"Enter Target Publish Date for '{title}': ")

    # Define the output file path
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
    output_file = output_dir / f"{safe_title}.txt"

    # Write the structured content to the new .txt file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Title: {title}\n")
        f.write(f"## Meta Title: {meta_title}\n")
        f.write(f"## Meta Description:\n{description}\n\n")
        f.write(f"## Summary:\n{summary}\n\n")
        f.write(f"## Goal:\n{goal}\n\n")
        f.write(f"## Tone:\n{tone}\n\n")
        f.write(f"## Keywords (for SEO):\n{keywords}\n\n")
        f.write(f"## Writer:\n{writer}\n\n")
        f.write(f"## Target Publish Date:\n{publish_date}\n\n")
        f.write("## Content:\n")
        f.write(content)

    print(f"✅ Created: {output_file.name}")

print("\nAll selected articles have been processed.")