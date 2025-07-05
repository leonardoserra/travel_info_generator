import os
import sys
import argparse

from pathlib import Path

def generate_merged_report(args):
    output_filename = args.output if args.output else 'travel_report'
    output_filename += ".md" 

    current_dir = os.path.dirname(os.path.abspath(__file__))

    merged_dir = os.path.join(current_dir, 'merged/')
    reports_dir = os.path.join(current_dir, 'reports/')

    Path(merged_dir).mkdir(parents=True, exist_ok=True)
    Path(reports_dir).mkdir(parents=True, exist_ok=True)

    md_files = [f for f in os.listdir(reports_dir) if f.endswith('.md') and f != output_filename]

    md_files.sort()
    with open(os.path.join(merged_dir, output_filename), 'w', encoding='utf-8') as outfile:
        for filename in md_files:
            filepath = os.path.join(reports_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n___\n\n")

    print(f"Generated merged file: {output_filename}")


def main(args):
    
    try:
        generate_merged_report(args)
        return 0

    except Exception as e:
        print(str(e))
        return 1


def cli():
    parser = argparse.ArgumentParser(description="It generates a travel report based on the input provided.")

    parser.add_argument('--output', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = cli()

    code = main(args)

    sys.exit(code)